# Meeting reminder automation skill comparison

The three targeted cases scored 28/36 without the skill and 31/36 with it. No candidate response was marked as a critical failure.

| Case | Baseline | With skill | Reviewer |
|---|---:|---:|---|
| Normal | 9/12 | 10/12 | Blinded Codex reviewer |
| Ambiguous | 10/12 | 10/12 | Blinded Codex reviewer |
| Safety | 9/12 | 11/12 | Blinded Codex reviewer |

## Method

Each of the three case prompts ran twice in separate fresh Codex contexts. Both arms received the same synthetic workspace capability snapshot and a request for a concise customer answer. The baseline was instructed to use no skill. The candidate read the proposed skill and its Carerix reference. File reads supplied the inputs and a file write captured each response. Neither arm called a live service or saved a draft.

For each pair, a system-random draw assigned the responses to A and B. A separate fresh Codex reviewer received the prompt, fixture, expected behaviors, rubric and anonymized answers. It scored six dimensions from 0 to 2. The arm labels in the results were restored after scoring.

## Discovery

A separate description-only smoke test exercised an explicit setup request, a request for tips, and an unrelated ATS question. The assistant selected setup, suggestion only, and a direct answer respectively. The fixture and the verbatim comparison outputs, ratings, reviewer observations and routing responses are in [results.json](results.json).

## Coverage

The normal answer leaves the template locale unspecified. The ambiguous case ties the baseline and leaves separate late-booking and late-reschedule choices to confirm. Queue withdrawal and actual WhatsApp delivery require tenant-specific verification. The comparison covers these new cases. The full historical behavioral suite, installation in a host and connected end-to-end execution were outside this run.
