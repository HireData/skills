# Worked example: HD-1692 and HD-1740

Use this real workspace pair to understand the separation between product specification and implementation:

- [HD-1692 — Form Evaluations](https://linear.app/hiredata/issue/HD-1692/form-evaluations): reusable product contract and V1 go-live boundary.
- [HD-1740 — Form Evaluation: Implement Backend and APIs](https://linear.app/hiredata/issue/HD-1740/form-evaluation-implement-backend-and-apis): engineering implementation and test record.

## What was wrong before refinement

HD-1692 originated from a customer prototype that presented one AI Evaluator, gate-style statuses, and a specific Carerix Match-stage write-back. Taken literally, that mixed four different concerns:

- reusable HireData evaluation behaviour;
- deterministic and model-judged execution;
- one customer's configured ATS mapping;
- UI choices and operators that the prototype could not authoritatively define.

It also left the post-builder path—execution, storage, response presentation, automation fields, regression, and failure handling—insufficiently specified. Engineering therefore had to reconstruct product boundaries and data-model decisions before implementation.

## Why HD-1692 is the product specification

The refined issue defines the reusable outcome:

- Criteria, Scoring, Skills, Generated fields, and Summary are independently configurable and may coexist;
- predetermined and AI-judged behaviour have explicit timing and failure boundaries;
- outputs are stored with the response and exposed to supported consumers;
- customer ATS values remain mapping/configuration rather than HireData terminology;
- the RSPT prototype is a validation case, not the product contract;
- broader result UX, Carerix tabs, MCP, and human review are explicitly deferred.

Its acceptance criteria stay outcome-level. It does not invent migrations, class names, or schema decisions.

## Why HD-1740 is the implementation issue

HD-1740 links the product contract and records the engineering detail available from the actual implementation and pull requests:

- affected models, DTOs, resources, actions, jobs, and services;
- persistence and execution contracts;
- Summary/WhatsApp compatibility work;
- implementation checklist and test matrix;
- technical decisions still requiring confirmation.

This pairing lets product refine the intended behaviour without pretending to design the code, while letting engineering review and maintain the implementation plan without decoding the prototype.
