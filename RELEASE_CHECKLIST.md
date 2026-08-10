# Plugin release checklist

The repository follows the current OpenAI plugin layout (a required `.codex-plugin/plugin.json`, bundled skills under `skills/`, and an MCP server configuration that points to HireData's production HTTPS endpoint) and mirrors it for Claude (`.claude-plugin/plugin.json` in the plugin and `.claude-plugin/marketplace.json` at the repo root).

## Every release, both hosts

- Bump `version` identically in `plugins/hiredata/.codex-plugin/plugin.json`, `plugins/hiredata/.claude-plugin/plugin.json`, and the plugin entry in `.claude-plugin/marketplace.json`. Claude only delivers plugin updates when the version field changes.
- Run `python3 scripts/validate_repo.py`; it enforces manifest parity across hosts.

## Completed in the repository

- Plugin identity, semantic version, descriptions, developer, category, capabilities, starter prompts, and public policy URLs.
- Five focused skills with self-contained references.
- Production HireData MCP URL using remote HTTP and OAuth.
- Repo marketplace for local development and team testing.
- Installation instructions for the plugin and manual MCP connection.
- Exactly five positive and three negative submission cases.
- A larger regression suite and comparison rubric for ongoing skill changes.
- Structural validation for all five skills.
- Apache-2.0 license, repository URL, security policy, pull-request template, and automated GitHub validation.

## Required before public directory submission

- Register the MCP connection in ChatGPT developer mode and add an `.app.json` mapping if the submission flow requires the returned `plugin_asdk_app...` technical ID.
- Complete HireData domain verification and a current MCP tool scan.
- Ensure every MCP tool declares `readOnlyHint`, `openWorldHint`, and `destructiveHint`, with a justification for each value.
- Verify HireData's business/developer identity and complete policy attestations.
- Add a demo-recording URL covering the main skills and MCP tools.
- Add release notes and reviewer-ready OAuth demo access.
- Run every submission and regression case from fresh conversations after installation.
- Confirm starter prompts complete end to end on every supported surface.
- Add screenshots only if the MCP provides custom UI; follow OpenAI's current size and prompt-coverage requirements.

## Required before Claude organization-wide distribution

- Confirm a clean install from a fresh clone with `/plugin marketplace add HireData/skills` and `/plugin install hiredata@hiredata-skills` in Claude Code, including the OAuth flow and one end-to-end run per skill.
- Confirm the GitHub-synced marketplace flow in a Claude Team or Enterprise organization (Organization settings → Plugins) and that skills trigger in web chat and the desktop app.
- Inquire with Anthropic about listing in the curated marketplaces surfaced under "Browse Anthropic sources," the closest equivalent of the OpenAI public directory.

## Current validator compatibility note

The live OpenAI submission documentation requires `interface.supportURL` for MCP-backed plugins. The bundled local plugin validator available during initial scaffolding rejected that newly documented field, while all other fields passed. Keep `supportURL` for the current public spec and rerun the newest validator before submission.

## Sources to recheck before release

- [Anthropic: Create and distribute a plugin marketplace](https://code.claude.com/docs/en/plugin-marketplaces)
- [Anthropic: Manage plugins for your organization](https://support.claude.com/en/articles/13837433-manage-plugins-for-your-organization)
- [OpenAI: Package your plugin](https://developers.openai.com/plugins/build/plugins)
- [OpenAI: Build skills](https://developers.openai.com/plugins/build/skills)
- [OpenAI: Connect and test your plugin](https://developers.openai.com/plugins/deploy/connect-chatgpt)
- [OpenAI: Submission error reference](https://developers.openai.com/plugins/deploy/submission-errors)
- [HireData: Connect HireData to your AI assistant](https://help.hiredata.com/apps/mcp/connect-hiredata-to-your-ai-assistant)
