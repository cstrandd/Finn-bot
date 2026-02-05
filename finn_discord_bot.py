import time
import json
import os
import requests
from bs4 import BeautifulSoup

# KLISRA IN DIN NYA WEBHOOK-URL MELLAN CITATEN
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1445570625937735811/KozjAlycNc31U5kGnMmiGcFZS2Q1hlxoiVW2JmO0J5dMudcmsK0co36Az6RLfk9ZoqCZ"

SEARCHES = {
    "Offshore": "https://www.finn.no/job/search?q=offshore",
    "Onshore": "https://www.finn.no/job/search?q=onshore",
    "Rigger": "https://www.finn.no/job/search?q=rigger",
    "Flaggmann": "https://www.finn.no/job/search?q=flaggmann",
    "Mekaniker": "https://www.finn.no/job/search?q=mekaniker",
    "Signalgiver": "https://www.finn.no/job/search?q=signalgiver",
    "Truckfører": "https://www.finn.no/job/search?q=truckfører",
    "BES vakt": "https://www.finn.no/job/search?q=bes+vakt",
}

SEEN_FILE = "seen_jobs.json"


def load_seen():
    if os.path.exists(SEEN_FILE):
        with open(SEEN_FILE, "r", encoding="utf-8") as f:
            return set(json.load(f))
    return set()


def save_seen(seen):
    with open(SEEN_FILE, "w", encoding="utf-8") as f:
        json.dump(list(seen), f)


def fetch_jobs(name, url):
    print(f"Hämtar {name} från {url}")
    headers = {"User-Agent": "Mozilla/5.0 (job-notifier for personal use)"}
    resp = requests.get(url, headers=headers, timeout=15)
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "html.parser")
    jobs = []

    for a in soup.find_all("a", href=True):
        href = a["href"]
        if "/job/" in href:
            link = "https://www.finn.no" + href if href.startswith("/") else href
            title = a.get_text(strip=True)
            if title:
                jobs.append((title, link))

    unique = {}
    for title, link in jobs:
        unique[link] = title

    return [(t, l) for l, t in unique.items()]


def send_to_discord(search_name, title, url):
    content = f"🛠️ **{search_name}** – nytt jobb hittat!\n{title}\n{url}"
    data = {"content": content}
    resp = requests.post(DISCORD_WEBHOOK_URL, json=data, timeout=10)
    if resp.status_code >= 400:
        print(f"Fel vid skick till Discord: {resp.status_code} {resp.text}")


def main():
    seen = load_seen()
    print(f"Laddade {len(seen)} tidigare annonser.")

    while True:
        try:
            for name, url in SEARCHES.items():
                jobs = fetch_jobs(name, url)
                for title, link in jobs:
                    job_id = link
                    if job_id not in seen:
                        seen.add(job_id)
                        print(f"Skickar annons för {name}: {title}")
                        send_to_discord(name, title, link)

            save_seen(seen)

        except Exception as e:
            print("Fel i huvudloopen:", e)

        print("Väntar 600 sekunder...\n")
        time.sleep(600)


if __name__ == "__main__":
    main()
