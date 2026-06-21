# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This is a Git/GitHub starter template repository containing essential configuration files for new projects. It provides:
- Standard GitHub workflow configuration (PR templates, auto-release)
- Editor configuration (.editorconfig)
- Semantic versioning with automated releases

## Key Scripts

**Manual version bumping:**
```bash
./scripts/bump-version.sh [major|minor|patch]  # defaults to patch
```

## Automated Workflows

- **Auto Release** (`.github/workflows/auto-release.yml`): Automatically creates a GitHub release on every push to main. First release starts at v0.0.0, subsequent releases increment the patch version. Generates release notes from commit messages.

## Code Style

Uses `.editorconfig` for consistent formatting:
- UTF-8 charset, LF line endings
- 2-space indentation (except: Python uses 4 spaces, Go/Makefile use tabs)
- CRLF for Windows batch/PowerShell files

## Branch Conventions

- Production branch: `main` (triggers auto-release)
- Development branch: `dev`
- Feature branches: `feature/your-feature-name` (branch from `dev`)
- PR templates available for: feature, bugfix, hotfix, advanced changes
- Branch protection rules: see `.github/BRANCH_PROTECTION.md` for setup guide
