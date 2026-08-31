# MCP form-editing gotchas

Behaviors to respect when editing forms through the MCP, especially published ones.

- Translation upserts replace the entire content map. Fetch the current translation, merge the change, and send the complete map back; a partial send silently deletes every other key. Never probe replace-versus-merge semantics on a production form.
- A field's evaluation configuration updates as one whole object: resend note, screening, scoring, and profiling together, or the omitted parts are cleared. Capability toggles merge per key.
- Form-level evaluation configuration (scoring bands, profiling skills, generated output fields) also replaces wholesale; include everything that should survive.
- Creating a form requires at least one generated output field, and labels and descriptions are length-capped. Keep welcome copy short and put long copy in the linked message template.
- Choice options and data-source bindings are mutually exclusive. When a question's answers mirror ATS data (language levels, stages, motives), bind the data source and have label fixes made in the ATS so every workspace stays in sync; reserve static options for values the form itself owns.
- Give inline data tokens a default filter so labels degrade gracefully when the referenced field is empty, and prefer switching the question off per vacancy as the real fix.
- A mandatory field cannot be excluded per record; leave fields non-mandatory when the design calls for per-vacancy toggling.
- Data references (job, match, candidate) are linked in the form editor, not through the MCP; confirm afterward that the keys saved, because tokens and per-record configurations depend on them.
