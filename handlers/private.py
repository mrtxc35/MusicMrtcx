from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from config import BOT_USERNAME, BOT_NAME as bot
from helpers.filters import command, other_filters2
# Ballas Müzik tarafından düzenlendi. 

@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]))
async def start(_, message: Message):
                await message.reply_photo(
                "https://images.app.goo.gl/MTLXTSDCA4MLHScP7",
                caption=(f"""**🤖 Mᴇʀʜᴀʙᴀ, Bᴇɴ Vᴀʜsɪ Mᴜᴢɪᴋ Bᴏᴛ..!\n\nᴛᴇʟᴇɢʀᴀᴍ sᴇsʟɪ sᴏʜʙᴇᴛʟᴇʀɪɴᴅᴇ\n··ᴍᴜ‌ᴢɪᴋ ᴠᴇ ᴠɪᴅᴇᴏ··\nᴏʏɴᴀᴛᴀʙɪʟᴇɴ ʙɪʀ ʙᴏᴛᴜᴍ\n\n✅ ᴋᴇʏɪғʟɪ ᴠᴇ ᴋᴇsɪɴᴛɪsɪᴢ ᴍᴜ‌ᴢɪᴋ ᴅɪɴʟᴇᴍᴇᴋ﹐ ᴠɪᴅᴇᴏ ɪᴢʟᴇᴍᴇᴋ ɪᴄ‌ɪɴ\n\nʙᴏᴛᴜ ɢʀᴜʙᴀ ᴇᴋʟᴇʏᴇʀᴇᴋ\n📌 S‌ᴜ Yᴇᴛᴋɪʟᴇʀɪ Vᴇʀɪɴ﹕\n﹡ ʙᴀɢ‌ʟᴀɴᴛı ɪʟᴇ ᴅᴀᴠᴇᴛ ᴇᴛᴍᴇ\n﹡ ᴍᴇsᴀᴊʟᴀʀı sɪʟᴍᴇ\n﹡ sᴇsʟɪ sᴏʜʙᴇᴛ ʏᴏ‌ɴᴇᴛɪᴍ**"""),
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ 𝖡𝖾𝗇𝗂 𝖦𝗋𝗎𝖻𝖺 𝖤𝗄𝗅𝖾 ➕", url=f"https://t.me/VahsiMuzikBot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📚 𝖪𝗈𝗆𝗎𝗍𝗅𝖺𝗋" , callback_data= "herkes"
                    ),
                    InlineKeyboardButton(
                        "⭕ 𝖪𝖺𝗇𝖺𝗅", url="https://t.me/murtibots"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🕹 Oyun & Film Botumuz", url="https://t.me/inekgame_bot"
                    )
                ]
                
           ]
        ),
    )



@Client.on_callback_query(filters.regex("herkes"))
async def herkes(_, query: CallbackQuery):
    await query.edit_message_text(f"""<b>Temel Komutlar : \n\n» /vara => ᴠɪᴅᴇᴏ ɪɴᴅɪʀ . \n» /ara => ᴍᴜᴢɪᴋ ɪɴᴅɪʀ . \n» /oynat => ᴍᴜᴢɪᴋ ᴏʏɴᴀᴛ . \n» /durdur => ᴍᴜᴢɪɢɪ ᴅᴜʀᴅᴜʀ . \n» /devam => ᴍᴜᴢɪɢɪ sᴜʀᴅᴜʀ . \n» /atla =>  ᴍᴜᴢɪɢɪ ᴀᴛʟᴀ . \n» /son => ᴍᴜᴢɪɢɪ sᴏɴʟᴀɴᴅɪʀ . \n» /katil => ᴀsɪsᴛᴀɴɪ ɢʀᴜʙᴀ ᴅᴀᴠᴇᴛ ᴇᴅᴇʀ . \n» /reload => ᴀᴅᴍɪɴ ʟɪsᴛᴇsɪɴɪ ɢᴜɴᴄᴇʟʟᴇʀ . \n\n» /auth => ᴋᴜʟʟᴀɴɪᴄɪɴɪɴ ʏᴏɴᴇᴛɪᴄɪ ᴏʟᴍᴀᴅɪɢɪ ʜᴀʟᴅᴇ ᴋᴏᴍᴜᴛʟᴀʀɪ ᴋᴜʟʟᴀɴᴍᴀsɪɴᴀ ɪᴢɪɴ ᴠᴇʀɪʀ .  \n\n» /unauth => ᴋᴜʟʟᴀɴɪᴄɪɴɪɴ ʏᴏɴᴇᴛɪᴄɪ ᴏʟᴍᴀᴅɪɢɪ ʜᴀʟᴅᴇ ᴋᴏᴍᴜᴛʟᴀʀɪ ᴋᴜʟʟᴀɴᴍᴀsɪɴɪ ᴇɴɢᴇʟʟᴇʀ . </b>""",
    reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "🇹🇷 𝖠𝗌𝗂𝗌𝗍𝖺𝗇", url="https://t.me/VahsiMuzikAsistan1"
                     ),
                     InlineKeyboardButton(
                         "🧑🏻‍💻 𝖮𝗐𝗇𝖾𝗋", url="https://t.me/uslanmazmurti"
                     )
                 ],
                 [
                     InlineKeyboardButton(
                         "⬅️ 𝖦𝖾𝗋𝗂 ⬅️", callback_data="cbstart")
                 ] 
             ]
         )
         )



@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(f"""**🤖Mᴇʀʜᴀʙᴀ, Bᴇɴ Vᴀʜsɪ Mᴜᴢɪᴋ Bᴏᴛ..!\n\nᴛᴇʟᴇɢʀᴀᴍ sᴇsʟɪ sᴏʜʙᴇᴛʟᴇʀɪɴᴅᴇ\n··ᴍᴜ‌ᴢɪᴋ ᴠᴇ ᴠɪᴅᴇᴏ··\nᴏʏɴᴀᴛᴀʙɪʟᴇɴ ʙɪʀ ʙᴏᴛᴜᴍ\n\n✅ ᴋᴇʏɪғʟɪ ᴠᴇ ᴋᴇsɪɴᴛɪsɪᴢ ᴍᴜ‌ᴢɪᴋ ᴅɪɴʟᴇᴍᴇᴋ﹐ ᴠɪᴅᴇᴏ ɪᴢʟᴇᴍᴇᴋ ɪᴄ‌ɪɴ\n\nʙᴏᴛᴜ ɢʀᴜʙᴀ ᴇᴋʟᴇʏᴇʀᴇᴋ\n📌 S‌ᴜ Yᴇᴛᴋɪʟᴇʀɪ Vᴇʀɪɴ﹕\n﹡ ʙᴀɢ‌ʟᴀɴᴛı ɪʟᴇ ᴅᴀᴠᴇᴛ ᴇᴛᴍᴇ\n﹡ ᴍᴇsᴀᴊʟᴀʀı sɪʟᴍᴇ\n﹡ sᴇsʟɪ sᴏʜʙᴇᴛ ʏᴏ‌ɴᴇᴛɪᴍ**""",
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ 𝖡𝖾𝗇𝗂 𝖦𝗋𝗎𝖻𝖺 𝖤𝗄𝗅𝖾 ➕", url=f"https://t.me/VahsiMuzikBot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📚 𝖪𝗈𝗆𝗎𝗍𝗅𝖺𝗋" , callback_data= "herkes"
                    ),
                    InlineKeyboardButton(
                        "⭕ 𝖪𝖺𝗇𝖺𝗅", url=f"https://t.me/murtibots"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🕹 Oyun & Film Botumuz", url="https://t.me/inekgame_bot"
                    )
                ]
                
           ]
        ),
    )
