from callsmusic.callsmusic import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,"[✨](https://telegra.ph/file/f6fad124b1ffd3cf8eefb.png) Heya! This is the Music Assistant of [Musiqo](https://t.me/BlissMusicRobot)")
  return                        
