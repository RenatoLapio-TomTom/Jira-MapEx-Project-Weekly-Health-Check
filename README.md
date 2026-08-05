# Jira MapEx Project Weekly Health Check

Automated weekly health check pipeline for the **MAPEX** Jira project.
Runs every Saturday, generates a Markdown report, and publishes it as a child page in a Confluence personal space.

---

## How it works

1. The GitHub Actions workflow (`.github/workflows/mapex-health-check.yml`) triggers every **Saturday at ~17:00 CET** (16:00 UTC; DST drift of ±1 h is acceptable).
2. The script (`scripts/mapex_health_check.py`) queries Jira for all MAPEX tickets created in the **last 90 days**, excluding tickets created by the configured list of Map Expert account IDs.
3. It produces a Markdown health report with four sections:
   - **Executive Summary** — scope, rejection rate, schedule health, top urgent tickets, overload flags, recommendations, RAG indicator.
   - **Rejected / Disputed Tickets** — tickets detected via rejection signals (incomplete resolution, reopening, dissatisfaction keywords, reporter post-closure comment).
   - **At-Risk / Late Tickets** — overdue, blocked, stale, due-soon, or unassigned tickets.
   - **Follow-up** — flagged tickets requiring assignee action.
4. The report is:
   - Saved locally in `reports/mapex-health-YYYY-MM-DD.md` and committed back to the repository.
   - Published as a **child page** under `CONFLUENCE_PARENT_PAGE_ID` in `CONFLUENCE_SPACE_KEY`.
5. Disputed ticket keys are persisted in `data/disputed_history.json` so they are **not re-reported** in future runs.

---

## Required GitHub Secrets

Add the following secrets under **Settings → Secrets and variables → Actions** in this repository:

| Secret | Description |
|--------|-------------|
| `JIRA_BASE_URL` | Jira instance URL, e.g. `https://tomtom.atlassian.net` |
| `JIRA_EMAIL` | Atlassian account email |
| `JIRA_API_TOKEN` | Atlassian API token (generate at https://id.atlassian.com/manage-profile/security/api-tokens) |
| `CONFLUENCE_BASE_URL` | Confluence URL, e.g. `https://tomtom.atlassian.net/wiki` |
| `CONFLUENCE_EMAIL` | Atlassian account email (usually same as `JIRA_EMAIL`) |
| `CONFLUENCE_API_TOKEN` | Atlassian API token (can be same as `JIRA_API_TOKEN`) |
| `CONFLUENCE_SPACE_KEY` | Confluence space key, e.g. `~lapio` for personal space |
| `CONFLUENCE_PARENT_PAGE_ID` | Numeric ID of the parent page under which reports will be created |

### Optional environment variables (set in workflow or script defaults)

| Variable | Default | Description |
|----------|---------|-------------|
| `JIRA_PROJECT_KEY` | `MAPEX` | Jira project key to analyze |
| `LOOKBACK_DAYS` | `90` | Number of days to look back for ticket creation |

---

## Files

```
.github/
  workflows/
    mapex-health-check.yml   # GitHub Actions workflow
config/
  excluded_reporters.txt     # Jira accountIds of Map Experts to exclude
data/
  disputed_history.json      # Persisted list of previously reported disputed ticket keys
reports/
  mapex-health-YYYY-MM-DD.md # Generated health reports (auto-committed each run)
scripts/
  mapex_health_check.py      # Main health check script
```

---

## Manual run

Trigger manually via **Actions → MAPEX Jira Weekly Health Check → Run workflow** in the GitHub UI, or using the GitHub CLI:

```bash
gh workflow run mapex-health-check.yml
```

---

## Disputed ticket history

`data/disputed_history.json` contains all ticket keys ever reported in the _Rejected / Disputed Tickets_ section.
Tickets in this list are suppressed from future reports.
To reset history (e.g., to force re-reporting), clear the `reported_keys` array in that file and commit.
