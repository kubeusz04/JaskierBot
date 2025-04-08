# 🎸 JaskierBot – Bard Discorda

**JaskierBot** to muzyczny bot Discord inspirowany słynnym bardem z "Wiedźmina". Serwuje ballady i pieśni prosto z SoundClouda, komentując wszystko w jego typowym stylu – z humorem, charyzmą i lekkim dramatyzmem 🎤🎶

---

## ✨ Funkcje
- 🎧 **Odtwarzanie utworów z SoundCloud** (po nazwie lub bezpośrednim linku)
- 🔍 **Wyszukiwanie 5 utworów z SoundCloud** i wybór jednego przez reakcje emoji
- 📜 **Popisowe komendy** jak `/ballada` czy `/groszadaj`, odtwarzające konkretne pieśni
- ⏯️ **Sterowanie odtwarzaniem** – pauza, wznowienie, stop, wyjście z kanału
- 🗣️ **Stylizowane wypowiedzi Jaskiera** – każda komenda opatrzona klimatycznym komentarzem

---

## ⚙️ Technologie
- `discord.py` – obsługa bota
- `yt_dlp` – pobieranie i przetwarzanie linków SoundCloud
- `ffmpeg` – przetwarzanie audio
- Python 3.10+

---

## 🧙 Jak uruchomić

1. Zainstaluj zależności:
   ```bash
   pip install -r requirements.txt
   ```

2. Upewnij się, że masz zainstalowany **FFmpeg** (np. `sudo apt install ffmpeg`)

3. Stwórz plik `.env` lub podmień token w `bot.run("TOKEN")`

4. Odpal bota:
   ```bash
   python bot.py
   ```

---

## 📜 Przykładowe komendy

```
/join            – dołącz do kanału głosowego
/zagraj <nazwa>  – zagraj utwór z SoundClouda
/ballada         – specjalny numer Jaskiera
/szukaj <słowo>  – wyszukaj 5 pasujących ballad i wybierz
/stop            – zatrzymaj pieśń
/wyjdz           – zakończ występ
```

---

## 🧭 Przyszłe funkcje
- Playlisty!
- Głosowanie na kolejną piosenkę
- Więcej magicznych wypowiedzi Jaskiera

---

## 🛡️ Licencja
Projekt stworzony do celów edukacyjnych i rozrywkowych. Nie jestem właścicielem żadnej muzyki odtwarzanej przez bota – wszelkie prawa należą do twórców na SoundCloud.
