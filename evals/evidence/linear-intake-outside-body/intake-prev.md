I drafted the issue below. Nothing was created in Linear, since no workspace is connected. Duplicates, project, labels, relations and the current priority policy are unverified.

**Title:** Scans: Zero-Record Scans Finish as Successful With Placeholder Findings

**Description**

Four scans from 2026-10-27 retrieved 0 records but finished with a successful status. Their reports show placeholder findings instead of real results. One of these scans is now the latest for its workspace, so the report view shows it instead of an older scan with valid results. Reports are due to a partner on 2026-11-04, so these can reach the partner as wrong data.

**Current behaviour**

- **Status:** scans that retrieved 0 records end as successful.
- **Reports:** they show placeholder findings, which look like real results.
- **Latest scan:** one affected scan is the latest for its workspace and hides the older valid scan.

**Expected behaviour**

- **Status:** a scan that retrieves no records because of a failure does not finish as successful.
- **Reports:** a report never presents placeholder findings as results.
- **Latest scan:** an empty or failed scan does not replace an older valid scan as the one shown for the workspace.

**Cause (unknown)**

The cause is not established. Two hypotheses are open, and they point to different fixes:

- **Expired connection:** the data source connection expired or was revoked, and the scan did not treat the failed fetch as a failure.
- **Timeout:** the retrieval timed out, and the scan finished with an empty result.

In both cases the scan marks success despite retrieving nothing, so the bug may be in how success is decided. Investigation should answer:

- Do the four scans share a connection, data source or workspace?
- What do the connection state and the scan logs show around the retrieval step?
- Is a legitimately empty result distinguishable from a failed retrieval?

**Evidence and links**

- **Scans:** add the four scan links, and mark which one hides the older valid scan.
- **Workspace and partner:** add the workspace link and the partner name.
- **Reports:** add links or screenshots of the placeholder findings.
- **Source:** add the original request (Intercom or Discord), and link it through a customer request.

**Triage questions**

- Which workspace and partner are affected?
- Are scans from other days or workspaces affected? This determines whether the issue is widespread.
- Is the older valid scan still intact, or has it been overwritten?
- What is the workaround for tomorrow's partner reports, such as rerunning the scans or excluding them?

**Proposed metadata**

- **Status:** Triage.
- **Priority:** High, proposed.
  - **Basis:** an important partner workflow is materially impaired. The scans fail silently and produce misleading reports.
  - **Deadline:** the 2026-11-04 deadline is context only. The matrix says not to set priority from a deadline.
  - **Urgent:** if the partner counts as a key partner, the matrix classes it as Urgent. I can't verify that, so the Triage owner should confirm.
- **Label:** Bug.
- **Project:** unset, to be chosen by Triage.
- **Assignee and cycle:** empty.
- **Relations:** none checked.

Fill in the evidence links and the partner's key status before submitting. The Triage owner can then decide between High and Urgent.
