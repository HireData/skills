I couldn't create the issue because Linear isn't connected here, so this is a draft to paste or file. I haven't checked for duplicates or the live SOP and matrix, and the cached policy files are dated 2026-08-15.

## Issue draft

**Title:** Scans: Empty Runs Finish as Successful and Replace Valid Results

**Body**

Four scans from 27 October retrieved 0 records but finished with a successful status. Their reports show placeholder findings instead of real results. One of them now hides an older valid scan for the same workspace, so the workspace's latest report no longer shows its real data.

**Current behaviour**

- **Status:** four scans from 27 October retrieved 0 records and still ended as successful.
- **Reports:** their reports show placeholder findings, as if data had been found.
- **Latest scan:** for one workspace, the empty scan is now the latest one and hides an older scan that holds valid data.

**Expected behaviour**

- **Status:** a scan that retrieved 0 records because of an error does not finish as successful.
- **Reports:** a failed or empty scan produces no placeholder findings.
- **Latest scan:** an empty or failed scan does not replace or hide an earlier valid scan.

The cause is not known yet. It could be an expired connection or a timeout during retrieval. Either way, the scan should not finish as successful.

**Properties**

| Property | Value |
|---|---|
| Status | Triage |
| Label | Bug |
| Priority | High (proposed, see reasoning below) |
| Project | Not set, because I couldn't verify the live project list |
| Assignee, cycle, estimate | Empty |

**Resources to attach:** the four scan links and the affected workspace, plus the older valid scan that is now hidden. Please add the run and record IDs in a comment, not in the body.

**Comment threads to open (one question each)**

1. Is the cause an expired connection or a timeout? Check the connection status and the timeout logs for the four scans.
2. Which workspace has the hidden valid scan, and can the older scan be restored as the latest before tomorrow's report?
3. Do the other three scans also hide earlier valid results?
4. Have other scans after 27 October ended with 0 records and a successful status?
5. Do the reports already sent or queued for the partner contain placeholder findings?

**Priority comment**

> Proposed High: reports with placeholder findings are materially impaired, and the application is still usable. The reports go to a partner tomorrow, 2026-11-04, which is the time sensitivity, but a deadline alone is not a matrix criterion.
>
> This could rise to Urgent in two cases. The first is if the cause is an expired connection and other workspaces are affected (the matrix covers app-connection failure and widespread failed runs). The second is if the partner counts as a key partner under the matrix. I couldn't verify partner status, so the Triage owner should confirm it.
>
> Written by Claude Sonnet 5.5 on behalf of [requester]

## Flagged as unverified

- Duplicates and related issues were not searched.
- The project, label names and priority policy come from the cached snapshot, not the live Notion pages.
- Linear will only link the issue to its customer request, source conversation and scan links once it is filed, so add those then.

If you connect Linear, I can search for duplicates, set the project and file this after you approve the draft.
