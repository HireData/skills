#!/usr/bin/env python3
"""Validate the HireData plugin, skills, and eval coverage without dependencies."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
PLUGIN_DIR = ROOT / "plugins" / "hiredata"
SKILLS_DIR = PLUGIN_DIR / "skills"
NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
SEMVER_PATTERN = re.compile(r"^\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?$")
LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


class Validator:
    def __init__(self) -> None:
        self.errors: list[str] = []

    def fail(self, message: str) -> None:
        self.errors.append(message)

    def load_json(self, path: Path) -> object:
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            self.fail(f"{path.relative_to(ROOT)}: {exc}")
            return {}

    def require_url(self, value: object, label: str) -> None:
        if not isinstance(value, str):
            self.fail(f"{label} must be an HTTPS URL")
            return
        parsed = urlparse(value)
        if parsed.scheme != "https" or not parsed.netloc:
            self.fail(f"{label} must be an HTTPS URL")

    def validate_manifest(self) -> None:
        manifest_path = PLUGIN_DIR / ".codex-plugin" / "plugin.json"
        manifest = self.load_json(manifest_path)
        if not isinstance(manifest, dict):
            self.fail("plugin.json must contain an object")
            return

        required = ["name", "version", "description", "author", "homepage", "repository", "license", "skills", "mcpServers", "interface"]
        for field in required:
            if not manifest.get(field):
                self.fail(f"plugin.json is missing {field}")

        if manifest.get("name") != "hiredata":
            self.fail("plugin.json name must be hiredata")
        if not SEMVER_PATTERN.fullmatch(str(manifest.get("version", ""))):
            self.fail("plugin.json version must be semantic versioning")
        if manifest.get("repository") != "https://github.com/HireData/skills":
            self.fail("plugin.json repository must point to HireData/skills")
        if manifest.get("license") != "Apache-2.0":
            self.fail("plugin.json license must be Apache-2.0")
        if manifest.get("skills") != "./skills/":
            self.fail("plugin.json skills must be ./skills/")

        for field in ("homepage", "repository"):
            self.require_url(manifest.get(field), f"plugin.json {field}")

        author = manifest.get("author", {})
        if not isinstance(author, dict):
            self.fail("plugin.json author must be an object")
        else:
            for field in ("name", "email", "url"):
                if not author.get(field):
                    self.fail(f"plugin.json author.{field} is required")
            self.require_url(author.get("url"), "plugin.json author.url")

        servers = manifest.get("mcpServers", {})
        server = servers.get("hiredata", {}) if isinstance(servers, dict) else {}
        if server.get("type") != "http" or server.get("url") != "https://api.hiredata.com/mcp":
            self.fail("plugin.json must configure the official HireData HTTP MCP endpoint")

        interface = manifest.get("interface", {})
        required_interface = [
            "displayName",
            "shortDescription",
            "longDescription",
            "developerName",
            "category",
            "capabilities",
            "websiteURL",
            "privacyPolicyURL",
            "termsOfServiceURL",
            "supportURL",
            "defaultPrompt",
        ]
        if not isinstance(interface, dict):
            self.fail("plugin.json interface must be an object")
        else:
            for field in required_interface:
                if not interface.get(field):
                    self.fail(f"plugin.json interface.{field} is required")
            for field in ("websiteURL", "privacyPolicyURL", "termsOfServiceURL", "supportURL"):
                self.require_url(interface.get(field), f"plugin.json interface.{field}")

    def parse_frontmatter(self, path: Path) -> dict[str, str]:
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except OSError as exc:
            self.fail(f"{path.relative_to(ROOT)}: {exc}")
            return {}
        if not lines or lines[0] != "---":
            self.fail(f"{path.relative_to(ROOT)} must start with YAML frontmatter")
            return {}
        try:
            end = lines.index("---", 1)
        except ValueError:
            self.fail(f"{path.relative_to(ROOT)} has unclosed YAML frontmatter")
            return {}

        fields: dict[str, str] = {}
        for line in lines[1:end]:
            if not line.strip():
                continue
            if ":" not in line:
                self.fail(f"{path.relative_to(ROOT)} has unsupported frontmatter: {line}")
                continue
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip()
        if set(fields) != {"name", "description"}:
            self.fail(f"{path.relative_to(ROOT)} frontmatter must contain only name and description")
        return fields

    def validate_skills(self) -> set[str]:
        if not SKILLS_DIR.is_dir():
            self.fail("plugins/hiredata/skills is missing")
            return set()

        names: set[str] = set()
        for skill_dir in sorted(path for path in SKILLS_DIR.iterdir() if path.is_dir()):
            skill_file = skill_dir / "SKILL.md"
            agent_file = skill_dir / "agents" / "openai.yaml"
            if not skill_file.is_file():
                self.fail(f"{skill_dir.relative_to(ROOT)} is missing SKILL.md")
                continue
            if not agent_file.is_file():
                self.fail(f"{skill_dir.relative_to(ROOT)} is missing agents/openai.yaml")

            fields = self.parse_frontmatter(skill_file)
            name = fields.get("name", "")
            description = fields.get("description", "")
            if name != skill_dir.name:
                self.fail(f"{skill_file.relative_to(ROOT)} name must match its directory")
            if not NAME_PATTERN.fullmatch(name):
                self.fail(f"{skill_file.relative_to(ROOT)} has an invalid skill name")
            if len(description) < 40:
                self.fail(f"{skill_file.relative_to(ROOT)} description is too short")
            if name in names:
                self.fail(f"duplicate skill name: {name}")
            names.add(name)

            text = skill_file.read_text(encoding="utf-8")
            for target in LINK_PATTERN.findall(text):
                if "://" in target or target.startswith("#"):
                    continue
                linked = (skill_dir / target.split("#", 1)[0]).resolve()
                if not linked.is_file():
                    self.fail(f"{skill_file.relative_to(ROOT)} links to missing file {target}")

        if len(names) < 5:
            self.fail("the plugin must contain at least five skills")
        return names

    def validate_marketplace(self) -> None:
        path = ROOT / ".agents" / "plugins" / "marketplace.json"
        marketplace = self.load_json(path)
        plugins = marketplace.get("plugins", []) if isinstance(marketplace, dict) else []
        hiredata = next((item for item in plugins if item.get("name") == "hiredata"), None)
        if not hiredata:
            self.fail("marketplace.json must list the hiredata plugin")
            return
        source = hiredata.get("source", {})
        relative = source.get("path")
        if source.get("source") != "local" or not isinstance(relative, str):
            self.fail("marketplace hiredata source must be a local path")
            return
        resolved = (ROOT / relative).resolve()
        if resolved != PLUGIN_DIR.resolve():
            self.fail("marketplace hiredata path must resolve to plugins/hiredata")

    def validate_claude_manifests(self) -> None:
        """Validate the Claude plugin manifests and their parity with the Codex ones."""
        codex_manifest = self.load_json(PLUGIN_DIR / ".codex-plugin" / "plugin.json")
        if not isinstance(codex_manifest, dict):
            codex_manifest = {}

        plugin_path = PLUGIN_DIR / ".claude-plugin" / "plugin.json"
        if not plugin_path.is_file():
            self.fail("plugins/hiredata/.claude-plugin/plugin.json is missing")
            return
        plugin = self.load_json(plugin_path)
        if not isinstance(plugin, dict):
            self.fail("Claude plugin.json must contain an object")
            return

        for field in ("name", "version", "description", "author", "homepage", "repository", "license", "mcpServers"):
            if not plugin.get(field):
                self.fail(f"Claude plugin.json is missing {field}")
        if not SEMVER_PATTERN.fullmatch(str(plugin.get("version", ""))):
            self.fail("Claude plugin.json version must be semantic versioning")

        servers = plugin.get("mcpServers", {})
        server = servers.get("hiredata", {}) if isinstance(servers, dict) else {}
        if server.get("type") != "http" or server.get("url") != "https://api.hiredata.com/mcp":
            self.fail("Claude plugin.json must configure the official HireData HTTP MCP endpoint")

        # Parity: the two host manifests must describe the same plugin release.
        for field in ("name", "version", "description", "repository", "license", "keywords"):
            if plugin.get(field) != codex_manifest.get(field):
                self.fail(f"Claude and Codex plugin.json disagree on {field}")
        if plugin.get("mcpServers") != codex_manifest.get("mcpServers"):
            self.fail("Claude and Codex plugin.json disagree on mcpServers")

        marketplace_path = ROOT / ".claude-plugin" / "marketplace.json"
        if not marketplace_path.is_file():
            self.fail(".claude-plugin/marketplace.json is missing")
            return
        marketplace = self.load_json(marketplace_path)
        if not isinstance(marketplace, dict):
            self.fail("Claude marketplace.json must contain an object")
            return
        if marketplace.get("name") != "hiredata-skills":
            self.fail("Claude marketplace.json name must be hiredata-skills")
        owner = marketplace.get("owner", {})
        if not isinstance(owner, dict) or not owner.get("name"):
            self.fail("Claude marketplace.json owner.name is required")

        plugins = marketplace.get("plugins", [])
        entry = next((item for item in plugins if isinstance(item, dict) and item.get("name") == "hiredata"), None)
        if not entry:
            self.fail("Claude marketplace.json must list the hiredata plugin")
            return
        source = entry.get("source")
        if not isinstance(source, str):
            self.fail("Claude marketplace hiredata source must be a relative path string")
        elif (ROOT / source).resolve() != PLUGIN_DIR.resolve():
            self.fail("Claude marketplace hiredata source must resolve to plugins/hiredata")
        if entry.get("version") != plugin.get("version"):
            self.fail("Claude marketplace entry version must match Claude plugin.json version")

    def validate_evals(self, skill_names: set[str]) -> None:
        submission = self.load_json(ROOT / "evals" / "submission-cases.json")
        if not isinstance(submission, dict):
            self.fail("submission-cases.json must contain an object")
        else:
            positive = submission.get("positive", [])
            negative = submission.get("negative", [])
            if len(positive) != 5 or len(negative) != 3:
                self.fail("submission-cases.json must contain exactly 5 positive and 3 negative cases")
            ids = [case.get("id") for case in positive + negative]
            if len(ids) != len(set(ids)):
                self.fail("submission-cases.json case IDs must be unique")
            for case in positive:
                if case.get("skill") not in skill_names:
                    self.fail(f"submission case {case.get('id')} references an unknown skill")

        regression = self.load_json(ROOT / "evals" / "regression-cases.json")
        cases = regression.get("cases", []) if isinstance(regression, dict) else []
        ids = [case.get("id") for case in cases]
        if len(ids) != len(set(ids)):
            self.fail("regression-cases.json case IDs must be unique")
        expected_kinds = {"normal", "ambiguous", "safety"}
        for name in sorted(skill_names):
            kinds = {case.get("kind") for case in cases if case.get("skill") == name}
            missing = expected_kinds - kinds
            if missing:
                self.fail(f"{name} is missing regression kinds: {', '.join(sorted(missing))}")
        for case in cases:
            if case.get("skill") not in skill_names:
                self.fail(f"regression case {case.get('id')} references an unknown skill")
            if case.get("kind") not in expected_kinds:
                self.fail(f"regression case {case.get('id')} has an invalid kind")
            for field in ("prompt", "must", "must_not"):
                if not case.get(field):
                    self.fail(f"regression case {case.get('id')} is missing {field}")

    def run(self) -> int:
        self.validate_manifest()
        skill_names = self.validate_skills()
        self.validate_marketplace()
        self.validate_claude_manifests()
        self.validate_evals(skill_names)
        if self.errors:
            print("Validation failed:")
            for error in self.errors:
                print(f"- {error}")
            return 1
        print(f"Validation passed: {len(skill_names)} skills, Codex and Claude plugin metadata, marketplaces, and eval coverage.")
        return 0


if __name__ == "__main__":
    sys.exit(Validator().run())
