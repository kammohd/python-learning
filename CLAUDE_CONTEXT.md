# Claude GitHub Training Context

Purpose
- Provide a concise, self-contained prompt/context file that Claude (Anthropic) or any assistant can use to continue the GitHub training session and run guided exercises against the local repo and remote.

Repository
- owner: kammohd
- repository: python-learning
- remote: origin -> https://github.com/kammohd/python-learning.git
- default branch: master

Workspace files of interest
- hello_world.py
- README_GIT.md
- git_tutorial.ps1

Current state
- Local branch: `master` (ahead 1 commit: d91e90e)
- Remote `origin/master` SHA: bf07b02

Guidance for the assistant (Claude)
- Goal: teach Git concepts through hands-on CLI and GUI steps. Be concise, actionable, and safe.
- Always show exact commands to run, wrapped in fenced code blocks, and explain expected results briefly.
- Before executing any destructive operation (reset --hard, force-push), ask for explicit confirmation.
- When interacting with the local repository, always verify status with `git status` and show diffs with `git diff` or `git log` as needed.

Primary exercises (use one-at-a-time)
1. Show status and tracked files
   - `git status -sb`
   - `git ls-files`
2. Compare local vs remote
   - `git fetch origin --prune`
   - `git log --oneline origin/master..master`
   - `git diff origin/master..master`
3. Create a feature branch, edit, commit, push
   - `git checkout -b feature/NAME`
   - edit `hello_world.py`
   - `git add hello_world.py`
   - `git commit -m "Message"`
   - `git push -u origin feature/NAME`
4. Merge and pull updates
   - create PR on remote or merge locally, then `git pull origin master`

Example assistant prompts (for reuse)
- "List files on origin/master and show their sizes."
- "Show commits that are on my local `master` but not on `origin/master`."
- "Create a branch, add a small change to `hello_world.py`, commit, and push; show commands only."

Safety and limits
- Do not automatically push or modify remote without user approval. If asked to push, confirm first.

Notes for the human learner
- Follow commands step-by-step; ask the assistant to explain any output you don't understand.
- Use VS Code Source Control as a visual complement to CLI commands.
