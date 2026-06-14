# Git Learning Guide

Goals
- Learn Git basics (commit, push, pull, branch, merge)
- Practice version control via CLI and VS Code Source Control
- Understand undoing changes, viewing history, and resolving conflicts

Prerequisites
- Git CLI installed and configured (user.name, user.email)
- A remote repo connected (you mentioned you already have one)

Quick CLI Cheatsheet
- `git status` — show working tree status
- `git add <file>` — stage changes
- `git commit -m "msg"` — record staged changes
- `git push` — push commits to remote
- `git pull` — fetch + merge from remote
- `git branch` / `git checkout -b <name>` — create/switch branches
- `git merge <branch>` — merge another branch into current
- `git log --oneline --graph --all` — view history
- `git diff` — see unstaged changes

Exercises (CLI)
1. Check status: `git status`
2. Create a feature branch: `git checkout -b feature/your-name`
3. Make a small edit in `hello_world.py`, stage and commit it:
   - `git add hello_world.py`
   - `git commit -m "Add greeting personalization"`
4. Push your branch: `git push -u origin feature/your-name`
5. Open a Pull Request on the remote (GitHub/GitLab web UI)
6. Merge the PR and `git pull` the default branch locally

Exercises (GUI — VS Code)
1. Open the Source Control view (Ctrl+Shift+G)
2. You will see changed files; enter a commit message and click ✓ to commit
3. Use the branch picker in the bottom-left to create/switch branches
4. Click the ••• menu for more actions (pull, push, fetch, sync)

Undoing and Recovery
- `git restore <file>` — discard unstaged changes
- `git restore --staged <file>` — unstage
- `git reset --hard <commit>` — hard reset (careful)
- `git revert <commit>` — safe way to undo a commit by creating a new commit

Further reading
- Pro Git book: https://git-scm.com/book/en/v2
- GitHub Docs: https://docs.github.com/en

If you want, I can run through these exercises interactively and create a sample branch/commit for you.
