<#
Git tutorial script (PowerShell). These are example commands you can run step-by-step.
Run one section at a time and read prompts before executing destructive commands.
#>

Write-Output "Current branch and status:"
git branch --show-current
git status

# 1. Configure (only if not set)
# git config --global user.name "Your Name"
# git config --global user.email you@example.com

# 2. Create and switch to a feature branch
# git checkout -b feature/your-name

# 3. Edit a file (open in editor), then stage and commit
# git add hello_world.py
# git commit -m "Add greeting personalization"

# 4. Push branch to remote
# git push -u origin feature/your-name

# 5. Update local default branch
# git checkout master
# git pull origin master

# Useful inspection commands
# git log --oneline --graph --decorate --all
# git diff HEAD~1..HEAD

# Undo examples (be careful)
# git restore hello_world.py            # discard unstaged changes
# git restore --staged hello_world.py   # unstage
# git revert <commit>                  # create a new commit that undoes

Write-Output "Done. Follow steps in README_GIT.md for guided exercises."
