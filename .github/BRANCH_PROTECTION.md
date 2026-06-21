# Branch Protection Rules

Configure these rules in **Settings > Branches > Add branch protection rule** after creating a repo from this template.

## Main Branch (`main`)

**Branch name pattern:** `main`

### Protect matching branches

- [x] **Require a pull request before merging**
  - [x] Require approvals: `1` (or more for teams)
  - [x] Dismiss stale pull request approvals when new commits are pushed
  - [x] Require approval of the most recent reviewable push

- [x] **Require status checks to pass before merging**
  - [x] Require branches to be up to date before merging
  - Add required checks: (add your CI workflow names here)

- [x] **Require conversation resolution before merging**

- [x] **Do not allow bypassing the above settings**

### Rules applied to everyone including administrators

- [ ] Allow force pushes (keep disabled)
- [ ] Allow deletions (keep disabled)

---

## Dev Branch (`dev`)

**Branch name pattern:** `dev`

### Protect matching branches

- [x] **Require a pull request before merging**
  - [x] Require approvals: `1`

- [ ] Require status checks (optional, less strict than main)

- [x] **Require conversation resolution before merging**

---

## Quick Setup via GitHub CLI

```bash
# Protect main branch
gh api repos/{owner}/{repo}/branches/main/protection -X PUT -f required_status_checks='{"strict":true,"contexts":[]}' -f enforce_admins=true -f required_pull_request_reviews='{"required_approving_review_count":1,"dismiss_stale_reviews":true}' -f restrictions=null

# Protect dev branch
gh api repos/{owner}/{repo}/branches/dev/protection -X PUT -f required_pull_request_reviews='{"required_approving_review_count":1}' -f restrictions=null
```

---

## Ruleset Alternative (Recommended for Organizations)

GitHub Rulesets provide more flexibility. Go to **Settings > Rules > Rulesets** to create repository rules that can:
- Apply to multiple branches with patterns
- Be inherited from organization level
- Include bypass permissions for specific roles
