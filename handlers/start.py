#copyright just rewrote the code we dont deserve anything 😴

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_sticker("CAACAgIAAxkBAAFDgbdgvwiTHFC9NSVmiePow70hexmH5QACsgADL0ojB_9n4AABYBHysh8E")
    await message.reply_text(
        f"""<b>[💌](https://telegra.ph/file/f6fad124b1ffd3cf8eefb.png) Welcome {message.from_user.first_name}!
**BlissMusic** is a project designed for **play**, as **simple** as possible, music in your groups through the new **voice chats** introduced by Telegram.

**❓How to use it?**
Press the » COMMANDS to view the full list of the commands of the bot!
Aand read /info to know about this bot
<\b>""",
      
       
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "COMMANDS", url="https://telegra.ph/𝚖𝚞𝚜𝚒𝚚𝚘-Sᴏɴɢ-06-09",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "GROUP", url="https://t.me/unitedbotsupport"
                    ),
                    InlineKeyboardButton(
                        "CHANNEL", url="https://t.me/Tubots"
                    ),
                    InlineKeyboardButton(
                        "CREDITS", url="https://t.me/Psycho_Bots"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "ADD TO GROUPS", url="https://t.me/BlissMusicRobot?startgroup=true"
                    ) 
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "CHANNEL", url="https://t.me/Tubots"
                    ),
                    InlineKeyboardButton(
                        "GROUP", url="https://t.me/Unitedbotsupport"
                    )
                ],    
                [    
                    InlineKeyboardButton(
                        "YES", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "NO", callback_data="close"
                    )
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("info")
    & filters.private
    & ~ filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name}!
Join our group for reporting issues and bugs check commands [click here](https://telegra.ph/𝚖𝚞𝚜𝚒𝚚𝚘-Sᴏɴɢ-06-09)

use @missblissrobot for downloading songs
 </b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "SOURCE CODE", url="https://github.com/LucidoXD/musiqo"
                    ),
                    InlineKeyboardButton(
                        "WEBSITE", url="https://cutt.ly/GjBGQ0D"
                    )
                ]
            ]
        )
    )    

