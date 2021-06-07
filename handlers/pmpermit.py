from callsmusic.callsmusic import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,"✨ Hey ! This is the Music Assistant of @TcPlayerBot !!✨.\n\n ❗️ Rules:\n   - ⚠ No Chatting or Spam Allowed ⚠\n\n 👉 **ℹ️ Send Group Invite Link if Userbot Can't Join Your Group or Contact @TcBotsBugs**")
  return                        
