from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_sticker("CAACAgEAAxkBAAEB_6xgvLmeBCAzjMVESVSvAXy5GFadZQACUAEAAj9n6UWess0Kxb4TQh8E")
    await message.reply_text(
        f"""`Hi` {message.from_user.first_name}!
\n`This is a VC Music Bot which can play music in your group's Voice Chat.`
`Powered By` @Tc_Bots 
\n`To get started simply add me to your group and make me admin. Also do not forget to add my assistant bot` @TcPlayer `to your group`.
\n`Hit` /help `list of available commands.`
""",
      
       
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Cʀᴇᴅɪᴛ", url="https://t.me/TcSupport",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Gʀᴏᴜᴘ", url="https://t.me/Tcbotsbugs"
                    ),
                    InlineKeyboardButton(
                        "Cʜᴀɴɴᴇʟ", url="https://t.me/tc_bots"
                    ),
                    InlineKeyboardButton(
                        "Sᴏᴜʀᴄᴇ", url="https://github.com/tcbots/TcPlayer"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Aᴅᴅ Mᴇ", url="https://t.me/TcPlayerBot?startgroup=true"
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
        "💁🏻‍♂️ Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Cʜᴀɴɴᴇʟ", url="https://t.me/tc_bots"
                    ),
                    InlineKeyboardButton(
                        "Gʀᴏᴜᴘ", url="https://t.me/tcbotsbugs"
                    )
                ],    
                [    
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
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
