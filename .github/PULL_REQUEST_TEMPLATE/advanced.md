---
name: Advanced Pull Request
about: Comprehensive pull request template for complex changes
title: '[TYPE] '
labels: ''
assignees: ''
---

# Pull Request

## Summary

<!-- Provide a comprehensive summary of the changes -->

## Type of Change

**Select all that apply:**

- [ ] 🐛 Bug fix (non-breaking change which fixes an issue)
- [ ] ✨ New feature (non-breaking change which adds functionality)
- [ ] 💥 Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] 📝 Documentation update
- [ ] 🔨 Refactoring (no functional changes)
- [ ] ⚡ Performance improvement
- [ ] 🎨 UI/UX improvement
- [ ] 🔧 Configuration change
- [ ] 🧪 Test update
- [ ] 🔒 Security fix

<details>
<summary>📋 Detailed Changes</summary>

### Technical Details
<!-- Provide a detailed description of the changes -->

### Components Modified
<!-- List the main components/modules affected -->

-
-
-

### Architecture Impact
<!-- Describe any architectural changes or impacts -->

</details>

<details>
<summary>💾 Database Changes</summary>

- [ ] No database changes
- [ ] Schema changes (migrations included)
- [ ] Data migrations required
- [ ] Seeds/fixtures updated

<!-- Describe any database schema changes, migrations, or data updates -->

</details>

<details>
<summary>🌐 API Changes</summary>

- [ ] No API changes
- [ ] New endpoints added
- [ ] Existing endpoints modified
- [ ] Endpoints deprecated/removed
- [ ] API documentation updated

<!-- Describe any API changes -->

</details>

<details>
<summary>🧪 Testing</summary>

### Test Coverage

- [ ] Unit tests added/updated
- [ ] Integration tests added/updated
- [ ] E2E tests added/updated
- [ ] Manual testing completed
- [ ] Performance testing completed
- [ ] Security testing completed

### Test Results

```
# Paste test output here
```

### Testing Instructions

1.
2.
3.

</details>

<details>
<summary>✅ Code Quality</summary>

### Quality Checklist

- [ ] Code follows project style guidelines and conventions
- [ ] Self-review of code completed
- [ ] Code is DRY (Don't Repeat Yourself)
- [ ] Functions/methods are focused and single-purpose
- [ ] Complex logic is properly commented
- [ ] No commented-out code or debug statements
- [ ] Error handling is comprehensive
- [ ] Logging is appropriate and meaningful
- [ ] Code is performant and optimized

### Static Analysis

- [ ] Linter passes with no errors
- [ ] Type checking passes (if applicable)
- [ ] Security scan completed
- [ ] No new technical debt introduced

</details>

<details>
<summary>📚 Documentation</summary>

- [ ] Code comments added/updated
- [ ] README updated
- [ ] API documentation updated
- [ ] User documentation updated
- [ ] CHANGELOG updated
- [ ] Architecture diagrams updated (if applicable)

</details>

<details>
<summary>📦 Dependencies</summary>

### New Dependencies

- [ ] No new dependencies
- Dependencies added:
  -
  -

### Dependency Updates

- [ ] No dependency updates
- Dependencies updated:
  -
  -

### Security Considerations
<!-- Note any security implications of dependency changes -->

</details>

<details>
<summary>🚀 Deployment</summary>

### Deployment Checklist

- [ ] Environment variables documented
- [ ] Configuration changes documented
- [ ] Migration strategy documented
- [ ] Rollback plan documented
- [ ] Deployment notes added

### Environment Impact

- [ ] Development
- [ ] Staging
- [ ] Production

### Pre-deployment Requirements

1.
2.

### Post-deployment Tasks

1.
2.

</details>

<details>
<summary>⚡ Performance Impact</summary>

### Performance Considerations

- [ ] No performance impact expected
- [ ] Performance improved
- [ ] Potential performance impact (explained below)

### Benchmarks

```
# Paste benchmark results here
```

</details>

<details>
<summary>🔒 Security</summary>

### Security Checklist

- [ ] No security implications
- [ ] Input validation implemented
- [ ] Output encoding implemented
- [ ] Authentication/authorization handled correctly
- [ ] Sensitive data properly protected
- [ ] SQL injection prevention verified
- [ ] XSS prevention verified
- [ ] CSRF protection verified

### Security Concerns
<!-- Note any security concerns or considerations -->

</details>

<details>
<summary>🔄 Backwards Compatibility</summary>

- [ ] Fully backwards compatible
- [ ] Backwards compatible with migration path
- [ ] Breaking changes (documented below)

### Breaking Changes
<!-- Detail any breaking changes and migration steps -->

</details>

<details>
<summary>🔗 Related Items</summary>

### Issues

Closes #
Relates to #
Depends on #

### Pull Requests

Depends on PR #
Blocks PR #

</details>

<details>
<summary>📸 Screenshots / Videos</summary>

### Before
<!-- Add screenshots/videos showing previous behavior -->

### After
<!-- Add screenshots/videos showing new behavior -->

</details>

<details>
<summary>👀 Reviewer Notes</summary>

### Review Focus Areas
<!-- Highlight specific areas that need careful review -->

-
-

### Known Limitations
<!-- Note any known limitations or future improvements -->

-
-

</details>

<details>
<summary>✔️ Final Checklist</summary>

### Pre-Review

- [ ] Branch is up to date with base branch
- [ ] All commits are clean and well-formatted
- [ ] Commit messages follow conventions
- [ ] No merge conflicts
- [ ] CI/CD pipeline passes
- [ ] All automated tests pass

### Ready for Merge

- [ ] Approved by required reviewers
- [ ] All review comments addressed
- [ ] Final testing completed
- [ ] Documentation reviewed
- [ ] Ready for deployment

</details>

---

<details>
<summary>📝 Additional Notes</summary>

<!-- Any additional context or notes for reviewers -->

</details>
