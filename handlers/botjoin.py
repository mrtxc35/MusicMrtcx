from callsmusic.callsmusic import client as USER
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserAlreadyParticipant
from helpers.decorators import errors, authorized_users_only

@Client.on_message(filters.group & filters.command(["katil", "asistan"]))
@authorized_users_only
@errors
async def addchannel(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>Beni Önce Yönetici Yapmalısın</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name =  "VahsiMuzik Asistan"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id,"•> **Senin İsteğin Üzerine Geldim** !")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>Asistan Zaten Grupta!</b>",
        )
        pass
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>⛔ Hata ⛔\nAsistanın grupta yasaklanmadığından emin olun."
            "\n\n Yada Asistan Hesabını Gruba Kendin Ekle\n\nAsistan Adı: @VahsiMuzikAsistan1\nAsistan Kimliği: 5620230571</b>",
        )
        return
    await message.reply_text(
            "<b>Asistan Zaten Grupta Var</b>",
        )
    
@USER.on_message(filters.group & filters.command(["ayril", "asistanby"]))
async def rem(USER, message):
    try:
        await USER.leave_chat(message.chat.id)
    except:  
        await message.reply_text(
            f"<b>Kullanıcı grubunuzdan ayrılamadı!."
            "\n\nYada Kendin Çıkarabilirsin</b>",
        )
        return
 
 
 
