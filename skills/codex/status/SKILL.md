---
name: status
description: "Show a lightweight mid-session Git status, recent commits, and staged and unstaged change summaries without changing files or updating history."
---

# Status

Give a lightweight mid-session Git check without changing files or reading the full history.
Follow already applicable project instructions.

If Git is available and this is a repository, inspect:

```text
git status --short --branch
git log --oneline -5
git diff --stat
git diff --cached --stat
```

Report the branch, whether the worktree is clean, and concise summaries of staged and unstaged
changes. Label them separately. If the folder is nested inside another repository, identify the
enclosing repository. If no commits exist, say so. Uncommitted changes can belong to another agent;
do not stage, discard or claim them.

If Git is unavailable or this is not a repository, say so and briefly list the current project
folder's contents using the available file tools. Do not initialise Git, fetch, commit or push.

Do not prompt to commit merely because the tree is dirty. The student can request a checkpoint or
invoke `$close-session` separately if installed.

**Inspect and adapt:** this is deliberately a quick Git view. Use `$start-session` for the
shared project-history handoff if that skill is installed.
