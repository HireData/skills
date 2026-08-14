---
name: hiredata-diagnose-automations
description: Diagnose why a HireData automation did not do what someone expected, and propose a safe repair. Use when runs are cancelled, failed, timed out or skipped, when an email or WhatsApp message never arrived, when a trigger appears not to fire, or when someone pastes a run error and asks what it means.
---

# Diagnose HireData automations

Explain what actually happened to a workflow before changing anything.

Most reports of a "broken" automation are one of five different situations with different fixes. Separate them first.

| Situation | Where the evidence is |
|---|---|
| The trigger never produced an event | `events` |
| Events arrived but runs stopped early | `runs`, then `run_steps` |
| A step errored | `run_steps` |
| The message was sent but not delivered or not read | `emails`, `messages` |
| Everything worked and the expectation was wrong | the trigger blueprint and the user story |

## Workflow

1. Establish the claim: which automation, which workspace, which recipient or record, what the person expected, and over what period. Ask only for what you cannot look up.
2. Inspect before concluding. Call `queryStatistics (operation: capabilities)` for the sources you intend to use, then read [references/diagnostic-queries.md](references/diagnostic-queries.md) for the query shape and its non-obvious constraints.
3. Walk the ladder in order — intake, run outcome, step reason, channel outcome, configuration. Stop as soon as the evidence explains the claim; do not run every query by reflex.
4. Read [references/failure-patterns.md](references/failure-patterns.md) to interpret the reason you found. Confirm the current vocabulary from live capabilities rather than assuming the reference is complete.
5. Separate expected cancellation from defect. A large share of cancelled runs is normal in healthy workspaces, because a run that does not match a filter or a path is cancelled rather than failed. Never report a cancellation rate as a fault on its own.
6. State the diagnosis as: what happened, the evidence that shows it, how many records it affected, whether it is still happening, and what remains unexplained.
7. Propose a repair with its trade-off. Show the exact change, and what it will and will not fix.
8. Apply nothing without approval of that exact change. Re-read the trigger, template or form after any approved change and confirm the saved state.

## Guardrails

- Report a zero as a zero. If a source is partial, pruned or gated, say which one and why the answer is incomplete instead of filling the gap.
- Never infer a reason that no source returned. If the run-level message is empty and no step explains it, say the reason is not recorded and name the next place a human should look.
- Do not treat `cancelled` as an error, `skipped` as a failure, or a single failed run as an outage.
- Diagnose in the workspace the person named. Do not compare against, or disclose, another workspace's data.
- Record identifiers appear in run messages. Quote them only back to someone entitled to that workspace, and anonymize them in any shared write-up.
- Changing, pausing, activating or replaying anything is a consequential action. Preview it and require explicit approval, even when the fix looks obvious and even while diagnosing.
- Re-running or replaying past events can re-send real messages to real candidates. Establish the blast radius and get approval that names it before proposing a replay.
- If the MCP is unavailable, return the diagnostic plan and the exact queries to run, and state clearly that nothing was verified.
