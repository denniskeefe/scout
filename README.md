#  OSINT Scout 3.0: High-Velocity Footprint Analysis

**OSINT Scout** is a lightweight, modular Python automation tool designed for 2026-era digital footprinting. It performs rapid, non-invasive "username stitching" across 30+ platforms including mainstream social media, decentralized Web3 networks, gaming communities, and professional hubs.

##  Features

* **Multi-Platform Scanning:** Checks 30+ sites across 5 distinct categories (Social, Tech, Web3, Gaming, Alt-Tech).
* **Automation Oversight:** Implements 2026-compliant headers and redirect-logic to distinguish between "live" profiles and "parked" pages.
* **Pattern Analysis Ready:** Generates a structured JSON report for easy ingestion into link-analysis tools like Maltego or Gephi.
* **Privacy-First:** Operates as a passive reconnaissance tool (it only reads publicly accessible status codes).

##  Installation (macOS)

1. **Clone or Save the Script:** Ensure `scout.py` is in your working directory.
2. **Install Dependencies:** Open Terminal and run:
```bash
pip3 install requests

```



##  Usage

Run the script from your terminal:

```bash
python3 scout.py

```

When prompted, enter the target username.

### Interpreting Results

* **[+] Found:** A profile exists and returned a successful `200 OK` status.
* **[?] Potential (Redirect):** The site redirected the request. This often occurs when a platform hides profiles behind a login wall or has "parked" the username.
* **[!] Error:** The request timed out or was blocked by 2026 anti-bot measures (e.g., Cloudflare Turnstile).

##  Report Structure

The tool generates a file named `deep_osint_[username].json`. This report includes:

* **Timestamp:** Precision tracking of when the scan occurred.
* **Summary:** Total counts of hits vs. misses.
* **Platform Map:** Direct URLs for all detected profiles.

##  Ethics & Compliance

This tool is intended for use by **Private Investigators**, **Cybersecurity Professionals**, and **Law Enforcement**.

* **Active vs. Passive:** This script performs **Passive OSINT**; it does not interact with the target or alert them to your presence.
* **Terms of Service:** Ensure your use of this tool complies with your local jurisdiction's laws and the specific Terms of Service of the platforms being scanned.

---

