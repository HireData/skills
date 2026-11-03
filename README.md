# HireData Skills

Open-source skills that teach AI agents how to design, create, test, and improve recruitment automations and write actionable issue reports for HireData. The skills are agent-neutral; the repository packages them as an installable plugin for both OpenAI hosts (ChatGPT, Codex) and Anthropic hosts (Claude Code, Claude Team/Enterprise plugin catalogs), while keeping the HireData MCP server implementation independent.

HireData's MCP supplies live product capabilities and workspace data. These skills supply the domain judgment and repeatable workflows needed to use those capabilities well. They must not duplicate or freeze MCP schemas when the MCP can provide them.

## Skill families

Skill names carry the architecture. The verb after `hiredata-` says which family a skill belongs to, and every family has one job:

| Family | Job | Examples |
|---|---|---|
| `hiredata-map-*` | Foundation knowledge an agent needs before acting: actors, objects, stages, timing. | `hiredata-map-staffing-lifecycle` |
| `hiredata-build-<slug>` | One per use case: a guided intake plus construction of that use case's automation, forms and messages. The `<slug>` is the use case's canonical slug from `catalog/use-cases.json`. | `hiredata-build-prescreening` |
| `hiredata-create-*` | The primitives build skills compose: triggers, forms, email templates, WhatsApp templates. | `hiredata-create-forms` |
| `hiredata-diagnose-*`, `hiredata-test-*`, `hiredata-report-*` | Operate what is live: find out why it misbehaved, check it before activation, report what it delivered. | `hiredata-diagnose-automations` |
| `hiredata-plan-*`, `hiredata-convert-*` | The sales and partner motion: turn a problem or a scan into a plan, a conversation or a proposal. | `hiredata-convert-scan-results` |
| other verbs | Internal workflows such as issue reporting. | `hiredata-create-linear-issues` |

## The use-case catalog

`catalog/use-cases.json` holds one row per use case, keyed by a **slug** that is shared by every surface that talks about the use case: the public website (`/examples/<slug>`), the library, the scan skill's finding-to-use-case mapping, and the build skill. A row records the website page, the build skill, the HireData template IDs that implement it, the scan findings that point at it, the walkthrough video, the self-service intake and the library item. Null means not available yet; the catalog never guesses.

A complete use case is a **kit**: a video (how it works), a build skill (an assistant configures it) and an intake (the customer configures it). The catalog is where a kit's three parts are linked, and `scripts/validate_repo.py` enforces that every `hiredata-build-<slug>` skill has a catalog row.

### One skill per use case, one reference per ATS

A use case is the same job in every ATS; what differs is the wiring: field names, trigger events, match stages, template IDs. So there is **one build skill per use case** and, inside it, **one reference file per ATS** (`references/carerix.md`, later `references/bullhorn.md`). The skill's `SKILL.md` carries the ATS-independent workflow and routes to the reference for the ATS named in the request or found in the workspace. Videos are recorded per ATS and linked from the catalog's `ats` entries, not stored in the repository. An ATS name never appears in a skill name. Split a use case into separate skills only when an ATS's procedure diverges so far that the shared `SKILL.md` stops being readable.

## Seed skills

- `hiredata-plan-activation`: turn a client problem into a prioritized activation plan.
- `hiredata-create-triggers`: design and safely create automation triggers.
- `hiredata-create-forms`: design and safely create recruitment forms.
- `hiredata-create-email-templates`: design and safely create recruitment emails.
- `hiredata-create-whatsapp-templates`: design and safely create WhatsApp templates.
- `hiredata-diagnose-automations`: explain why a workflow did not do what was expected, then propose a safe repair.
- `hiredata-diagnose-email-performance`: explain why open, click, or delivery rates fell, and turn it into advice a customer can act on.
- `hiredata-map-staffing-lifecycle`: apply staffing and ATS domain knowledge (actors, objects, stages, timing) to interpret a request before acting.
- `hiredata-create-linear-issues`: turn evidence, requests, prototypes, and technical notes into actionable HireData issue reports.
- `hiredata-report-automation-roi`: report what live automations actually delivered, over the period they have genuinely been running.
- `hiredata-test-forms-and-emails`: audit a form or email template against normal, missing, and invalid inputs before activation.
- `designing-interfaces`: design new interfaces or redesign existing ones toward simple, user-friendly results, with the reasoning behind each change.

The first five are distilled from HireData's pre-MCP project prompts. Treat them as a tested starting point, then validate consequential behavior against a non-production HireData workspace before relying on them operationally.

## Repository structure

```text
plugins/hiredata/          Plugin package (Codex and Claude manifests)
plugins/hiredata/skills/   Installable, self-contained skills, named by family
catalog/use-cases.json     One row per use case: slug, website, build skill, templates, scan findings, intake, library, per-ATS reference and video
.agents/plugins/           Repo marketplace for ChatGPT and Codex
.claude-plugin/            Repo marketplace for Claude
evals/                     Stable behavioral regression cases and rubric
scripts/validate_repo.py   Dependency-free structural and eval validation
CONTRIBUTING.md            Contribution and quality requirements
INSTALL.md                 Plugin and MCP connection instructions
```

The two host manifests (`plugins/hiredata/.codex-plugin/plugin.json` and `plugins/hiredata/.claude-plugin/plugin.json`) describe the same plugin release; `scripts/validate_repo.py` enforces their parity.

## Principles

1. Solve a concrete user problem rather than documenting a feature.
2. Use the HireData MCP as the source of truth for current schemas, objects, fields, and workspace state.
3. Inspect before proposing, preview before mutating, and verify after mutating.
4. Keep skills client-neutral; do not depend on one AI product's question or browser interface.
5. Put detailed, non-obvious knowledge in `references/` and keep `SKILL.md` concise.
6. Never include customer secrets, credentials, internal-only metrics, or unsupported legal and policy claims.
7. Require evidence that an update is at least as good as the version it replaces.

## Validate a contribution

Run the repository's dependency-free checks before opening a pull request:

```text
python3 scripts/validate_repo.py
```

The checks validate plugin metadata, skill structure, references, eval coverage, and the use-case catalog (valid slugs, website paths, and a catalog row for every build skill). They do not replace the fresh-context behavioral comparison described in [evals/RUBRIC.md](evals/RUBRIC.md).

## License and security

Released under the [Apache License 2.0](LICENSE). Report vulnerabilities privately using [SECURITY.md](SECURITY.md); do not open a public issue containing credentials, customer data, or an exploitable security problem.
