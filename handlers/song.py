# Telegramda yani ben boş işler müdürü :) <> Murti Tarafından düzenlenen ufak çaplı proje. 
import os
import requests
import aiohttp
import yt_dlp
import wget

from pyrogram import Client, filters
from youtube_search import YoutubeSearch
from yt_dlp import YoutubeDL

from config import BOT_USERNAME
from helpers.filters import command


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(":"))))



@bot.on_message(filters.command("indir") & ~filters.edited)
def bul(_, message):
    query = " ".join(message.command[1:])
    m = message.reply("🔎")
    ydl_ops = {"format": "bestaudio[ext=m4a]"}
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)
        duration = results[0]["duration"]

    except Exception as e:
        m.edit("<b>⛔ **Üzgünüm Şarkıyı Bulamadım.**</b>")
        print(str(e))
        return
    m.edit("<b>•> **İndirme Başlatıldı...**</b>")
    try:
        with yt_dlp.YoutubeDL(ydl_ops) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = f"▶️ **Şarkı**: [{title[:35]}]({link})\n⏳ **Süre**: `{duration}`\nAraştıran [Vahsi Muzik Bot](https://t.me/VahsiMuzikBot)"
        secmul, dur, dur_arr = 1, 0, duration.split(":")
        for i in range(len(dur_arr) - 1, -1, -1):
            dur += int(float(dur_arr[i])) * secmul
            secmul *= 60
        m.edit("•> **Yüklüyorum**...")
        message.reply_audio(audio_file, caption=rep, parse_mode='md',quote=False, title=title, duration=dur, thumb=thumb_name, performer="@uslanmazmurti")
        m.delete()
        bot.send_audio(chat_id=-1001820185928, audio=audio_file, caption=rep, performer="@uslanmazmurti", parse_mode='md', title=title, duration=dur, thumb=thumb_name)
    except Exception as e:
        m.edit("<b>⛔ **Hata Bekle Ve Tekrar Dene** .</b>")
        print(e)

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)
 

@Client.on_message(
    command(["vbul", "vindir"]) & ~filters.edited
)
async def vsong(client, message):
    ydl_opts = {
        "format": "best",
        "keepvideo": True,
        "prefer_ffmpeg": False,
        "geo_bypass": True,
        "outtmpl": "%(title)s.%(ext)s",
        "quite": True,
    }
    query = " ".join(message.command[1:])
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)
        results[0]["duration"]
        results[0]["url_suffix"]
        results[0]["views"]
        message.from_user.mention
    except Exception as e:
        print(e)
    try:
        msg = await message.reply("•> **Video İndiriyorum...**")
        with YoutubeDL(ydl_opts) as ytdl:
            ytdl_data = ytdl.extract_info(link, download=True)
            file_name = ytdl.prepare_filename(ytdl_data)
    except Exception as e:
        return await msg.edit(f"🚫 **Hata:** {e}")
    preview = wget.download(thumbnail)
    await msg.edit("•> **Video Yüklüyorum...**")
    await message.reply_video(
        file_name,
        duration=int(ytdl_data["duration"]),
        thumb=preview,
        caption=ytdl_data["title"],
    )
    try:
        os.remove(file_name)
        await msg.delete()
    except Exception as e:
        print(e)
