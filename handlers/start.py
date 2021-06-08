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
        f"""<b>🏖️ Welcome {message.from_user.first_name}!
BlissMusic is a project designed for play, as simple as possible, music in your groups through the new voice chats introduced by Telegram.

❓How to use it?
Press the » /help command to view the full list of the commands of the bot!
<\b>""",
      
       
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Credit", url="https://t.me/luciddo",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Group", url="https://t.me/unitedbotsupport"
                    ),
                    InlineKeyboardButton(
                        "Channel", url="https://t.me/Tubots"
                    ),
                    InlineKeyboardButton(
                        "Bliss song", url="https://t.me/missblissrobot"
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
                        "Channel", url="https://t.me/Tubots"
                    ),
                    InlineKeyboardButton(
                        "Group", url="https://t.me/Unitedbotsupport"
                    )
                ],    
                [    
                    InlineKeyboardButton(
                        "Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No", callback_data="close"
                    )
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("help")
    & filters.private
    & ~ filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name}!
\n/play <song name> - play song you requested
/dplay <song name> - play song you requested via deezer
/splay <song name> - play song you requested via jio saavn
/playlist - Show now playing list
/current - Show now playing
/song <song name> - download songs you want quickly
/search <query> - search videos on youtube with details
/deezer <song name> - download songs you want quickly via deezer
/saavn <song name> - download songs you want quickly via saavn
/video <song name> - download videos you want quickly
\n*Admins only*
/player - open music player settings panel
/pause - pause song play
/resume - resume song play
/skip - play next song
/end - stop music play
/userbotjoin - invite assistant to your chat
/admincache - Refresh admin list
 </b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Cʜᴀɴɴᴇʟ", url="https://t.me/tc_bots"
                    ),
                    InlineKeyboardButton(
                        "Gʀᴏᴜᴘ", url="https://t.me/tcbotsbugs"
                    )
                ]
            ]
        )
    )    
