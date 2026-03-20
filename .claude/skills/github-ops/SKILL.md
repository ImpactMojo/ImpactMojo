---
name: github-ops
description: GitHub API operations — create PRs, manage issues, reviews, releases, and branch management using $GITHUB_PAT. Use when the user asks to create/merge PRs, open/close issues, manage labels/milestones, or interact with GitHub.
---

# GitHub Operations Skill

Perform GitHub API operations using `$GITHUB_PAT` for any repository the token has access to.

## Authentication

All API calls use:
```
Authorization: token $GITHUB_PAT
```

Base URL: `https://api.github.com`

## Capabilities

### Pull Requests
- Create PRs: `POST /repos/{owner}/{repo}/pulls`
- Merge PRs: `PUT /repos/{owner}/{repo}/pulls/{number}/merge`
- List/review PRs: `GET /repos/{owner}/{repo}/pulls`
- Add reviewers: `POST /repos/{owner}/{repo}/pulls/{number}/requested_reviewers`
- Comment on PRs: `POST /repos/{owner}/{repo}/issues/{number}/comments`

### Issues
- Create issues: `POST /repos/{owner}/{repo}/issues`
- Close issues: `PATCH /repos/{owner}/{repo}/issues/{number}` with `{"state": "closed"}`
- Label issues: `POST /repos/{owner}/{repo}/issues/{number}/labels`
- Assign issues: `POST /repos/{owner}/{repo}/issues/{number}/assignees`

### Releases
- Create release: `POST /repos/{owner}/{repo}/releases`
- List releases: `GET /repos/{owner}/{repo}/releases`

### Branch Management
- List branches: `GET /repos/{owner}/{repo}/branches`
- Delete branch: `DELETE /repos/{owner}/{repo}/git/refs/heads/{branch}`
- Branch protection: `PUT /repos/{owner}/{repo}/branches/{branch}/protection`

## Usage Pattern

Always use `curl` with the PAT:
```bash
curl -s -H "Authorization: token $GITHUB_PAT" \
  -H "Accept: application/vnd.github.v3+json" \
  https://api.github.com/repos/{owner}/{repo}/endpoint
```

For POST/PATCH/PUT, add `-X METHOD -d '{"key": "value"}'`.

## Best Practices
- Always check if a PR/issue exists before creating duplicates
- Include meaningful titles and descriptions
- Link PRs to issues with "Closes #N" in the body
- Never force-push to main/master
- Prefer the API over `gh` CLI for reliability in remote environments
