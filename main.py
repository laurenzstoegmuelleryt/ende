import os

print("📂 Aktuelles Verzeichnis:", os.getcwd())
print("📄 Dateien im aktuellen Ordner:", os.listdir("."))

if os.path.exists("yt_session.session"):
    print("✅ Session-Datei gefunden!")
else:
    print("❌ Session-Datei NICHT gefunden!")
from telethon import TelegramClient, events
import re
import os
import requests
import sys
import asyncio

# Umgebungsvariablen von Render
API_ID = int(os.environ["API_ID"])
API_HASH = os.environ["API_HASH"]
SESSION_NAME = os.environ.get("SESSION_NAME", "yt_session")
CHANNEL_USERNAME = os.environ["CHANNEL_USERNAME"]
MAKE_WEBHOOK_URL = os.environ["MAKE_WEBHOOK_URL"]

# Client erstellen
client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

# Regex für YouTube-Links
yt_pattern = re.compile(
    r"(https?:\/\/(?:www\.)?(?:youtube\.com\/watch\?v=|youtu\.be\/)[\w\-]+)"
)

@client.on(events.NewMessage(chats=CHANNEL_USERNAME))
async def handler(event):
    text = event.raw_text
    yt_links = yt_pattern.findall(text)
    if yt_links:
        payload = {"links": yt_links, "message": text}
        requests.post(MAKE_WEBHOOK_URL, json=payload)
        print(f"🚀 YT-Links gesendet: {yt_links}")

async def main():
    print("🚀 Bot startet...")

    running_on_render = os.environ.get("RENDER") is not None

    if running_on_render:
        await client.connect()
        if not await client.is_user_authorized():
            print("❌ Keine gültige Session-Datei gefunden! Bitte lokal einloggen und neu deployen.")
            sys.exit(1)
    else:
        # Lokal interaktiv einloggen
        await client.start()

    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())
