# 🎸 JaskierBot – Bard Discorda

**JaskierBot** to nie tylko bot muzyczny – to pełnoprawny bard na Twoim serwerze Discord!  
Potrafi grać ballady z SoundClouda, komentować każdą komendę,  
a do tego organizuje interaktywne quizy i prowadzi ranking Twojej ekipy. 🎤🎶

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
Podaj dane, a skrypt je wstawi ✨


---

## 🧪 Wszystkie Komendy

```
/ballada   -  Zagraj popisowy numer Jaskra
/groszadaj  - Zagraj grosza daj wiedźminowi...
/pauza  - Wstrzymaj granie muzyki
/szukaj (nazwa piosenki)  - szuka 5 utworów o podanej nazwie i daje do wyboru co ma oddtworzyć
/wejdz - Wchodzi na kanał głosowy
/wyjdz - Wychodzi z kanału głosowego
/wznowienie - wznawia zatrzymaną piosenkę 
/zagraj  (nazwa piosenki)  -  Gra podany utwór
/zatrzymaj - Przerywa grę i usuwa utwór z kolejki
/quiz - Mini gra coś ala kumple - bot losuje pytanie i możecie zagłosować do kogo to pasuje (tylko dla tych co są na kanale głosowym) (edytowane)

```
