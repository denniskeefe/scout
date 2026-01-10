import requests
import json
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
                "Discord_Lookup": f"https://discord.com/users/{username}", # Requires user ID in reality, but often mirrored
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
                "ProductHunt": f"https://www.producthunt.com/@{username}",
                "Kaggle": f"https://www.kaggle.com/{username}"
            },
            "Alt-Tech/Decentralized": {
                "Bluesky": f"https://bsky.app/profile/{username}.bsky.social",
                "Mastodon": f"https://mastodon.social/@{username}",
                "Telegram_Chan": f"https://t.me/{username}",
                "Rumble": f"https://rumble.com/user/{username}",
                "Gab": f"https://gab.com/{username}",
                "Minds": f"https://www.minds.com/{username}"
            },
            "Web3/Finance": {
                "OpenSea": f"https://opensea.io/{username}",
                "Etherscan": f"https://etherscan.io/address/{username}", # Checks handle-mapping
                "CashApp": f"https://cash.app/${username}",
                "Venmo": f"https://venmo.com/u/{username}"
            }
        }

    def check_platforms(self):
        print(f"[*] Commencing Deep-Scan for: {self.username}")
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'}
        
        for category, sites in self.platforms.items():
            print(f"\n--- {category} ---")
            for platform, url in sites.items():
                self.results["summary"]["total_checked"] += 1
                try:
                    # Added 'allow_redirects=False' to detect 2026 "Profile Not Found" redirects
                    response = requests.get(url, headers=headers, timeout=5, allow_redirects=False)
                    
                    if response.status_code == 200:
                        self.results["platforms"][platform] = {"status": "Found", "url": url}
                        self.results["summary"]["found"] += 1
                        print(f"[+] {platform}: Profile detected.")
                    elif response.status_code == 302 or response.status_code == 301:
                        # Redirects often mean the profile doesn't exist on modern sites
                        self.results["platforms"][platform] = {"status": "Potential (Redirect)"}
                    else:
                        self.results["platforms"][platform] = {"status": "Not Found"}
                except Exception as e:
                    self.results["platforms"][platform] = {"status": "Error", "msg": "Timeout/Blocked"}

    def save_report(self):
        filename = f"deep_osint_{self.username}.json"
        with open(filename, 'w') as f:
            json.dump(self.results, f, indent=4)
        print(f"\n[*] Deep-Scan Complete. Total Hits: {self.results['summary']['found']}")

if __name__ == "__main__":
    target = input("Enter the username: ")
    scout = OSINTScout(target)
    scout.check_platforms()
    scout.save_report()
