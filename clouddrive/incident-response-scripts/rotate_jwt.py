import os
import secrets
import subprocess

# Dynamically resolve paths so the script can be executed from anywhere
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CLOUDDRIVE_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
ENV_PATH = os.path.join(CLOUDDRIVE_DIR, ".env")

def main():
    print("[*] Initiating Emergency JWT Rotation...")
    
    # 1. Generate new key
    new_key = secrets.token_hex(32)
    print(f"[*] Generated new 64-character secure JWT key.")

    # 2. Read .env and replace
    if not os.path.exists(ENV_PATH):
        print(f"[!] Error: {ENV_PATH} not found.")
        return

    with open(ENV_PATH, "r") as f:
        lines = f.readlines()

    with open(ENV_PATH, "w") as f:
        for line in lines:
            if line.startswith("JWT_SECRET_KEY="):
                f.write(f"JWT_SECRET_KEY={new_key}\n")
            else:
                f.write(line)
    print("[*] Successfully injected new key into .env file.")

    # 3. Restart Docker containers
    print("[*] Recreating backend container to load new key into memory...")
    subprocess.run(["docker", "compose", "up", "-d", "backend"], cwd=CLOUDDRIVE_DIR, check=True)

    print("[*] Restarting Nginx to clear DNS cache...")
    subprocess.run(["docker", "compose", "restart", "nginx"], cwd=CLOUDDRIVE_DIR, check=True)

    print("[+] Emergency Rotation Complete. All existing user sessions have been invalidated globally.")

if __name__ == "__main__":
    main()
