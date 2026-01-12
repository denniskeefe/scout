import requests
import json
import time
import random
from datetime import datetime

class OSINTScout:
    def __init__(self, username):
        self.username = username
        self.results = {
            "target": username,
            "timestamp": datetime.now().isoformat(),
            "summary": {"total_checked": 0, "found": 0},
            "platforms": {}
        }
        
        # 2026 Expanded Categorized Platforms
        self.platforms = {
            "Social/Mainstream": {
                "X": f"https://x.com/{username}",
                "Instagram": f"https://instagram.com/{username}",
                "Facebook": f"https://facebook.com/{username}",
                "Threads": f"https://www.threads.net/@{username}",
                "Reddit": f"https://www.reddit.com/user/{username}",
                "Pinterest": f"https://www.pinterest.com/{username}",
                "Snapchat": f"https://www.snapchat.com/add/{username}",
                "Linktree": f"https://linktr.ee/{username}"
            },
            "Gaming/Community": {
                "Twitch": f"https://www.twitch.tv/{username}",
                "Steam": f"https://steamcommunity.com/id/{username}",
                "Roblox": f"https://www.roblox.com/user.aspx?username={username}",
                "Xbox": f"https://www.xboxgamertag.com/search/{username}",
                "PlayStation": f"https://psnprofiles.com/{username}"
            },
            "Tech/Professional": {
                "GitHub": f"https://github.com/{username}",
                "StackOverflow": f"https://stackoverflow.com/users/story/{username}",
                "LinkedIn": f"https://www.linkedin.com/in/{username}",
                "Medium": f"https://medium.com/@{username}",
                "Kaggle": f"https://www.kaggle.com/{username}"
            },
            "Alt-Tech/Decentralized": {
                "Bluesky": f"https://bsky.app/profile/{username}.bsky.social",
                "Mastodon": f"https://mastodon.social/@{username}",
                "Telegram_Chan": f"https://t.me/{username}",
                "Rumble": f"https://rumble.com/user/{username}"
            }
        }

        # List of modern User-Agents to rotate
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0"
        ]

    def check_platforms(self):
        print(f"[*] Commencing Deep-Scan for: {self.username}")
        
        for category, sites in self.platforms.items():
            print(f"\n--- {category} ---")
            for platform, url in sites.items():
                self.results["summary"]["total_checked"] += 1
                
                # --- OPSEC: RANDOM DELAY ---
                # Human-like pause between 2.0 and 5.5 seconds
                delay = random.uniform(2.0, 5.5)
                time.sleep(delay)

                # --- OPSEC: HEADER ROTATION ---
                headers = {
                    'User-Agent': random.choice(self.user_agents),
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                    'Accept-Language': 'en-US,en;q=0.5',
                    'Referer': 'https://www.google.com/', # Spoofing the traffic source
                    'DNT': '1' # Do Not Track request
                }

                try:
                    # allow_redirects=False is key for detecting 'missing' pages that redirect to home
                    response = requests.get(url, headers=headers, timeout=10, allow_redirects=False)
                    
                    if response.status_code == 200:
                        self.results["platforms"][platform] = {"status": "Found", "url": url}
                        self.results["summary"]["found"] += 1
                        print(f"[+] {platform}: Profile detected.")
                    elif response.status_code in [301, 302]:
                        self.results["platforms"][platform] = {"status": "Potential (Redirect)"}
                        print(f"[?] {platform}: Redirected (Check manually).")
                    else:
                        self.results["platforms"][platform] = {"status": "Not Found"}
                        print(f"[-] {platform}: Not Found.")

                except Exception as e:
                    self.results["platforms"][platform] = {"status": "Error", "msg": str(e)}
                    print(f"[!] {platform}: Connection error/timeout.")

    def save_report(self):
        filename = f"osint_report_{self.username}.json"
        with open(filename, 'w') as f:
            json.dump(self.results, f, indent=4)
        print(f"\n[*] Scan Complete. Total Hits: {self.results['summary']['found']}")
        print(f"[*] Report saved to {filename}")

if __name__ == "__main__":
    target = input("Enter the target username: ").strip()
    if target:
        scout = OSINTScout(target)
        scout.check_platforms()
        scout.save_report()
    else:
        print("Invalid username.")
