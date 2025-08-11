rom telethon import TelegramClient
import os
import asyncio

# === Pfad zur Session-Datei ermitteln ===
BASE_DIR = os.path.dirname(os.path.abspath(_file_))
session_path = os.path.join(BASE_DIR, "yt_session.session")

# === Deine Telegram API-Daten ===
api_id = 26887058       # <-- Deine API_ID hier eintragen
api_hash = "8f3e45ebdde3dc58cc4de8a405477c47"   # <-- Deinen API_HASH hier eintragen

# === Client mit absolutem Pfad erstellen ===
client = TelegramClient(session_path, api_id, api_hash)


async def main():
    # Verbindung starten (nutzt bestehende Session falls vorhanden)
    await client.start()
    print(f"✅ Session erfolgreich geladen: {session_path}")

    # Beispiel: Eigene User-Infos abrufen
    me = await client.get_me()
    print(f"👤 Eingeloggt als: {me.first_name} (ID: {me.id})")

    # Hier kannst du deine weitere Logik einfügen
    # await client.send_message("me", "Hallo von Render! 🚀")


if _name_ == "_main_":
    with client:
        client.loop.run_until_complete(main())
