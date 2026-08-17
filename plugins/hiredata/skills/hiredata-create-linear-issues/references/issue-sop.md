# HireData Linear issue SOP

This reference captures the maintained team workflow as of 2026-08-15. Treat the live Notion pages as authoritative when accessible:

- [Reporting an Issue to Linear](https://www.notion.so/27900d8748688063b797cc454553c12d)
- [Processing an Issue within Linear](https://www.notion.so/29c00d87486880aa8df1c4d68d467e11)
- [How Linear Statuses Work](https://www.notion.so/2dc00d874868809ca942d7f0382d29e4)
- [Linear Issues Templates](https://www.notion.so/2ab00d874868809ba444ffafe01eded2)

## Access model

The skill is intentionally HireData-specific and may be installed by HireData team members, customers, and partners. Access is controlled by the connected systems, not by removing useful workflow knowledge from the skill:

- HireData team members use the internal Notion SOPs and live Linear workspace available to their account.
- Approved partners use the HireData project and Notion pages that have been shared with them. For example, a partner contributing to a joint RMA project may follow the shared project's issue-management rules.
- Users without live access can still produce a complete report from the bundled references, but must mark live metadata, duplicate checks, and policy freshness as unverified.

Never expose or request credentials, tokens, unrelated personal data, or pages the user is not authorized to access. Installing the skill grants no additional Notion, Linear, customer, or project permissions.

## When to create an issue

Create an issue for:

- a reproducible bug requiring development;
- a client request requiring technical assessment or development;
- a product or UX improvement with clear user value.

Before creating:

- search Linear for duplicates and related work;
- gather screenshots, recordings, URLs, environment details, customer context, and source links;
- prefer updating an existing issue when it already represents the same outcome.

## Minimum description

Use the matching template, but ensure the issue answers:

- **Title:** short and descriptive.
- **Summary:** what the issue/request is and why it matters.
- **Current behaviour:** what happens now.
- **Expected behaviour:** the intended observable outcome.
- **Steps to reproduce:** required for bugs when reproducible.

Write neutrally and factually. Use screenshots or videos when they materially clarify the issue.

## Required metadata before entering a cycle

| Field | Team rule |
|---|---|
| Status | Default new intake to Triage unless instructed otherwise |
| Priority | Use the approved prioritization matrix when the user is authorized to apply it; otherwise describe impact and leave the HireData priority unset. If genuinely unsure and the SOP permits, use Medium and flag it |
| Assignee | Leave empty unless the owner is known |
| Project | Select the relevant project, such as Core, Forms, Mail, Messaging, or Carerix RMA |
| Label | Select the applicable approved label, such as Bug, Feature, Improvement, Data, or Question. Use multiple labels only when each adds distinct routing or reporting value |
| Cycle | Leave empty unless instructed |
| Links | Add relevant automation, run, event, account, prototype, recording, or page links |
| Customer request | Connect the customer and link the original Intercom/Discord/other source |

## Review and submit

Before submission:

1. Check that title, description, evidence, metadata, and links are complete for the issue's maturity.
2. Check related and potentially duplicate issues.
3. Do not promote an issue beyond its honest readiness level.

After submission:

- every new issue starts in **Triage**;
- Desi reviews Triage, with Tim as fallback when Desi is absent;
- if materially incomplete, leave it in Triage and tag the reporter for missing information; do not rewrite substantive requirements on the reporter's behalf;
- if it is a duplicate, close the duplicate, comment with the original issue, and notify the reporter;
- add new facts to the issue or comments rather than leaving them only in chat;
- move approved work according to urgency and planning workflow:
  - Urgent: current cycle, assign a developer, and notify them;
  - High: Ready to Plan;
  - Medium: Ready to Plan when capacity warrants it;
  - Low: Ready to Plan or Backlog;
- verify delivered work on production before notifying a customer or partner.
