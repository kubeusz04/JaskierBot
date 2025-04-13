# 🎸 JaskierBot – Bard Discorda

**JaskierBot** to nie tylko bot muzyczny – to pełnoprawny bard na Twoim serwerze Discord!  
Potrafi grać ballady z SoundClouda, komentować każdą komendę, a do tego organizuje interaktywne quizy i prowadzi ranking Twojej ekipy. 🎤🎶

---

## ✨ Główne funkcje

### 🎵 Muzyczny bard
- `/wejdz` – bot dołącza do kanału głosowego
- `/zagraj <nazwa>` – gra utwór z SoundClouda na podstawie frazy
- `/szukaj <nazwa>` – wyszukuje 5 utworów z SoundClouda, użytkownicy wybierają reakcją
- `/ballada` – gra specjalny utwór "Zapachniało powiewem jesieni"
- `/groszadaj` – odtwarza "Grosza daj Wiedźminowi"
- `/pauza`, `/wznowienie`, `/zatrzymaj`, `/wyjdz` – sterowanie muzyką

### 🧠 Quiz
- `/quiz` – bot wybiera losowe pytanie i każdego z użytkowników z kanału głosowego, wszyscy głosują reakcjami
- `/ranking` – pokazuje wyniki głosowań i punkty graczy

---
![Zrzut ekranu](https://github.com/kubeusz04/JaskierBot/blob/main/2.png?raw=true)
![Zrzut ekranu 2](https://github.com/kubeusz04/JaskierBot/blob/main/1.png?raw=true)

---

## ⚙️ Wymagania

- Python 3.10+
- `discord.py`
- `yt-dlp`
- `ffmpeg`
- `pynacl`

Zainstaluj zależności:
```bash
pip install -r requirements.txt
sudo apt install ffmpeg -y
```

---

## 🛠️ Konfiguracja

Uruchom setup_jaskier.py w tym samym folderze co JaskierBot 1.0.py
```bash
python3 setup_jaskier.py
```
---
## 🪙 Jak zdobyć Discord BOT TOKEN

🔐 Wejdź na Discord Developer Portal

Kliknij „New Application” → nazwij ją np. JaskierBot

Po utworzeniu:
Przejdź do zakładki Bot

Kliknij „Add Bot” → potwierdź

Kliknij „Reset Token” → potwierdź → skopiuj bot token

Wklej ten token podczas działania setup_jaskier.py lub ręcznie do bot.run("...")

---

## 🎧 Jak zdobyć SoundCloud client_id
SoundCloud oficjalnie nie udostępnia prostego sposobu, ale da się zdobyć działające client_id ze strony – to legalne i działa tylko do odczytu.

🧙‍♂️ Instrukcja:
Wejdź na SoundCloud: https://soundcloud.com/

Wciśnij F12, aby otworzyć narzędzia deweloperskie (DevTools)

Przejdź do zakładki „Network”

Wyszukaj dowolny utwór i kliknij, by go odtworzyć

W filtrze wpisz: client_id

Zobaczysz linki typu:

https://api-v2.soundcloud.com/media/soundcloud:tracks:XXXXXX/stream/hls?client_id=xxxxxxxxxxxxxxxxxxxx
Skopiuj to co jest za client_id= – to jest właśnie to, czego szukasz!

🔁 Ten identyfikator możesz teraz wkleić do setup_jaskier.py albo bezpośrednio do kodu.

---

