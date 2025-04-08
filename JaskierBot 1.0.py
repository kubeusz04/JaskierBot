import discord
from discord.ext import commands
import yt_dlp
import asyncio
import random
from collections import defaultdict
import json
import os



ranking_file = "ranking.json"
punkty = {}


def zapisz_ranking():
    with open(ranking_file, "w") as f:
        json.dump(punkty, f)

# Pytania do quizu
pytania_quiz = [
    "Kto najprawdopodobniej zniknie po 1 piwie?",
    "Kto najgłośniej śpiewa na voice?",
    "Kto zasnąłby podczas walki z potworem?",
    "Kto zawsze znajdzie mema idealnego do sytuacji?",
    "Kto najczęściej zapomina o czymś ważnym?",
    "Kto ma najbardziej oryginalne memy?",
    "Kto spóźnia się zawsze na spotkania?",
    "Kto najczęściej robi zakupy online?",
    "Kto jest mistrzem gotowania (albo przynajmniej tak twierdzi)?",
    "Kto najczęściej zmienia status na Discordzie?",
    "Kto zawsze zaprasza wszystkich do wspólnego grania?",
    "Kto zasnąłby w kinie podczas oglądania filmu?",
    "Kto zawsze mówi, że 'wczoraj jeszcze pamiętał'?",
    "Kto jest największym fanem jakiegoś serialu?",
    "Kto najlepiej opowiada historie?",
    "Kto najchętniej chodzi na spacery?",
    "Kto zasnąłby w trakcie pracy?",
    "Kto zawsze znajdzie sposób, żeby opóźnić ważne zadanie?",
    "Kto najczęściej wpada w dziwne pomysły?",
    "Kto zawsze wie, co się dzieje w popkulturze?",
    "Kto najlepiej śpiewa na karaoke?",
    "Kto zawsze przynosi coś do jedzenia na wspólne spotkania?",
    "Kto najczęściej zaczyna śmiać się w najmniej odpowiednich momentach?",
    "Kto jest najbardziej kreatywny?",
    "Kto ma najdziwniejsze hobby?",
    "Kto najbardziej lubi sprzątać?",
    "Kto najczęściej rozśmiesza innych bez powodu?",
    "Kto zawsze włącza kamerę na Zoomie?",
    "Kto najlepiej radzi sobie w grach komputerowych?",
    "Kto nigdy nie zamyka drzwi, nawet gdy to robią wszyscy?",
    "Kto jest najbardziej nieśmiały?",
    "Kto najczęściej zaprasza innych do wspólnych działań?",
    "Kto z nas najczęściej mówi: 'Będzie dobrze!'?",
    "Kto najczęściej przekłada plany na później?",
    "Kto najbardziej szanuje porządek?",
    "Kto potrafi najdłużej nie rozmawiać z nikim?",
    "Kto najczęściej pisze 'dziękuję' w każdej rozmowie?",
    "Kto najlepszy w rozwiązywaniu problemów?",
    "Kto potrafi wyjść z każdej sytuacji bez konsekwencji?",
    "Kto ma największą kolekcję gadżetów związanych z czymś, co kocha?",
    "Kto zawsze prowadzi dyskusje o filmach i serialach?",
    "Kto jest najbardziej 'na czasie' z najnowszymi technologiami?",
    "Kto najlepiej radzi sobie z zarządzaniem czasem?",
    "Kto zna najbardziej nietypowe fakty?",
    "Kto najczęściej dostaje śmieszne wpadki?",
    "Kto najbardziej stara się trzymać 'diety'?",
    "Kto najczęściej narzeka na pogodę?",
    "Kto najbardziej dba o swoją kolekcję książek?",
    "Kto najczęściej mówi: 'Jeszcze tylko 5 minut!'?",
    "Kto by zapomniał, że w ogóle dołączył na voice?",
    "Kto najpewniej powiedziałby coś dziwnego przez sen?",
    "Kto wygląda jakby ciągle był na urlopie?",
    "Kto najbardziej przypomina postać z kreskówki?",
    "Kto by wylał herbatę na klawiaturę… drugi raz w tygodniu?",
    "Kto najczęściej wycisza mikrofon i zapomina go włączyć?",
    "Kto najpewniej przegrałby z lodówką w szachy?",
    "Kto najczęściej udaje, że słucha?",
    "Kto najchętniej zamieszkałby w lodówce?",
    "Kto miałby największą szansę przeżyć apokalipsę zombie… przez przypadek?",
    "Kto by się zgubił we własnym mieście?",
    "Kto najpewniej wszedłby na voice i powiedział: 'Co tu się dzieje?'",
    "Kto najczęściej odpowiada 'XD' zamiast rozwiązać problem?",
    "Kto mógłby mieć swój program w TV o dziwnych przygodach?",
    "Kto powinien mieć zakaz opowiadania żartów?",
    "Kto zawsze klika 'Zamknij' zanim przeczyta komunikat?",
    "Kto najczęściej mówi 'zaraz wracam' i znika na godzinę?",
    "Kto nie odróżnia lewej od prawej, ale jakoś daje radę?",
    "Kto by się spóźnił na własne urodziny?",
    "Kto mówi 'ostatni mecz' i gra do 3 w nocy?",
    "Kto wygląda jak NPC podczas rozmowy?",
    "Kto zawsze odpowiada memem?",
    "Kto by zapomniał, że sam zorganizował quiz?",
    "Kto by się śmiał z własnego żartu zanim go dokończy?",
    "Kto się zmutował i zapomniał?",
    "Kto najczęściej robi miny do kamery, jak nikt nie patrzy?",
    "Kto najczęściej mówi: 'Ale to był plan B!'",
    "Kto najczęściej ma lag – mentalny, nie internetowy?",
    "Kto najpewniej przypadkiem zrobiłby live publiczny?",
    "Kto by założył kapcie nie do pary i jeszcze się ucieszył?",
    "Kto by zgubił myszkę, trzymając ją w ręku?",
    "Kto najpewniej zapytałby Google o to, jak włączyć Google?",
    "Kto by wygrał konkurs na najbardziej losowy komentarz?",
    "Kto by powiedział: 'Nie wiem co robię, ale działa!'?",
    "Kto najczęściej mówi: 'To nie bug, to feature'?",
    "Kto by zasnął w trakcie tego quizu?",
    "Kto najczęściej robi 'dziwne dźwięki' na voice?",
    "Kto wygląda jakby właśnie wstał – o 20:00?",
    "Kto najpewniej wcisnąłby ALT+F4 „bo tak kazali”?",
    "Kto jest chodzącym memem?",
    "Kto najpewniej zniknąłby po upojnej nocy... i obudził się w innym mieście?",
    "Kto powiedziałby 'kocham cię'... do kebaba o 4:00 rano?",
    "Kto wygląda jakby potrzebował terapii, ale najpierw drinka?",
    "Kto najczęściej mówi 'nie jestem pijany', przewracając się o własny cień?",
    "Kto miałby zakaz wstępu do 3 klubów i 2 kościołów?",
    "Kto powiedziałby 'to była faza eksperymentalna', mając na myśli ostatnie 5 lat?",
    "Kto najpewniej miałby OnlyFans... z memami stóp?",
    "Kto mówi 'żadne uzależnienie, to pasja!'?",
    "Kto najczęściej randkuje z ludźmi, których nawet nie zna… po imieniu?",
    "Kto ma fazę 'kocham cię' po 2 piwach, a 'nienawidzę cię' po 3?",
    "Kto ma playlistę na seks, walkę i zakupy – tę samą?",
    "Kto miałby nagranie ze swojego kompromitującego tańca... jako NFT?",
    "Kto najpewniej powiedziałby 'to nie był kink-shaming, to była troska'?",
    "Kto przeszedłby przez piekło... dla jednego zdjęcia z ex?",
    "Kto flirtuje jakby prowadził podcast kryminalny?",
    "Kto miałby dziwne rzeczy w historii wyszukiwania i jeszcze się tym chwalił?",
    "Kto by powiedział 'to była orgia edukacyjna' i nie żartował?",
    "Kto powiedział 'kocham cię' do lusterka – po całym dniu?",
    "Kto by zrobił test DNA... z ciekawości, czy to jego pies?",
    "Kto miałby tatuaż z błędem ortograficznym i jeszcze go bronił?"
]


emoji_lista = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣']


# Wczytaj ranking z pliku (jeśli istnieje)
if os.path.exists(ranking_file):
    with open(ranking_file, "r") as f:
        punkty = json.load(f)
else:
    punkty = {}


# Intencje i prefix komend
intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True

bot = commands.Bot(command_prefix='/', intents=intents)

# Opcje dla FFmpeg
FFMPEG_OPTIONS = {
    'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
    'options': '-vn'
}

# Opcje dla yt_dlp z działającym SoundCloud client_id
ydl_opts = {
    'format': 'bestaudio/best',
    'quiet': True,
    'default_search': 'auto',
    'extractor_args': {
        'soundcloud': {
            'client_id': ['Tu ID']  
        }
    }
}

@bot.event
async def on_ready():
    print(f'✅ Zalogowano jako {bot.user.name}')

# Komenda: dołącz do kanału głosowego
@bot.command()
async def wejdz(ctx):
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        await channel.connect()
        await ctx.send("🎤 Ah, moi drodzy! Zgadujcie, kto właśnie dołączył do Waszego kanału głosowego? Tak, to ja – Jaskier! 🎶")
    else:
        await ctx.send("❌ Och, smutna wieść! Musisz być na kanale głosowym, by móc usłyszeć moje cudowne pieśni!")

# Komenda: odtwórz piosenkę z SoundClouda po nazwie
@bot.command()
async def zagraj(ctx, *, query: str):
    if not ctx.voice_client:
        await ctx.invoke(bot.get_command("join"))

    search_url = f"scsearch1:{query}"  # szukamy tylko 1 pasujący wynik na SC

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(search_url, download=False)
        if "entries" in info:
            info = info["entries"][0]  # pierwszy wynik

        source = info["url"]
        title = info.get("title", "Nieznany tytuł")

    ctx.voice_client.stop()
    ctx.voice_client.play(discord.FFmpegPCMAudio(source, **FFMPEG_OPTIONS))
    await ctx.send(f"▶️ A teraz, ballada o nazwie: **{title}**")

# Komenda: wyjście z kanału
@bot.command()
async def wyjdz(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        await ctx.send("👋 No cóż, to był zaszczyt, ale czas na mnie!")
    else:
        await ctx.send("Hej! Muszę być na tym samym kanale głosowym co ty by grać ballady!")

# Komenda: pauza
@bot.command()
async def pauza(ctx):
    if ctx.voice_client and ctx.voice_client.is_playing():
        ctx.voice_client.pause()
        await ctx.send("⏸️ Wstrzymuję te cudowne dźwięki! Potrzebujecie przerwy na podziwianie mojego głosu!")
    else:
        await ctx.send("❌ Mam coś zagrać? Puki co moja lutnia czeka!")

# Komenda: wznowienie
@bot.command()
async def wznowienie(ctx):
    if ctx.voice_client and ctx.voice_client.is_paused():
        ctx.voice_client.resume()
        await ctx.send("▶️ Na czym to ja stanołem? Ahh tak!")
    else:
        await ctx.send("O czym ty mówisz? Przecież wysłuchałeś całej mojej pieśni")

@bot.command()
async def ballada(ctx):
    if not ctx.voice_client:
        await ctx.invoke(bot.get_command("join"))

    url = "https://soundcloud.com/piotr-koz-owski-460663538/piotr-kozlowski-zapachnialo-powiewem-jesieni"

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        source = info["url"]
        title = info.get("title", "Nieznany utwór")

    ctx.voice_client.stop()
    ctx.voice_client.play(discord.FFmpegPCMAudio(source, **FFMPEG_OPTIONS))
    await ctx.send(f"🍁🎤 Ach, moi przyjaciele! Specjalnie dla Was – mój popisowy numer! Wsłuchajcie się w powiew jesieni!")


@bot.command()
async def groszadaj(ctx):
    if not ctx.voice_client:
        await ctx.invoke(bot.get_command("join"))

    url = "https://soundcloud.com/user-295714458/netflix-wiedzmin-ost-grosza-daj-wiedzminowi-soundtrack"

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        source = info["url"]
        title = info.get("title", "Nieznany utwór")

    ctx.voice_client.stop()
    ctx.voice_client.play(discord.FFmpegPCMAudio(source, **FFMPEG_OPTIONS))
    await ctx.send(f"🎤 Ach, wiedziałem że o nią poprosisz! Proszę bardzo, specjalnie dla ciebie!")

# Komenda: stop
@bot.command()
async def zatrzymaj(ctx):
    if ctx.voice_client and ctx.voice_client.is_playing():
        ctx.voice_client.stop()
        await ctx.send("⏹️ Ah! I oto zakończyliśmy ten występ! Ale nie martwcie się, mój głos zawsze wraca!")
    else:
        await ctx.send("❌ Nic teraz nie gra, moi drodzy! Czas na przerwę!")

@bot.command()
async def szukaj(ctx, *, search: str):
    await ctx.send(f"🎶 Dajcie mi chwilkę... próbuję sobie przypomnieć ballady zawierające: **{search}**")

    ydl_opts_search = {
        'format': 'bestaudio/best',
        'quiet': True,
        'default_search': 'auto',
        'extractor_args': {
            'soundcloud': {
                'client_id': ['Tu ID'] 
            }
        }
    }

    with yt_dlp.YoutubeDL(ydl_opts_search) as ydl:
        try:
            search_query = f"scsearch5:{search}"
            results = ydl.extract_info(search_query, download=False)
            entries = results.get('entries', [])[:5]
        except Exception as e:
            await ctx.send(f"🎻 Wybaczcie, coś poszło nie tak przy szukaniu ballady: `{e}`")
            return

    if not entries:
        await ctx.send("🥀 Nic nie znalazłem. Może inna fraza?")
        return

    emoji_list = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣']
    message = "**🎼 Oto moje propozycje! Zagłosuj reakcją:**\n\n"
    for i, entry in enumerate(entries):
        message += f"{emoji_list[i]} **{entry['title']}**\n"

    vote_msg = await ctx.send(message)

    for emoji in emoji_list[:len(entries)]:
        await vote_msg.add_reaction(emoji)

    await asyncio.sleep(3)

    vote_msg = await ctx.channel.fetch_message(vote_msg.id)
    max_votes = 0
    chosen_index = 0

    for i, reaction in enumerate(vote_msg.reactions[:len(entries)]):
        users = [user async for user in reaction.users() if not user.bot]
        count = len(users)
        if count > max_votes:
            max_votes = count
            chosen_index = i

    selected = entries[chosen_index]
    url = selected['url']

    await ctx.invoke(bot.get_command("join"))

    with yt_dlp.YoutubeDL(ydl_opts_search) as ydl:
        try:
            info = ydl.extract_info(url, download=False)
            stream_url = info['url']
            title = info.get('title', 'Nieznany utwór')
        except Exception as e:
            await ctx.send(f"❌ Ups, nie mogę zagrać tej ballady: `{e}`")
            return

    ctx.voice_client.stop()
    ctx.voice_client.play(discord.FFmpegPCMAudio(stream_url, **FFMPEG_OPTIONS))
    await ctx.send(f"🎤 Zwycięska ballada to: **{title}**! Niech zabrzmi w całym królestwie!")

@bot.command()
async def quiz(ctx):
    if not ctx.author.voice or not ctx.author.voice.channel:
        await ctx.send("❌ Musisz być na kanale głosowym, by rozpocząć quiz!")
        return

    channel = ctx.author.voice.channel
    czlonkowie = [m for m in channel.members if not m.bot]

    if len(czlonkowie) < 2:
        await ctx.send("👥 Potrzeba przynajmniej 2 osób na kanale głosowym!")
        return

    losuj = random.sample(czlonkowie, min(5, len(czlonkowie)))
    pytanie = random.choice(pytania_quiz)

    opis = "\n".join([f"{emoji_lista[i]} {user.mention}" for i, user in enumerate(losuj)])
    embed = discord.Embed(
        title="🎭 Wybierz do kogo najbardziej to pasuje:",
        description=f"**{pytanie}**\n\nGłosujcie reakcjami:\n{opis}",
        color=discord.Color.gold()
    )
    quiz_msg = await ctx.send(embed=embed)

    for i in range(len(losuj)):
        await quiz_msg.add_reaction(emoji_lista[i])

    await ctx.send("⏳ Macie 30 sekund na głosowanie!")

    await asyncio.sleep(30)
    quiz_msg = await ctx.channel.fetch_message(quiz_msg.id)

    reakcje = quiz_msg.reactions
    max_glosy = 0
    zwyciezca = None

    for i, reaction in enumerate(reakcje):
        async for user in reaction.users():
            if user.bot:
                continue
            user_id = str(losuj[i].id)
            punkty[user_id] = punkty.get(user_id, 0) + 1

        if reaction.count - 1 > max_glosy:
            max_glosy = reaction.count - 1
            zwyciezca = losuj[i]

    zapisz_ranking()

    if zwyciezca:
        await ctx.send(f"🏆 **{zwyciezca.mention}** wygrał rundę quizu! Chodź nie jestem pewien czy to powód do dumy... ")
    else:
        await ctx.send("😶 Brak głosów! Jestem zasmucony...")


@bot.command()
async def ranking(ctx):
    if not punkty:
        await ctx.send("🏁 Brak wyników – quiz jeszcze się nie rozpoczął!")
        return

    ranking = sorted(punkty.items(), key=lambda x: x[1], reverse=True)
    embed = discord.Embed(title="📜 Ranking ", color=discord.Color.purple())

    for i, (user_id, pkt) in enumerate(ranking[:10]):
        user = ctx.guild.get_member(int(user_id))
        if user:
            embed.add_field(name=f"{i+1}. {user.display_name}", value=f"{pkt} punktów", inline=False)

    await ctx.send(embed=embed)


# Uruchom bota
bot.run("Tu Token")
