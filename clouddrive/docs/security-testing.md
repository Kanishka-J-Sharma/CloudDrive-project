\# Security Testing



\- Unit and functional tests cover core flows: login, upload, download, and access control.

\- Security tests focus on:

&#x20; - Invalid or expired JWT tokens.

&#x20; - Accessing files that belong to another user.

&#x20; - Handling of missing or malformed input.

\- CI workflow runs pytest on every push and pull request.

\- Additional checks (if enabled):

&#x20; - Static analysis (e.g., Semgrep) for common web vulnerabilities.

&#x20; - Dependency scanning (pip-audit) for known vulnerable packages.

\- Manual checks:

&#x20; - Verify that rotating the JWT secret invalidates old tokens.

&#x20; - Try accessing resources without auth to confirm 401 responses.

