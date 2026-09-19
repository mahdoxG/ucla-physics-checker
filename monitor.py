import os
import time
import requests
from playwright.sync_api import sync_playwright

TARGET_CLASSES = [
    {
        "name": "Physics 5A - Section 003",
        "url": "https://sa.ucla.edu/ro/Public/SOC/Results/ClassDetail?term_cd=26F&subj_area_cd=PHYSICS&crs_catlg_no=0005A%20%20%20&class_id=318025220&class_no=%20003%20%20"
    },
    {
        "name": "Physics 5A - Section 004",
        "url": "https://sa.ucla.edu/ro/Public/SOC/Results/ClassDetail?term_cd=26F&subj_area_cd=PHYSICS&crs_catlg_no=0005A%20%20%20&class_id=318025230&class_no=%20004%20%20"
    }
]

DISCORD_WEBHOOK_URL = os.environ.get("DISCORD_WEBHOOK")

def check_ucla_classes():
    open_spots = []
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        for item in TARGET_CLASSES:
            try:
                page.goto(item["url"], wait_until="networkidle")
                text = page.inner_text("body")
                
                if "Open" in text and "Closed" not in text and "Full" not in text:
                    open_spots.append(item)
            except Exception as e:
                print(f"Error checking {item['name']}: {e}")
                
        browser.close()
        
    return open_spots
    
    if __name__ == "__main__":
    # --- TEST MODE: FORCING A FAKE ALERT ---
    spots = [{"name": "TEST RUN - Physics 5A", "url": "https://sa.ucla.edu"}]
    
    # (Leave the rest of the script as is)
    if spots:
        for spot in spots:
            message = f"🚨 **UCLA PHYSICS SPOT OPEN:** {spot['name']}\nRegister now: {spot['url']}"
            print(message)
            if DISCORD_WEBHOOK_URL:
                requests.post(DISCORD_WEBHOOK_URL, json={"content": message})

"""if __name__ == "__main__":
    # Runs 4 checks spaced 60 seconds apart per GitHub Actions execution
    CHECKS_PER_RUN = 4
    DELAY_SECONDS = 60

    for i in range(CHECKS_PER_RUN):
        print(f"Check {i+1} of {CHECKS_PER_RUN}...")
        spots = check_ucla_classes()
        
        if spots:
            for spot in spots:
                message = f"🚨 **UCLA PHYSICS SPOT OPEN:** {spot['name']}\nRegister now: {spot['url']}"
                print(message)
                if DISCORD_WEBHOOK_URL:
                    requests.post(DISCORD_WEBHOOK_URL, json={"content": message})
            break  # Exit immediately if a spot is found
            """
        print("All sections full.")
        if i < CHECKS_PER_RUN - 1:
            print(f"Waiting {DELAY_SECONDS} seconds before next check...\n")
            time.sleep(DELAY_SECONDS)
