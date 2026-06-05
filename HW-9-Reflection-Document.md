# HW9 Incident Reflection: Leaked JWT Secret

### 1. Were the steps in your runbook easy to follow and understand?
Yes, the steps were intentionally designed to be executed during a high-stress, Severity-1 security emergency. Instead of vague guidelines like "Rotate the secret," the runbook provided the exact terminal commands required to generate a cryptographically secure 64-character hex string (e.g., `python -c "import secrets..."`) and explicitly stated the exact Docker commands needed to reload the backend without bringing down the database. This eliminated guesswork and reduced the Time to Recover (TTR).

### 2. Can you simplify your runbook further?
The manual generation of the key and the manual editing of the `.env` file introduces room for human error (e.g., a typo while pasting). To prove this can be simplified, I actually wrote and implemented a custom automation script (`clouddrive/incident-response-scripts/rotate_jwt.py`). During a crisis, an SRE simply runs `python clouddrive/incident-response-scripts/rotate_jwt.py`, and the script automatically generates the key, safely injects it into the configuration, and triggers the Docker backend and Nginx restarts in one flawless, automated action.

### 3. Any steps in your runbook that should be automated further?
In an enterprise cloud environment, the entire concept of manually editing a local configuration file should be automated away. We should migrate the `JWT_SECRET_KEY` from a static `.env` file into a centralized enterprise vault (like HashiCorp Vault or AWS Secrets Manager). For a truly automated runbook, the CI/CD pipeline should automatically trigger a key rotation API call directly to the Vault upon detecting a leak, and redeploy the backend automatically, achieving a "Zero-Touch" recovery.

### 4. Any automated steps in your runbook that need manual supplementation?
The detection phase is highly automated using our custom-built GitHub Actions CI/CD scanner, which automatically halts the pipeline and throws a red alert if a regex pattern matching a secret is committed. However, this automated step strictly requires manual supplementation: an SRE must manually verify if the leaked string is the *actual* production key or just a harmless dummy string used in a testing file. If we fully automated the rotation based purely on the scanner, a developer committing a fake test key could accidentally trigger a global logout for millions of legitimate users.
