# Refinement guide for complex issues

Use these checks when a prototype, customer mock, recording, or broad feature request is the primary source.

1. Make the issue understandable without opening the prototype.
2. Separate deterministic rules from model-judged behaviour because their triggers, costs, failure modes, and tests differ.
3. State whether capabilities can be enabled together, since this can change product boundaries and effort.
4. Expose product decisions that affect the data model without designing the schema on engineering's behalf.
5. Use an input/output configuration matrix when field types behave differently.
6. Cover what happens after configuration: execution, stored output, result surfaces, reporting, automation fields, and regression.
7. Name required refactors that materially affect delivery.
8. Keep customer-specific mappings in a verification case rather than generic expected behaviour.
9. Verify dependencies. Complementary work is not automatically a blocker.
10. Decide terminology before it becomes API or schema naming.
11. Collect blocking questions during refinement instead of forcing engineering to reconstruct them after work begins.

The goal is to make refinement about decisions and trade-offs rather than reconstructing intent.
