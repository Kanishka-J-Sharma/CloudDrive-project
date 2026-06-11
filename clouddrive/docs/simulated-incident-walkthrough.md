\# Simulated Incident Walkthrough



Scenario: Leaked JWT secret key allowing attackers to forge tokens.



\- 02:00 – Uptime Kuma shows elevated error rate and login anomalies.

\- 02:05 – Grafana dashboard shows spikes in failed logins and unusual access patterns.

\- 02:10 – Engineer reviews logs and discovers tokens signed with an unexpected key.

\- 02:15 – Investigation reveals a JWT secret accidentally committed and pushed in a branch.

\- 02:20 – Team rotates the JWT secret, redeploys the backend, and forces users to re-authenticate.

\- 02:30 – Logs confirm that old tokens are rejected with 401 and normal usage resumes.

\- 03:00 – Team updates the threat model, security testing plan, and compliance notes.

\- Outcome:

&#x20; - Runbook was followed for detection, response, and recovery.

&#x20; - The incident is now documented as a prepared scenario for training and future reviews.

