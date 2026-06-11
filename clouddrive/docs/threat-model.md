\# Threat Model



\- System: CloudDrive lets authenticated users upload, store, and download files via a Flask backend and Postgres/S3.

\- Assets: user data, file contents, database, S3 objects, JWT tokens, admin credentials, Grafana/Loki logs.

\- Trust boundaries: browser ↔ nginx ↔ backend ↔ db/S3; admin/engineer access to Grafana and CI/CD.

\- Key threats:

&#x20; - Stolen JWT secret allowing token forgery and account takeover.

&#x20; - IDOR (insecure direct object reference) to read other users' files.

&#x20; - SQL injection or misconfigured DB exposing data.

&#x20; - Leaked credentials in Git history or CI/CD.

&#x20; - Misconfigured S3 bucket allowing public read or write.

\- Mitigations:

&#x20; - JWT-based auth, rotated secrets, and 401 on invalid tokens.

&#x20; - Authorization checks on file/folder access.

&#x20; - Parameterized DB access via ORM.

&#x20; - Secret scanning in CI and use of env vars instead of hardcoding.

&#x20; - Centralized logging and Grafana dashboard to detect anomalies.

