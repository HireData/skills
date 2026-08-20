#!/usr/bin/env python3
"""Deterministic pull-request gate for the rules in CONTRIBUTING.md and README.md.

Runs on untrusted pull-request code with no repository secrets. It never posts to
GitHub; it writes findings and a redacted review context to an artifact directory
that the trusted review workflow consumes.

Usage:
    python3 scripts/check_pr_rules.py \
        --base-sha <sha> --head-sha <sha> \
        --pr-body-file body.md --pr-number 12 --pr-author octocat \
        --pr-title "..." --out pr-review
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_PREFIX = "plugins/hiredata/skills/"
REGRESSION_PATH = "evals/regression-cases.json"
SUBMISSION_PATH = "evals/submission-cases.json"

MANIFEST_PATHS = [
    "plugins/hiredata/.codex-plugin/plugin.json",
    "plugins/hiredata/.claude-plugin/plugin.json",
    ".claude-plugin/marketplace.json",
]

# Flip any rule to "warning" to stop it from blocking a pull request.
SEVERITY = {
    "structure": "blocking",
    "eval-updated": "blocking",
    "eval-coverage": "blocking",
    "eval-quality": "blocking",
    "pr-evidence": "blocking",
    "pr-checklist": "blocking",
    "secrets": "blocking",
    "references-depth": "blocking",
    "version-bump": "blocking",
    "skill-name": "warning",
    "skill-length": "warning",
    "description-trigger": "warning",
}

# Verb-led skill names, per CONTRIBUTING.md ("preferably verb-led").
VERB_PREFIXES = {
    "analyze", "audit", "build", "check", "compare", "compose", "configure",
    "convert", "create", "design", "detect", "diagnose", "draft", "explain",
    "export", "extract", "find", "generate", "import", "improve", "inspect",
    "investigate", "map", "migrate", "monitor", "plan", "prepare", "publish",
    "refine", "report", "resolve", "review", "run", "schedule", "score",
    "summarize", "sync", "test", "trace", "translate", "triage", "update",
    "validate", "verify", "write",
}

# Phrases that signal a description says *when* the skill should fire, not just what it does.
TRIGGER_TOKENS = (
    "use when", "use this", "use for", "use it", "use whenever", "trigger",
    "when a", "when the", "when someone", "when you", "when users", "when a user",
    "for when", "applies when", "invoke",
)

# Credential and personal-data shapes that must never enter a public repository.
SECRET_PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("Anthropic API key", re.compile(r"sk-ant-[A-Za-z0-9_\-]{16,}")),
    ("OpenAI API key", re.compile(r"\bsk-(?:proj-)?[A-Za-z0-9]{32,}")),
    ("GitHub token", re.compile(r"\b(?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9]{20,}")),
    ("GitHub fine-grained token", re.compile(r"\bgithub_pat_[A-Za-z0-9_]{20,}")),
    ("AWS access key id", re.compile(r"\b(?:AKIA|ASIA)[0-9A-Z]{16}\b")),
    ("Slack token", re.compile(r"\bxox[abprs]-[A-Za-z0-9-]{10,}")),
    ("Google API key", re.compile(r"\bAIza[0-9A-Za-z_\-]{35}\b")),
    ("private key block", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |PGP )?PRIVATE KEY-----")),
    ("JSON web token", re.compile(r"\beyJ[A-Za-z0-9_\-]{10,}\.[A-Za-z0-9_\-]{10,}\.[A-Za-z0-9_\-]{10,}")),
    ("hardcoded secret assignment", re.compile(
        r"(?i)\b(?:password|passwd|secret|api[_-]?key|access[_-]?token|client[_-]?secret)\b\s*[:=]\s*['\"][^'\"\s]{8,}['\"]"
    )),
    ("bearer token", re.compile(r"(?i)\bauthorization\s*:\s*bearer\s+[A-Za-z0-9._\-]{16,}")),
]

# Placeholder domains that are safe to use in documentation and eval prompts.
ALLOWED_EMAIL_DOMAINS = {
    "hiredata.com", "example.com", "example.org", "example.net",
    "users.noreply.github.com", "acme.example", "sandbox.example",
}
EMAIL_PATTERN = re.compile(r"\b[A-Za-z0-9._%+\-]+@([A-Za-z0-9.\-]+\.[A-Za-z]{2,})\b")

CHECKLIST_PATTERN = re.compile(r"^\s*[-*]\s*\[( |x|X)\]\s*(.+?)\s*$", re.MULTILINE)
EVIDENCE_ROW_PATTERN = re.compile(r"^\s*\|(?!\s*[-: ]+\|)(.+)\|\s*$", re.MULTILINE)
SEMVER_PATTERN = re.compile(r"^\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?$")

MAX_SKILL_MD_LINES = 220
MAX_DIFF_CHARS = 160_000
MAX_FILE_CHARS = 24_000


def run(*args: str) -> str:
    return subprocess.run(args, cwd=ROOT, check=False, capture_output=True, text=True).stdout


class Gate:
    def __init__(self, base: str, head: str, body: str) -> None:
        self.base = base
        self.head = head
        self.body = body or ""
        self.findings: list[dict[str, str]] = []
        self.changed = self._changed_files()
        self.added_lines = self._added_lines()

    # ---------------------------------------------------------------- helpers

    def add(self, rule: str, title: str, problem: str, fix: str, where: str = "") -> None:
        self.findings.append({
            "rule": rule,
            "severity": SEVERITY.get(rule, "blocking"),
            "source": "deterministic",
            "title": title,
            "where": where,
            "problem": problem,
            "fix": fix,
        })

    def _changed_files(self) -> list[str]:
        out = run("git", "diff", "--name-only", f"{self.base}...{self.head}")
        return [line for line in out.splitlines() if line.strip()]

    def _added_lines(self) -> list[tuple[str, str]]:
        """(path, line) for every line this pull request adds."""
        out = run("git", "diff", "--unified=0", f"{self.base}...{self.head}")
        current = ""
        lines: list[tuple[str, str]] = []
        for line in out.splitlines():
            if line.startswith("+++ b/"):
                current = line[6:]
            elif line.startswith("+") and not line.startswith("+++"):
                lines.append((current, line[1:]))
        return lines

    def file_at(self, ref: str, path: str) -> str | None:
        result = subprocess.run(
            ["git", "show", f"{ref}:{path}"], cwd=ROOT,
            check=False, capture_output=True, text=True,
        )
        return result.stdout if result.returncode == 0 else None

    def json_at(self, ref: str, path: str) -> dict:
        raw = self.file_at(ref, path)
        if raw is None:
            return {}
        try:
            return json.loads(raw)
        except json.JSONDecodeError:
            return {}

    def changed_skills(self) -> list[str]:
        names: list[str] = []
        for path in self.changed:
            if path.startswith(SKILLS_PREFIX):
                name = path[len(SKILLS_PREFIX):].split("/", 1)[0]
                if name and name not in names:
                    names.append(name)
        return sorted(names)

    # ----------------------------------------------------------------- checks

    def check_structure(self) -> None:
        result = subprocess.run(
            [sys.executable, "scripts/validate_repo.py"], cwd=ROOT,
            check=False, capture_output=True, text=True,
        )
        if result.returncode == 0:
            return
        details = [
            line.lstrip("- ").strip()
            for line in result.stdout.splitlines()
            if line.startswith("- ")
        ] or [(result.stdout + result.stderr).strip()[:800] or "validator exited non-zero"]
        for detail in details:
            self.add(
                "structure",
                "Structural validation fails",
                detail,
                "Run `python3 scripts/validate_repo.py` locally and fix the reported item. "
                "CONTRIBUTING.md requires this gate to pass before merge.",
            )

    def check_evals(self) -> None:
        skills = self.changed_skills()
        if not skills:
            return

        if REGRESSION_PATH not in self.changed:
            self.add(
                "eval-updated",
                "No eval evidence for a changed skill",
                f"This pull request changes {', '.join(skills)} but does not touch {REGRESSION_PATH}.",
                "CONTRIBUTING.md → Add evidence: every pull request must add or update eval cases in "
                f"`{REGRESSION_PATH}` covering a normal case, a missing/ambiguous-data case, and a "
                "safety or invalid-combination case for the changed skill.",
                REGRESSION_PATH,
            )

        base_cases = {
            case.get("id"): case
            for case in self.json_at(self.base, REGRESSION_PATH).get("cases", [])
        }
        head_data = self.json_at(self.head, REGRESSION_PATH)
        head_cases = head_data.get("cases", [])
        expected_kinds = {"normal", "ambiguous", "safety"}

        for skill in skills:
            skill_dir = ROOT / SKILLS_PREFIX / skill
            if not skill_dir.is_dir():
                continue  # deleted skill; validate_repo.py covers the consequences
            mine = [case for case in head_cases if case.get("skill") == skill]
            missing = expected_kinds - {case.get("kind") for case in mine}
            if missing:
                self.add(
                    "eval-coverage",
                    f"`{skill}` is missing regression kinds",
                    f"No {', '.join(sorted(missing))} case exists for `{skill}`.",
                    f"Add one case per missing kind to `{REGRESSION_PATH}` with a unique `id`, the "
                    f"`skill` set to `{skill}`, and populated `prompt`, `must`, and `must_not` fields.",
                    REGRESSION_PATH,
                )
            touched = [case for case in mine if base_cases.get(case.get("id")) != case]
            if not touched and REGRESSION_PATH in self.changed:
                self.add(
                    "eval-updated",
                    f"`{skill}` changed without new or updated eval cases",
                    f"`{REGRESSION_PATH}` changed, but no case belonging to `{skill}` was added or modified.",
                    "Add or update at least one regression case that demonstrates the behaviour this "
                    "change is meant to improve, so the diff carries its own evidence.",
                    REGRESSION_PATH,
                )
            for case in mine:
                if base_cases.get(case.get("id")) == case:
                    continue
                for field in ("prompt", "must", "must_not"):
                    if not case.get(field):
                        self.add(
                            "eval-quality",
                            f"Eval case `{case.get('id')}` is incomplete",
                            f"Field `{field}` is empty.",
                            "Every regression case needs a concrete `prompt`, a `must` list of behaviours "
                            "the output has to show, and a `must_not` list of failures that block the change.",
                            REGRESSION_PATH,
                        )

    def check_pr_body(self) -> None:
        boxes = CHECKLIST_PATTERN.findall(self.body)
        if not boxes:
            self.add(
                "pr-checklist",
                "Pull-request description does not use the template",
                "No checklist items were found in the description.",
                "Copy `.github/pull_request_template.md` into the description and complete every "
                "section: problem or user story, change, evidence table, and checklist.",
            )
        else:
            unchecked = [text for mark, text in boxes if mark == " "]
            if unchecked:
                shown = "\n".join(f"  - {item}" for item in unchecked[:10])
                self.add(
                    "pr-checklist",
                    "Unchecked items in the contribution checklist",
                    f"{len(unchecked)} item(s) are still unchecked:\n{shown}",
                    "Complete each item and tick its box, or state in the description why the item does "
                    "not apply to this change.",
                )

        if not self.changed_skills():
            return

        rows = [
            [cell.strip() for cell in row.split("|")]
            for row in EVIDENCE_ROW_PATTERN.findall(self.body)
        ]
        scored = [
            row for row in rows
            if sum(1 for cell in row if re.fullmatch(r"\d+(?:\.\d+)?(?:\s*/\s*\d+)?", cell)) >= 2
        ]
        if len(scored) < 3:
            self.add(
                "pr-evidence",
                "Evidence table is missing baseline and candidate scores",
                f"Found {len(scored)} scored row(s); the template expects a baseline and a candidate "
                "score for the normal, ambiguous, and safety cases.",
                "Score both the previous/no-skill baseline and the candidate against `evals/RUBRIC.md` in "
                "fresh contexts, fill all three rows of the evidence table, and link the anonymized "
                "outputs, tool traces, and reviewer notes.",
            )

    def check_secrets(self) -> None:
        for path, line in self.added_lines:
            if path.startswith(".github/workflows/") or path.startswith("scripts/"):
                continue  # this gate's own patterns and workflow secret references
            for label, pattern in SECRET_PATTERNS:
                if pattern.search(line):
                    article = "an" if label[0].lower() in "aeiou" else "a"
                    self.add(
                        "secrets",
                        f"Possible {label} in the diff",
                        f"`{path}` adds a line matching {article} {label} pattern.",
                        "Remove the value, rotate it if it was ever real, and reference a placeholder or "
                        "an environment variable instead. CONTRIBUTING.md forbids contributing customer "
                        "data, credentials, or confidential HireData information.",
                        path,
                    )
                    break
            for domain in EMAIL_PATTERN.findall(line):
                if domain.lower() not in ALLOWED_EMAIL_DOMAINS:
                    self.add(
                        "secrets",
                        "Possible real personal or customer email address",
                        f"`{path}` adds an address at `{domain}`.",
                        "Replace it with an `@example.com` placeholder unless it is an official HireData "
                        "contact address.",
                        path,
                    )
                    break

    def check_references_depth(self) -> None:
        for path in self.changed:
            if not path.startswith(SKILLS_PREFIX) or "/references/" not in path:
                continue
            tail = path.split("/references/", 1)[1]
            if "/" in tail:
                self.add(
                    "references-depth",
                    "Reference file is nested too deeply",
                    f"`{path}` sits below `references/`.",
                    "CONTRIBUTING.md requires one-level-deep `references/` files. Move the content to "
                    "`references/<name>.md` and link it from `SKILL.md`.",
                    path,
                )

    def check_version_bump(self) -> None:
        if not any(path.startswith("plugins/") for path in self.changed):
            return
        versions: dict[str, tuple[str, str]] = {}
        for path in MANIFEST_PATHS:
            base_doc = self.json_at(self.base, path)
            head_doc = self.json_at(self.head, path)
            if path.endswith("marketplace.json"):
                def pick(doc: dict) -> str:
                    entry = next(
                        (item for item in doc.get("plugins", [])
                         if isinstance(item, dict) and item.get("name") == "hiredata"),
                        {},
                    )
                    return str(entry.get("version", ""))
            else:
                def pick(doc: dict) -> str:
                    return str(doc.get("version", ""))
            versions[path] = (pick(base_doc), pick(head_doc))

        unbumped = [path for path, (old, new) in versions.items() if old == new]
        if len(unbumped) == len(MANIFEST_PATHS):
            current = versions[MANIFEST_PATHS[0]][1] or "unknown"
            self.add(
                "version-bump",
                "Plugin content changed without a version bump",
                f"Files under `plugins/` changed but the version stayed at {current}.",
                "RELEASE_CHECKLIST.md: bump `version` identically in "
                "`plugins/hiredata/.codex-plugin/plugin.json`, "
                "`plugins/hiredata/.claude-plugin/plugin.json`, and the `hiredata` entry in "
                "`.claude-plugin/marketplace.json`. Claude only delivers plugin updates when the "
                "version field changes.",
            )
        elif unbumped:
            self.add(
                "version-bump",
                "Version bumped inconsistently across manifests",
                "Not every manifest carries the new version: " + ", ".join(f"`{p}`" for p in unbumped),
                "Set the same semantic version in all three manifest locations.",
            )
        for path, (_, new) in versions.items():
            if new and not SEMVER_PATTERN.fullmatch(new):
                self.add(
                    "version-bump",
                    "Version is not semantic versioning",
                    f"`{path}` has version `{new}`.",
                    "Use MAJOR.MINOR.PATCH, optionally with a pre-release suffix.",
                    path,
                )

    def check_skill_shape(self) -> None:
        for skill in self.changed_skills():
            skill_md = ROOT / SKILLS_PREFIX / skill / "SKILL.md"
            if not skill_md.is_file():
                continue
            stem = skill[len("hiredata-"):] if skill.startswith("hiredata-") else skill
            verb = stem.split("-")[0]
            if verb and verb not in VERB_PREFIXES:
                self.add(
                    "skill-name",
                    f"`{skill}` is not verb-led",
                    f"The name reads as `{verb}...` rather than an action.",
                    "CONTRIBUTING.md prefers lowercase, hyphenated, verb-led names such as "
                    "`hiredata-create-forms` or `hiredata-diagnose-automations`.",
                    f"{SKILLS_PREFIX}{skill}/SKILL.md",
                )

            text = skill_md.read_text(encoding="utf-8")
            body_lines = len(text.splitlines())
            if body_lines > MAX_SKILL_MD_LINES:
                self.add(
                    "skill-length",
                    f"`{skill}` SKILL.md is long",
                    f"{body_lines} lines, above the {MAX_SKILL_MD_LINES}-line guideline.",
                    "Keep the main workflow concise and move detailed rules and examples into "
                    "one-level-deep `references/` files.",
                    f"{SKILLS_PREFIX}{skill}/SKILL.md",
                )

            description = ""
            lines = text.splitlines()
            if lines and lines[0] == "---":
                for line in lines[1:]:
                    if line == "---":
                        break
                    if line.startswith("description:"):
                        description = line.split(":", 1)[1].strip()
            if description and not any(
                token in description.lower() for token in TRIGGER_TOKENS
            ):
                self.add(
                    "description-trigger",
                    f"`{skill}` description does not say when to trigger",
                    "The description explains what the skill does but not the situations that should "
                    "invoke it.",
                    "CONTRIBUTING.md: make the description say what the skill does *and* when it should "
                    "trigger, e.g. \"... Use when a user needs to ...\".",
                    f"{SKILLS_PREFIX}{skill}/SKILL.md",
                )

    def run_all(self) -> None:
        self.check_structure()
        self.check_evals()
        self.check_pr_body()
        self.check_secrets()
        self.check_references_depth()
        self.check_version_bump()
        self.check_skill_shape()


def build_context(gate: Gate, meta: dict) -> dict:
    """Redacted, size-bounded material for the trusted Claude review step."""
    diff = run("git", "diff", f"{gate.base}...{gate.head}", "--", ".")
    truncated = len(diff) > MAX_DIFF_CHARS
    sources: dict[str, str] = {}
    for skill in gate.changed_skills():
        skill_md = ROOT / SKILLS_PREFIX / skill / "SKILL.md"
        if skill_md.is_file():
            sources[f"{SKILLS_PREFIX}{skill}/SKILL.md"] = skill_md.read_text(
                encoding="utf-8")[:MAX_FILE_CHARS]
    for doc in ("CONTRIBUTING.md", "evals/RUBRIC.md", "README.md"):
        path = ROOT / doc
        if path.is_file():
            sources[doc] = path.read_text(encoding="utf-8")[:MAX_FILE_CHARS]
    return {
        "meta": meta,
        "changed_files": gate.changed,
        "changed_skills": gate.changed_skills(),
        "diff": diff[:MAX_DIFF_CHARS],
        "diff_truncated": truncated,
        "sources": sources,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-sha", required=True)
    parser.add_argument("--head-sha", required=True)
    parser.add_argument("--pr-body-file", default="")
    parser.add_argument("--pr-number", default="")
    parser.add_argument("--pr-title", default="")
    parser.add_argument("--pr-author", default="")
    parser.add_argument("--out", default="pr-review")
    args = parser.parse_args()

    body = ""
    if args.pr_body_file and Path(args.pr_body_file).is_file():
        body = Path(args.pr_body_file).read_text(encoding="utf-8")

    gate = Gate(args.base_sha, args.head_sha, body)
    gate.run_all()

    meta = {
        "pr_number": args.pr_number,
        "pr_title": args.pr_title,
        "pr_author": args.pr_author,
        "pr_body": body[:MAX_FILE_CHARS],
        "base_sha": args.base_sha,
        "head_sha": args.head_sha,
        "repository": os.environ.get("GITHUB_REPOSITORY", ""),
    }

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "findings.json").write_text(
        json.dumps({"findings": gate.findings, "meta": meta}, indent=2), encoding="utf-8")
    (out_dir / "context.json").write_text(
        json.dumps(build_context(gate, meta), indent=2), encoding="utf-8")

    blocking = [f for f in gate.findings if f["severity"] == "blocking"]
    warnings = [f for f in gate.findings if f["severity"] == "warning"]
    for finding in gate.findings:
        marker = "BLOCK" if finding["severity"] == "blocking" else " WARN"
        print(f"[{marker}] {finding['rule']}: {finding['title']}")
        print(f"        {finding['problem']}")
    print(f"\n{len(blocking)} blocking, {len(warnings)} warning(s), "
          f"{len(gate.changed)} changed file(s).")
    return 1 if blocking else 0


if __name__ == "__main__":
    sys.exit(main())
