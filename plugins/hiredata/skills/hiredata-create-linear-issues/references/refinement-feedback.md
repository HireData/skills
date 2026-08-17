# Refinement lessons from engineering feedback

Use these lessons for complex features, especially when a prototype or customer mock is the primary source.

1. Make the issue understandable with the prototype removed. AI-generated prototypes can contain invented operators, lists, mappings, and technical constraints.
2. Separate deterministic rules from model-judged behaviour. They have different triggers, costs, failure modes, and tests.
3. State whether capabilities can be enabled together. This changes the data model and effort materially.
4. Expose product decisions that affect the data model without designing the schema on engineering's behalf.
5. Use a per-input/per-output configuration matrix when different field types behave differently.
6. Cover what happens after configuration: execution, stored output, result surfaces, statistics, automation fields, and regression.
7. Name required refactors that are part of delivering the feature.
8. Keep customer wiring—such as writing a result to a specific ATS field—in a verification case, not generic expected behaviour.
9. Verify real dependencies. Complementary work is not automatically a blocker.
10. Decide terminology before it becomes enum/API/schema naming.
11. Collect blocking questions during refinement. Do not force the developer to decode them after work starts.

The goal is not to eliminate refinement. The goal is to make refinement about decisions and trade-offs rather than reconstructing intent.
