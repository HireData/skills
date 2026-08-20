#!/usr/bin/env python3
"""Merge the deterministic and judgment findings and report the verdict on the PR.

Posts (or updates) one sticky comment, requests changes when a rule is broken,
dismisses its own stale change requests once a pull request is clean, and sets the
`PR rules` commit status so the result can be made a required check.

Runs only in the trusted workflow. It reads artifacts and never checks out
pull-request code.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request

MARKER = "<!-- hiredata-skills-pr-rules -->"
STATUS_CONTEXT = "PR rules"
API = "https://api.github.com"

RULE_DOCS = {
    "structure": "CONTRIBUTING.md → Review checklist",
    "eval-updated": "CONTRIBUTING.md → Add evidence",
    "eval-coverage": "CONTRIBUTING.md → Add evidence",
    "eval-quality": "evals/RUBRIC.md",
    "pr-evidence": "evals/RUBRIC.md → Comparison gate",
    "pr-checklist": ".github/pull_request_template.md",
    "secrets": "CONTRIBUTING.md → Contributing / SECURITY.md",
    "references-depth": "CONTRIBUTING.md → Build the skill",
    "version-bump": "RELEASE_CHECKLIST.md",
    "skill-name": "CONTRIBUTING.md → Build the skill",
    "skill-length": "CONTRIBUTING.md → Build the skill",
    "description-trigger": "CONTRIBUTING.md → Build the skill",
    "J1": "CONTRIBUTING.md → Choose the work",
    "J2": "README.md → Principles",
    "J3": "README.md → Principles",
    "J4": "README.md → Principles",
    "J5": "CONTRIBUTING.md → Build the skill",
    "J6": "CONTRIBUTING.md → Build the skill",
    "J7": "CONTRIBUTING.md → Review checklist",
    "J8": "README.md → Principles",
    "J9": "CONTRIBUTING.md → Review checklist",
    "J10": "CONTRIBUTING.md → Build the skill",
    "J11": "CONTRIBUTING.md → Add evidence",
    "J12": "evals/RUBRIC.md → Comparison gate",
}


def request(method: str, path: str, token: str, payload: dict | None = None) -> object:
    url = path if path.startswith("http") else f"{API}{path}"
    data = json.dumps(payload).encode("utf-8") if payload is not None else None
    req = urllib.request.Request(
        url, data=data, method=method,
        headers={
            "authorization": f"Bearer {token}",
            "accept": "application/vnd.github+json",
            "x-github-api-version": "2022-11-28",
            "content-type": "application/json",
            "user-agent": "hiredata-skills-pr-rules",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as response:
            body = response.read().decode("utf-8")
        return json.loads(body) if body else {}
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", "replace")[:400]
        print(f"{method} {path} -> HTTP {exc.code}: {detail}", file=sys.stderr)
        raise


def render_finding(index: int, finding: dict) -> str:
    where = f" — `{finding['where']}`" if finding.get("where") else ""
    doc = RULE_DOCS.get(finding.get("rule", ""), "")
    lines = [f"**{index}. {finding['title']}**{where}"]
    if finding.get("problem"):
        lines.append("")
        lines.append(finding["problem"])
    if finding.get("fix"):
        lines.append("")
        lines.append(f"*How to fix:* {finding['fix']}")
    if doc:
        lines.append("")
        lines.append(f"<sub>Rule `{finding['rule']}` · {doc}</sub>")
    return "\n".join(lines)


def render_comment(blocking: list[dict], warnings: list[dict], ai: dict, handle: str,
                   head_sha: str) -> str:
    out = [MARKER]
    if blocking:
        out.append("## ❌ Changes requested — this pull request does not yet meet the repository rules\n")
        out.append(
            f"{len(blocking)} rule "
            f"{'violation' if len(blocking) == 1 else 'violations'} must be resolved before this "
            "can be approved. Each item below names the rule, what is wrong, and what to change.\n"
        )
        out.append("### Must fix\n")
        out.extend(render_finding(i, f) + "\n" for i, f in enumerate(blocking, 1))
    else:
        mention = f"@{handle} " if handle else ""
        out.append("## ✅ Adheres to the repository rules\n")
        out.append(
            f"{mention}this pull request passes every automated rule check — structural validation, "
            "eval evidence, contribution checklist, and the judgment review against `CONTRIBUTING.md` "
            "and `evals/RUBRIC.md`. Ready for your review.\n"
        )

    if ai.get("summary"):
        out.append(f"### Review summary\n\n{ai['summary']}\n")

    if warnings:
        out.append(
            f"<details>\n<summary>Non-blocking suggestions ({len(warnings)})</summary>\n"
        )
        out.extend("\n" + render_finding(i, f) + "\n" for i, f in enumerate(warnings, 1))
        out.append("</details>\n")

    if ai.get("status") == "skipped":
        out.append(
            "> ⚠️ The judgment review was skipped: no `ANTHROPIC_API_KEY` secret is configured. "
            "Only the deterministic rules ran.\n"
        )
    elif ai.get("status") == "error":
        out.append(f"> ⚠️ The judgment review could not run: {ai.get('summary', 'unknown error')}\n")

    out.append(
        f"<sub>Checked `{head_sha[:7]}` against `CONTRIBUTING.md`, `README.md`, "
        "`RELEASE_CHECKLIST.md`, and `evals/RUBRIC.md`. Run `python3 scripts/check_pr_rules.py` "
        "locally with the same base to reproduce the deterministic half. "
        "Push a new commit to re-run this check.</sub>"
    )
    return "\n".join(out)


def review_body(blocking: list[dict]) -> str:
    lines = [
        "This pull request does not yet adhere to the rules in `CONTRIBUTING.md`, "
        "`README.md`, and `RELEASE_CHECKLIST.md`.\n",
    ]
    lines.extend(render_finding(i, f) + "\n" for i, f in enumerate(blocking, 1))
    lines.append(
        "Push the fixes to this branch and the check will re-run automatically. "
        "Reply here if you think a rule does not apply to this change."
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--findings", required=True)
    parser.add_argument("--ai", required=True)
    parser.add_argument("--handle", default="")
    args = parser.parse_args()

    token = os.environ["GITHUB_TOKEN"]
    repo = os.environ["GITHUB_REPOSITORY"]

    with open(args.findings, encoding="utf-8") as handle:
        det = json.load(handle)
    try:
        with open(args.ai, encoding="utf-8") as handle:
            ai = json.load(handle)
    except (OSError, json.JSONDecodeError):
        ai = {"summary": "", "findings": [], "status": "error"}

    meta = det.get("meta", {})
    pr_number = str(meta.get("pr_number", "")).strip()
    head_sha = str(meta.get("head_sha", "")).strip()
    if not pr_number or not head_sha:
        print("no pull-request metadata in the artifact; nothing to post", file=sys.stderr)
        return 1

    findings = list(det.get("findings", [])) + list(ai.get("findings", []))
    blocking = [f for f in findings if f.get("severity") == "blocking"]
    warnings = [f for f in findings if f.get("severity") != "blocking"]

    body = render_comment(blocking, warnings, ai, args.handle, head_sha)

    # One sticky comment per pull request, updated in place.
    comments = request("GET", f"/repos/{repo}/issues/{pr_number}/comments?per_page=100", token)
    existing = next(
        (c for c in comments if isinstance(c, dict) and MARKER in (c.get("body") or "")), None)
    if existing:
        request("PATCH", f"/repos/{repo}/issues/comments/{existing['id']}", token, {"body": body})
    else:
        request("POST", f"/repos/{repo}/issues/{pr_number}/comments", token, {"body": body})

    reviews = request("GET", f"/repos/{repo}/pulls/{pr_number}/reviews?per_page=100", token)
    ours = [
        r for r in reviews
        if isinstance(r, dict)
        and r.get("state") == "CHANGES_REQUESTED"
        and (r.get("user") or {}).get("login") in ("github-actions[bot]", "github-actions")
    ]

    if blocking:
        try:
            request("POST", f"/repos/{repo}/pulls/{pr_number}/reviews", token, {
                "commit_id": head_sha,
                "body": review_body(blocking),
                "event": "REQUEST_CHANGES",
            })
        except urllib.error.HTTPError:
            print("could not submit a review; the sticky comment still carries the verdict",
                  file=sys.stderr)
    else:
        for review in ours:
            try:
                request(
                    "PUT",
                    f"/repos/{repo}/pulls/{pr_number}/reviews/{review['id']}/dismissals",
                    token,
                    {"message": "All rule violations were resolved on a later commit.",
                     "event": "DISMISS"},
                )
            except urllib.error.HTTPError:
                print(f"could not dismiss review {review['id']}", file=sys.stderr)

    run_url = (
        f"{os.environ.get('GITHUB_SERVER_URL', 'https://github.com')}/{repo}/actions/runs/"
        f"{os.environ.get('GITHUB_RUN_ID', '')}"
    )
    description = (
        f"{len(blocking)} rule violation{'' if len(blocking) == 1 else 's'}"
        if blocking else "Adheres to the repository rules"
    )
    request("POST", f"/repos/{repo}/statuses/{head_sha}", token, {
        "state": "failure" if blocking else "success",
        "context": STATUS_CONTEXT,
        "description": description[:140],
        "target_url": run_url,
    })

    print(f"posted verdict: {len(blocking)} blocking, {len(warnings)} warning(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
