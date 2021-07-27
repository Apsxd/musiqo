#unitedbots #callsmusic #psychobots
from callsmusic.callsmusic import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,"[✨](https://telegra.ph/file/c6c36a4bcecef600fd9be.jpg) Heya! This is the Music Assistant of [Musiqo](https://t.me/MusiqoRobot) Ask at @Unitedbotsupport")
  return                        
