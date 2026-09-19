Python
import os
import requests

DISCORD_WEBHOOK_URL = os.environ.get("DISCORD_WEBHOOK")

if __name__ == "__main__":
    print("Testing Discord Webhook...")
    
    message = "🚨 **UCLA PHYSICS SPOT OPEN:** TEST RUN - Physics 5A\nRegister now: https://sa.ucla.edu"
    
    if DISCORD_WEBHOOK_URL:
        response = requests.post(DISCORD_WEBHOOK_URL, json={"content": message})
        print(f"Discord request sent! Response status: {response.status_code}")
    else:
        print("ERROR: DISCORD_WEBHOOK secret not found in environment variables.")
