# CloudDrive Security Incident Runbook

This runbook outlines the exact operational procedures for detecting, responding to, and recovering from critical security incidents. 

---

## Incident 01: Emergency Credential Rotation (JWT Compromise)

**Severity:** Sev-1 (Critical)
**Description:** The JSON Web Token (JWT) Secret Key has been exposed to an unauthorized party (e.g., leaked via GitHub, compromised server, or unauthorized access). Because CloudDrive uses stateless authentication, an exposed JWT Secret allows an attacker to mathematically forge valid authentication tokens for any user (including Administrators) without needing a password.

### Phase 1: Detection
1. Receive automated alert from CI/CD pipeline (e.g., GitHub Advanced Security Secret Scanning) or a report from a security researcher.
2. The alert will state: `CRITICAL SECURITY ALERT: High-entropy secret or password leaked in commit!`

### Phase 2: Response & Triage
1. SSH into the CloudDrive production server.
2. Run `cat .env` to inspect the production environment variables.
3. Compare the `JWT_SECRET_KEY` value in the server with the leaked value reported in the alert.
4. **Decision Gate:** If the keys match, the system is fundamentally compromised. Proceed to Phase 3 immediately to perform a global session invalidation.

### Phase 3: Recovery (The "Nuke and Pave" Rotation)

**Option A: Manual Rotation (Educational / Fallback)**
1. **Generate a new key:** Generate a cryptographically secure 64-character hex string. 
   *(Run this command in the terminal):*
   ```bash
   python -c "import secrets; print(secrets.token_hex(32))"
   ```
2. **Inject the new key:** Open the `.env` file using `nano clouddrive/.env`. Delete the compromised `JWT_SECRET_KEY` and paste the newly generated key. Save and exit.
3. **Deploy the fix:** Reload the backend container to inject the new key into the application's memory without bringing down the database or frontend.
   *(Run this command in the terminal):*
   ```bash
   docker compose up -d backend
   docker compose restart nginx
   ```

**Option B: Automated Enterprise Rotation (Recommended)**
To eliminate human error during a high-stress crisis, execute the custom automation script. This script automatically generates a new key, safely injects it into the `.env` file, and orchestrates the required Docker container reboots in under 3 seconds.
   *(Run this command from the root directory):*
   ```bash
   python clouddrive/incident-response-scripts/rotate_jwt.py
   ```

### Phase 4: Verification & Consequence Management
1. **Verify Global Logout:** Navigate to the CloudDrive web application. Attempt to refresh a page or perform an action while logged in. You should be instantly kicked back to the Login screen with a `401 Unauthorized` error. This confirms that all forged tokens and all legitimate user sessions globally have been successfully invalidated.
2. **Git History Scrubbing:** The compromised secret still exists in the GitHub commit history. The SRE team must execute a `git filter-repo` command to permanently rewrite the repository history and destroy the leaked string.
3. **Post-Mortem:** Draft an incident report documenting how the secret bypassed pre-commit hooks and leaked to a public repository.
