# Finn-bot - Automation of Finn.no jobs to Discord

A Python-based automation tool that monitors **Finn.no** for new job listings and delivers instant notifications to a Discord channel via Webhooks.

## 🌟 Key Features
* **Real-time Monitoring**: Automatically scans search results at set intervals.
* **Discord Integration**: Formats and sends job links directly to your Discord server.
* **Smart Filtering**: Tracks seen jobs via a JSON database to prevent duplicate alerts.
* **Security First**: Uses Environment Variables (\`.env\`) to protect sensitive Webhook URLs.

## 🛠 Tech Stack
* **Language**: Python 3.x.
* **Libraries**: \`requests\`, \`beautifulsoup4\`, \`python-dotenv\`.
* **Infrastructure**: Fully Dockerized and ready for cloud deployment (e.g., Fly.io).

---
*Developed by C Strand*" > README.md
