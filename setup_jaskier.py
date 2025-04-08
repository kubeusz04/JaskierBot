import re

bot_file = "JaskierBot 1.0.py"

def replace_in_file(token, client_id):
    with open(bot_file, "r", encoding="utf-8") as f:
        code = f.read()

    # Zamień token
    code = re.sub(r'bot\.run\(["\'].*?["\']\)', f'bot.run("{token}")', code)

    # Zamień client_id w ydl_opts
    code = re.sub(
        r"client_id': \['(.*?)'\]",
        f"client_id': ['{client_id}']",
        code
    )

    with open(bot_file, "w", encoding="utf-8") as f:
        f.write(code)

    print("✅ Token i client_id zostały zaktualizowane w pliku bota.")

if __name__ == "__main__":
    print("🔧 Konfigurator JaskierBota")
    token = input("🔑 Wklej swój Discord BOT TOKEN: ").strip()
    client_id = input("🎧 Wklej SoundCloud client_id: ").strip()

    if token and client_id:
        replace_in_file(token, client_id)
    else:
        print("❌ Token lub client_id nie zostały podane. Anulowano.")
