# Team assignment: teach AI how HireData work gets done

## The question

What recurring part of your work requires HireData, recruitment, staffing, or customer knowledge that you repeatedly have to explain, correct, or look up—and what skill would let another AI user perform that work reliably through HireData's MCP?

## Assignment

Create one new HireData skill or materially improve one of the five seed skills in this repository.

Your contribution must:

1. Start from an existing customer problem, user story, support question, implementation mistake, or recurring internal task.
2. State who has the problem, how often it occurs, and what improves if the skill succeeds.
3. Use the HireData MCP where possible instead of reproducing schemas or workspace data in the prompt.
4. Include at least three eval cases: normal, missing/ambiguous data, and unsafe or invalid input.
5. Compare the previous version or no-skill baseline with the proposed skill using the repository rubric.
6. Record a short video showing the problem, the skill, one eval, and what you learned.
7. Open a PR and post the result in `#friday-updates`.

Improving a seed skill counts when the PR demonstrates a real, measured improvement. Merely making the wording longer does not.

## Suggested ownership

### Callum — connect skills to high-impact client problems

Choose an existing problem or user story with meaningful reach or frequency. Either improve `hiredata-plan-activation` so it identifies and prioritizes that problem, or improve the relevant creation skill so it solves it end to end. In the same process, write the missing support article about AI variables and use at least one AI-variable case in the evals.

### Desi — teach AI to test HireData automations

Create `hiredata-test-templates`. Teach the AI to test emails, forms, WhatsApp messages, variables, branching, missing data, language, recipient context, and downstream behavior. Include recruitment-specific acceptance criteria and use the existing seed skills' outputs as fixtures.

### Tim — capture recruitment and staffing industry knowledge

Create `hiredata-apply-staffing-knowledge`. Focus on the knowledge Tim currently teaches others: the staffing lifecycle, ATS concepts and relationships, differences between candidate/client/recruiter journeys, high-volume moments, appropriate follow-ups, common anti-patterns, and the questions an experienced consultant asks. Keep it action-oriented rather than building an encyclopedia. Test it against real anonymized client situations and use it to improve at least one seed skill.

### Ian — lightweight technical quality gate

Given Ian's development workload, do not require a separate new skill. Ask him to review one PR for correct MCP usage, unsafe mutations, stale schema assumptions, and feasibility. If he sees a recurring technical failure, a small improvement to an existing skill counts as his contribution.

### Victor — establish the gold standard

Use `hiredata-create-triggers` as the first reference implementation. Run its baseline and candidate evals, tighten it based on the results, and use that PR to demonstrate the expected contribution format.

## Friday update format

- Problem or user story
- Skill created or improved
- What HireData knowledge it teaches
- Baseline versus new eval result
- One failure or surprise discovered
- Link to PR and video
