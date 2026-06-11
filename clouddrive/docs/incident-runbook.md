\# Incident Runbook (JWT Secret Leak)



\## Detection

\- Alerts from Grafana/Uptime Kuma when error rates or unauthorized access patterns spike.

\- Logs showing suspicious tokens or repeated 401/403 responses.

\- External report (e.g., security researcher) of a leaked JWT secret in code or CI logs.



\## Response

\- Immediately rotate the JWT secret and deploy new configuration.

\- Invalidate active sessions by enforcing re-login for all users.

\- Search logs to estimate which accounts and data may be affected.

\- Lock or monitor high-risk accounts that show suspicious behavior.

\- Communicate the incident and required actions to stakeholders.



\## Recovery

\- Verify that old tokens no longer work and new logins succeed.

\- Tighten secret handling in CI/CD (no secrets in code or logs).

\- Update threat model and security tests to cover this scenario.

\- Document a postmortem and track follow-up actions.

