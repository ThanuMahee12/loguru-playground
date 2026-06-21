---
name: Hotfix
about: Critical production issue requiring immediate attention
title: '[HOTFIX] '
labels: 'hotfix, critical, priority-high'
assignees: ''
---

# 🚨 HOTFIX Pull Request

## Incident Overview

**Severity Level:**
- [ ] 🔴 Critical - Complete outage or data loss
- [ ] 🟠 High - Major functionality broken
- [ ] 🟡 Medium - Important feature impaired

**Issue Summary:**
<!-- Brief description of the production issue -->

**Incident Ticket:** #

<details>
<summary>📊 Impact Details</summary>

**Users Affected:**

**Systems Affected:**

**Business Impact:**

**Detected:** YYYY-MM-DD HH:MM UTC

**Reported by:**

</details>

<details>
<summary>🔍 Root Cause</summary>

### Problem Description
<!-- Detailed explanation of what went wrong -->

### Root Cause Analysis
<!-- Why did this happen? -->

</details>

<details>
<summary>🔧 Fix Description</summary>

### Solution
<!-- What is being fixed? -->

### Changes Made
<!-- Specific code changes -->

-
-
-

### Files Modified

-
-

</details>

<details>
<summary>✅ Validation</summary>

### Testing Performed

- [ ] Fix tested in development
- [ ] Fix tested in staging/pre-prod
- [ ] Manual smoke testing completed
- [ ] Automated tests passing
- [ ] Regression testing completed

### Test Results
<!-- Provide evidence that the fix works -->

### Verification Steps
<!-- How to verify the fix works in production -->

1.
2.
3.

**Expected Outcome:**

</details>

<details>
<summary>🚀 Deployment</summary>

### Deployment Urgency
- [ ] Deploy immediately
- [ ] Deploy within 1 hour
- [ ] Deploy within 4 hours
- [ ] Schedule deployment

### Deployment Plan

1.
2.
3.

### Database Changes
- [ ] No database changes
- [ ] Schema changes required
- [ ] Data migration required

### Rollback Plan

**Rollback Steps:**
1.
2.
3.

### Monitoring

**Metrics to watch:**
-
-

**Alert thresholds:**
-
-

</details>

<details>
<summary>⚠️ Risk Assessment</summary>

### Risk Level
- [ ] Low risk - Isolated change
- [ ] Medium risk - Multiple components affected
- [ ] High risk - Core functionality changed

### Potential Side Effects

-
-

### Mitigation Strategy

</details>

<details>
<summary>📢 Communication</summary>

### Stakeholders Notified
- [ ] Engineering team
- [ ] Product team
- [ ] Support team
- [ ] Customers/users (if applicable)

### Status Update Plan

### Post-Deployment Communication

</details>

<details>
<summary>✔️ Hotfix Checklist</summary>

### Pre-Deployment

- [ ] Issue fully understood and root cause identified
- [ ] Fix verified in non-production environment
- [ ] All relevant tests passing
- [ ] Code review completed (or justification for skip)
- [ ] Deployment plan documented
- [ ] Rollback plan documented
- [ ] Stakeholders notified
- [ ] Monitoring plan in place

### Deployment

- [ ] Backup created (if applicable)
- [ ] Deployment executed according to plan
- [ ] Fix verified in production
- [ ] Monitoring confirms stability
- [ ] No new errors introduced

### Post-Deployment

- [ ] Issue resolved and verified
- [ ] Monitoring shows normal operation
- [ ] Stakeholders notified of resolution
- [ ] Post-mortem scheduled
- [ ] Documentation updated

</details>

<details>
<summary>🔗 Related Items</summary>

Fixes #
Related incident #

</details>

<details>
<summary>📝 Additional Context</summary>

### Why Skip Normal Process?
<!-- Justify why this is a hotfix vs. normal PR -->

### Long-term Solution

- [ ] This is the permanent fix
- [ ] Follow-up ticket needed for permanent solution

**Follow-up ticket:** #

</details>

---

<details>
<summary>👥 Emergency Approvals</summary>

**Required Approvals:**
- [ ] Engineering Lead
- [ ] On-call Engineer
- [ ] Product/Business (if customer-facing)

**Approved by:**

</details>

---

**⚠️ HOTFIX GUIDELINES:**
- Hotfixes should be minimal, focused changes
- Skip hotfix process only for true production emergencies
- Schedule post-mortem to prevent recurrence
- Create follow-up tickets for technical debt
