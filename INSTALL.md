# Install the HireData plugin and MCP

The repository packages reusable skills and points compatible plugin hosts at HireData's existing remote MCP server. It does not contain or deploy the MCP server itself.

## Requirements

- A HireData account with access to at least one workspace.
- An AI client that supports OpenAI plugins or remote MCP servers.
- A supported plan for custom MCP connections where the client requires one.

The official HireData MCP endpoint is:

```text
https://api.hiredata.com/mcp
```

It uses OAuth. Do not add an API token or commit credentials to this repository.

## Install the local plugin for development

This repository includes a repo marketplace at `.agents/plugins/marketplace.json` and the plugin at `plugins/hiredata`.

1. Clone `https://github.com/HireData/skills.git` and open it as a trusted project in the ChatGPT desktop app or Codex.
2. Restart the app so it discovers the repo marketplace.
3. Open Plugins and install **HireData** from **HireData Skills**.
4. Complete the HireData OAuth flow, select the permitted workspace or workspaces, review the requested permissions, and authorize.
5. Start a new conversation before testing changed skills.

For a marketplace stored outside the currently open project, add its repository root first:

```text
codex plugin marketplace add /absolute/path/to/skills
codex plugin add hiredata@hiredata-skills
```

## Connect HireData manually in ChatGPT

Use this path when installing the skills separately or when the plugin host does not import the bundled MCP configuration.

### ChatGPT desktop

1. Open **Settings → Plugins** under Integrations.
2. Open the **MCPs** tab and choose **+ Add server**.
3. Enter:
   - Name: `HireData`
   - Type: `Streamable HTTP`
   - URL: `https://api.hiredata.com/mcp`
4. Leave token and header fields empty and save.
5. On first use, sign in to HireData, select the allowed workspaces, review permissions, confirm the redirect, and authorize.

Custom MCP connections currently require a paid ChatGPT plan. On ChatGPT web, use **Settings → Connectors → Advanced**, enable Developer mode, and add a custom connector with the same URL.

### Claude

1. Open **Settings → Connectors**. In the desktop app, Connectors is under Customize.
2. Choose **Add → Add custom connector**.
3. Enter `https://api.hiredata.com/mcp` and add it.
4. Connect, sign in to HireData, select workspaces, review permissions, confirm the redirect, and authorize.
5. A sensible permission setup is to allow read-only tools automatically while keeping write and delete tools on approval.

### Codex manual fallback

If the plugin is unavailable, add the remote MCP server directly:

```text
codex mcp add hiredata --url https://api.hiredata.com/mcp
```

Then complete the OAuth login when prompted and start a new task so the tools and skills are loaded together.

## Security behavior

- The assistant receives only the workspace access selected during authorization.
- It operates with the same HireData permissions as the signed-in user.
- Requests are recorded in HireData's activity log.
- New MCP capabilities require reauthorization before access expands.
- Disconnect the connector in the AI client or revoke its grant in HireData settings.

For current screenshots, plan availability, troubleshooting, and client-specific steps, use the [official HireData MCP guide](https://help.hiredata.com/apps/mcp/connect-hiredata-to-your-ai-assistant).
