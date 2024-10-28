from pyamino import Bot, Client
from pyamino.ext import *
import random
import json
import requests
import sqlite3
import shutil

# Initialize the bot
bot = Bot(
    command_prefix="/",
    community_id=67,
    console_enabled=False,
    device_id=None,
    intents=True,
    online_status=True,
    signature_key="DFA5ED192DDA6E88A12FE12130DC6206B1251E44",
    device_key="E7309ECC0953C6FA60005B2765F99DBBC965C8E9",
    KEY="a9c6bb6f-2fb6-4ada-b10f-09d8b73e6796"
    #proxy="http://orubkglj:08pw1vm4zwqx@45.127.248.127:5128"
    ) 
client = Client(
    signature_key="DFA5ED192DDA6E88A12FE12130DC6206B1251E44",
    device_key="E7309ECC0953C6FA60005B2765F99DBBC965C8E9",
    KEY="a9c6bb6f-2fb6-4ada-b10f-09d8b73e6796"
    )

@bot.on_ready()
def ready():
    print(f"{bot.profile.username} has logged in!")

@bot.on_member_leave()
def leave(ctx: Context):
    ctx.reply("Nos entristece que te vayas, te deseamos buena suerte :(")

@bot.command(
    name="ping", # Set the name of the command.
    description="This will reply with Pong!", # Set the description of the command.
    aliases=["p"], # Set the aliases of the command. This will allow !p to be used as !ping.
    cooldown=4 # Set the cooldown of the command. This will prevent the command from being used for <cooldown> seconds.
    )
def ping(ctx: Context):
    ctx.reply("Pong!")

@bot.command("hola")
def say(ctx: Context, message: str):
    ctx.reply("Hola que tal, todo bien?")

@bot.command("comentar")
def saludar(ctx: Context):
    client.comment("tu eres mas guap@ que el 99.99% del mundo", ctx.author.uid)
    ctx.send("Comentario agregado!")

@bot.command("carta")
def cartaidol(ctx: Context):
    cards = ["JisooTT.png", "YoongiFUT.png", "JennieFUT.png", "JisooFUT.png", "JinsoulFUT.png", "LisaFUT.png", "HeejinFUT.png", "JypFUT.png", "SmFUT.png", "KarinaFUT.png", "NingningFUT.png", "RoseFUT.png", "YgFUT.png", "XiaotingFUT.png", "ClFUT.png", "BahiyyihFUT.png", "JuyeonFUT.png", "PsyFUT.png", "YeojinFUT.png", "VillanaFUT.png", "SuzyFUT.png", "DaniFUT.png", "MaribelFUT.png", "LisaPV.png", "JenniePV.png", "JisooPV.png", "RosePV.png", "Dawn.png", "Spreen.png", "DanielleFUT.png", "HaerinFUT.png", "HyeinFUT.png", "MinjiFUT.png", "HanniFUT.png"]
    select = random.choice(cards)
    img = "/home/max/Documents/pydocs/media/idols/" + select
    ctx.send_image(image=img)
    ctx.send("Carta de: " + ctx.author.nickname)
    
@bot.command("caracola")
def caracola(ctx: Context, message: str):
    resp = ["Ni idea crack", "Y yo que se?", "Si", "No", "Pero.. como?", "Por supuesto", "Negativo", "Afirmativo", "Claro que si!", "Claro que no!", "...", "keseyo", "y yo kese", "Pregunta a quien este en llamada", "RETO: arroba a tu novi@ y dile que apesta!... ah y referente a tu prefunta no se herman@..", "Y hoy en su seccion Preguntas Tontas: " + message]
    asn = random.choice(resp)
    ctx.reply(asn)

@bot.command("pid")
def pid(ctx: Context):
    cha = ctx.message.content[5:200]
    if ctx.author.uid == "fc83578c-706a-44ef-bc2a-e2c119f2fe92":
        uide = client.community.fetch_object_id(link=cha)
        ctx.reply(uide)
    else:
        ctx.reply("No tienes permiso para ejecutar este comando!")

@bot.command("compatibilidad")
def compatibilidad(ctx: Context, message: str):
    user = ctx.author.nickname
    user2 = message
    love = random.randint(0, 100)
    ctx.send("La compatibilidad entre " + user + " y " + user2 + " es de:\n[BC]" + str(love) + "%")

@bot.on_member_join()
def join(ctx: Context):
    ctx.send("Hola " + ctx.author.nickname + ", se bienvenid@ a Ven a socializar !! ᴬⁿⁱᵐᵉ, esperamos que te la pases muy bien :)")

@bot.on_chat_tip()
def tip(ctx: Context):
    ctx.send("Muchas gracias por tu aportacion " + ctx.author.nickname + " ^^")

@bot.command("rascaygana")
def rascaygana(ctx: Context):
    imu = "/home/max/Documents/pydocs/media/CartaRYG.png"
    ctx.send_image(imu)
    ctx.send("El rasca y gana es un minijuego de azar, donde si usas /rascar y te sale la carta con los diamantes ganas 20 ACs")

@bot.command("rascar")
def rascar(ctx: Context, ct: Community):
    ui = ctx.author.uid
    file = open("cooldown.txt", "r").read()
    if ui in file:
        ctx.reply("Tu ya has rascado una carta, vuelve mañana ^^")
    else:
        with open("cooldown.txt", "a") as arch:
            arch.write(ui + "\n")
            arch.close()
        opts = ["CartaRYGGana.png", "CartaRYGPierde.png"]
        uri = "/home/max/Documents/pydocs/media/"
        card = random.choice(opts)
        carta = uri + card
        ctx.send_image(carta)
        if card == "CartaRYGGana.png":
            ctx.send("Felicidades " + ctx.author.nickname)
            wks = client.community.fetch_user_wikis(userId=ctx.author.uid, start=0, size=2, comId="67")
            wiki = wks.wikiId[0]
            ct.send_coins(coins=25, wikiId=wiki)

@bot.command("video")
def video(ctx: Context, msg: str):
    id = msg
    url = "https://ytstream-download-youtube-videos.p.rapidapi.com/dl"
    querystring = {"id":id}
    headers = {
        "X-RapidAPI-Key": "082395124cmsh8f011e89c74584fp1b5c87jsn52b9ca1173b4",
        "X-RapidAPI-Host": "ytstream-download-youtube-videos.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    mp4 = response.json()
    vid = mp4["formats"][0]["url"]
    ctx.send_image(vid)

@bot.command("img")
def img(ctx: Context):
    ctx.send_image(image="https://i.ytimg.com/vi/5AAyh7scplM/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLB8sKmlAv7uyI0YWqQGRLr1NzxLvA")
    ctx.send(mentioned=[ctx.author.uid], content="a")

@bot.on_error()
def error(error: Exception): # This will be called when an error occurs.
    print(f"An error has occurred: {error}")

@bot.command("cid")
def cid(ctx: Context):
    cuid = ctx.message.chatId
    ctx.send(cuid)

@bot.command("cancion")
def cancion(ctx: Context, cmn: Community):
    song = ctx.message.content[9:200]
    url = "https://youtube-search-and-download.p.rapidapi.com/search"
    querystring = {"query":song,"hl":"es","gl":"MX","type":"v","duration":"s","sort":"r"}
    headers = {
	   "X-RapidAPI-Key": "082395124cmsh8f011e89c74584fp1b5c87jsn52b9ca1173b4",
	   "X-RapidAPI-Host": "youtube-search-and-download.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    song = response.json()
    q = open("ids.txt", "w")
    f = open("songs.txt", "w")
    for cancion in range(5):
        titulo = song["contents"][cancion]["video"]["title"]
        id = song["contents"][cancion]["video"]["videoId"]
        dura = song["contents"][cancion]["video"]["lengthText"]
        putt = "Titulo: " + titulo + " | ID: " + id + " | Duracion:" + dura + "\n[C]-×-" + "\n"
        q.write(id + "\n")
        f.write(putt)
    f.close()
    q.close()
    h = open("songs.txt", "r").read()
    ctx.send(content=h)

@bot.command("play")
def play(ctx: Context):
    idu = ctx.message.content[6:80]
    uno = open("ids.txt", "r")
    if idu == "1":
        idi = uno.read()[0:11]
    elif idu == "2":
        idi = uno.read()[12:23]
    elif idu == "3":
        idi = uno.read()[24:35]
    elif idu == "4":
        idi = uno.read()[36:47]
    elif idu == "5":
        idi = uno.read()[48:59]
    else:
        print("a")
    print(idi)
    url = "https://ytstream-download-youtube-videos.p.rapidapi.com/dl"
    querystring = {"id":idi}
    headers = {
	    "X-RapidAPI-Key": "082395124cmsh8f011e89c74584fp1b5c87jsn52b9ca1173b4",
	    "X-RapidAPI-Host": "ytstream-download-youtube-videos.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    pum = response.json()
    link = pum["formats"][0]["url"]
    ctx.send_audio(audio=link)

@bot.command("icon")
def icon(ctx: Context):
    msg = ctx.message.content[6:50]
    uid = bot.community.fetch_object_id(link=msg)
    avt = bot.community.fetch_user(userId=uid).avatar
    ctx.send_image(avt)

@bot.command("tts")
def tts(ctx: Context):
    msg = ctx.message.content[5:4000]
    url = "https://express-voic-text-to-speech.p.rapidapi.com/getAudioLink"
    querystring = {"service":"StreamElements","voice":"Brian","text":msg}
    headers = {
	    "x-rapidapi-key": "082395124cmsh8f011e89c74584fp1b5c87jsn52b9ca1173b4",
	    "x-rapidapi-host": "express-voic-text-to-speech.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    url = data["audio_url"]
    ctx.send_audio(audio=url)

@bot.on_text_message()
def on_text_message(ctx: Context):
    usuario = ctx.author.nickname
    with open("msgs.txt", "a") as f:
        f.write(ctx.author.nickname + ": " + ctx.message.content)
    f.close()

@bot.command("clima")
def clima(ctx: Context):
    msg = ctx.message.content[7:100]
    response = requests.get("https://api.weatherapi.com/v1/current.json?key=d57ce648a23a4ff99a040359240204&q=" + msg + "&aqi=no")
    datin = response.json()
    tempe = datin["current"]["temp_c"]
    naim = datin["location"]["name"]
    ctx.send("Hola muy buenas tardes, hoy en la ciudad de " + naim + ", la temperatura es de: " + str(tempe)[0:3] + "°")

@bot.command("confesar")
def confesar(ctx: Context):
    txt = ctx.message.content[10:4000]
    if len(txt) <= 5:
        ctx.replt("Escribe una confesion de verdad!")
    elif len(txt) >= 6:
        bot.community.send_message(chatId="f2a7c255-ce11-40bd-8b24-d7b26bd9a557", content="[BC]Confesion Anonima\n[I]" + txt)

@bot.command("emojify")
def emojify(ctx: Context):
    emo = ["🙉💋😡","👻🧠🖕","🥸😭😱","🙄😒🤪","🤟😽🤑","🍑🍆🥺","👳‍♂️🖤☠️","🤜🤰💨","💋🥵💦","💪🫦👬","👭💘👵","🤑🤡💩"]
    ji = random.choice(emo)
    ctx.reply("Si te tuviera que definir en tres emojis, serian estos: " + ji)

@bot.command("comandos")
def comandos(ctx: Context):
    ctx.send("[BC]Lista de Comandos\n/ping - Verifica si el bot esta online.\n/hola - El bot te saluda.\n/caracola (pregunta) - Hazle una pregunta y te dira una respuesta.\n/clima (ciudad) - Te dice la temperatura.\n/comptabilidad (nombre de otro usuario) - Mide su compatibilidad.\n/tts (mensaje) - Hace que el bot diga tu mensaje con su voz.\n/confesar (mensaje) - Haz una confesion anonima, para enviar el comando hazlo en un chat con el bot privado\n/rascaygana - Te explica un juego que tenemos en el chat.\n/emojify - Te define en tres emojis.\n/horoscopo (signo) - Te dice tu horoscopo.")

@bot.command("horoscopo")
def horoscopo(ctx: Context):
    msg = ctx.message.content[11:200]
    horo = msg.capitalize()
    if horo == "Geminis":
        horo = "gemini"
    elif horo == "Tauro":
        horo = "taurus"
    elif horo == "Sagitario":
        horo = "Sagittarius"
    elif horo == "Piscis":
        horo = "Pisces"
    elif horo == "Escorpio":
        horo = "Scorpio"
    elif horo == "Acuario":
        horo = "Aquarius"
    elif horo == "Capricornio":
        horo = "Capricorn"
    url = "https://horoscope-app-api.vercel.app/api/v1/get-horoscope/daily?sign=" + horo + "&day=today"
    response = requests.get(url)
    datazo = response.json()
    horoscopo = datazo["data"]["horoscope_data"]
    url2 = "https://google-translate113.p.rapidapi.com/api/v1/translator/text"
    payload = {
        "from": "en",
        "to": "es",
        "text": horoscopo
    }
    headers = {
	    "content-type": "application/x-www-form-urlencoded",
	    "X-RapidAPI-Key": "082395124cmsh8f011e89c74584fp1b5c87jsn52b9ca1173b4",
	    "X-RapidAPI-Host": "google-translate113.p.rapidapi.com"
    }
    res = requests.post(url2, data=payload, headers=headers)
    datafono = res.json()
    texto = datafono["trans"]
    ctx.send("[B]Para ti mi " + horo + ":\n" + texto)

bot.run("asterixyt@yahoo.com", "Loading500-")