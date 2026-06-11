\# Compliance



\- Goals: align CloudDrive with basic industry expectations (inspired by SOC 2 and OWASP ASVS).

\- Access control:

&#x20; - Authenticated access with JWT.

&#x20; - Authorization checks on file and folder ownership.

\- Logging and monitoring:

&#x20; - Application logs shipped via Promtail to Loki.

&#x20; - Grafana dashboards used to observe login failures, errors, and activity trends.

\- Secrets management:

&#x20; - Credentials provided via environment variables.

&#x20; - Support for AWS Secrets Manager in production to rotate sensitive values.

\- Incident response:

&#x20; - Documented runbook for handling leaked JWT secrets and other high-severity issues.

&#x20; - Post-incident review feeds back into threat model and security tests.

