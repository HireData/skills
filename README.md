# HireData Skills

Open-source skills that teach AI agents how to design, create, test, and improve recruitment automations with HireData. The repository packages them as an installable OpenAI plugin while keeping the HireData MCP server implementation independent.

HireData's MCP supplies live product capabilities and workspace data. These skills supply the domain judgment and repeatable workflows needed to use those capabilities well. They must not duplicate or freeze MCP schemas when the MCP can provide them.

## Seed skills

- `hiredata-plan-activation`: turn a client problem into a prioritized activation plan.
- `hiredata-create-triggers`: design and safely create automation triggers.
- `hiredata-create-forms`: design and safely create recruitment forms.
- `hiredata-create-email-templates`: design and safely create recruitment emails.
- `hiredata-create-whatsapp-templates`: design and safely create WhatsApp templates.

These are first versions distilled from HireData's pre-MCP project prompts. Treat them as a tested starting point, then validate consequential behavior against a non-production HireData workspace before relying on them operationally.

## Repository structure

```text
plugins/hiredata/          OpenAI plugin package and manifest
plugins/hiredata/skills/   Installable, self-contained skills
evals/                     Stable behavioral regression cases and rubric
scripts/validate_repo.py   Dependency-free structural and eval validation
CONTRIBUTING.md            Contribution and quality requirements
TEAM_ASSIGNMENT.md         Internal kickoff assignment
INSTALL.md                 Plugin and MCP connection instructions
```

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

The checks validate plugin metadata, skill structure, references, and eval coverage. They do not replace the fresh-context behavioral comparison described in [evals/RUBRIC.md](evals/RUBRIC.md).

## License and security

Released under the [Apache License 2.0](LICENSE). Report vulnerabilities privately using [SECURITY.md](SECURITY.md); do not open a public issue containing credentials, customer data, or an exploitable security problem.
