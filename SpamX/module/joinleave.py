
from SpamX import (RiZoeL1, RiZoeL2, RiZoeL3, RiZoeL4, RiZoeL5, 
                RiZoeL6, RiZoeL7, RiZoeL8, RiZoeL9, RiZoeL10, 
                RiZoeL11, RiZoeL12, RiZoeL13, RiZoeL14, RiZoeL15, 
                RiZoeL16, RiZoeL17, RiZoeL18, RiZoeL19, RiZoeL20, HNDLR,
                SUDO_USERS)
from pyrogram import Client, filters
from pyrogram.types import Message


@RiZoeL.on_message(filters.user(SUDO_USERS) & filters.command(["join"], prefixes=HNDLR))
@RiZoeL2.on_message(filters.user(SUDO_USERS) & filters.command(["join"], prefixes=HNDLR))
@RiZoeL3.on_message(filters.user(SUDO_USERS) & filters.command(["join"], prefixes=HNDLR))
@RiZoeL4.on_message(filters.user(SUDO_USERS) & filters.command(["join"], prefixes=HNDLR))
@RiZoeL5.on_message(filters.user(SUDO_USERS) & filters.command(["join"], prefixes=HNDLR))
@RiZoeL6.on_message(filters.user(SUDO_USERS) & filters.command(["join"], prefixes=HNDLR))
@RiZoeL7.on_message(filters.user(SUDO_USERS) & filters.command(["join"], prefixes=HNDLR))
@RiZoeL8.on_message(filters.user(SUDO_USERS) & filters.command(["join"], prefixes=HNDLR))
@RiZoeL9.on_message(filters.user(SUDO_USERS) & filters.command(["join"], prefixes=HNDLR))
@RiZoeL10.on_message(filters.user(SUDO_USERS) & filters.command(["join"], prefixes=HNDLR))
@RiZoeL11.on_message(filters.user(SUDO_USERS) & filters.command(["join"], prefixes=HNDLR))
@RiZoeL12.on_message(filters.user(SUDO_USERS) & filters.command(["join"], prefixes=HNDLR))
@RiZoeL13.on_message(filters.user(SUDO_USERS) & filters.command(["join"], prefixes=HNDLR))
@RiZoeL14.on_message(filters.user(SUDO_USERS) & filters.command(["join"], prefixes=HNDLR))
@RiZoeL15.on_message(filters.user(SUDO_USERS) & filters.command(["join"], prefixes=HNDLR))
@RiZoeL16.on_message(filters.user(SUDO_USERS) & filters.command(["join"], prefixes=HNDLR))
@RiZoeL17.on_message(filters.user(SUDO_USERS) & filters.command(["join"], prefixes=HNDLR))
@RiZoeL18.on_message(filters.user(SUDO_USERS) & filters.command(["join"], prefixes=HNDLR))
@RiZoeL19.on_message(filters.user(SUDO_USERS) & filters.command(["join"], prefixes=HNDLR))
@RiZoeL20.on_message(filters.user(SUDO_USERS) & filters.command(["join"], prefixes=HNDLR))
async def join(_, e: Message): 
    chat = e.text[6:]
    if chat.isnumeric():
        return await e.reply_text("Can't join a chat with chat id. Give username or invite link."
    try:
      await e.join_chat(chat)
      await e.reply("**Join Successfully ✅ **")
    except Exception as ex:
        await e.reply_text(f"**ERROR:** \n\n{str(ex)}")

@RiZoeL.on_message(filters.user(SUDO_USERS) & filters.command(["leave"], prefixes=HNDLR))
@RiZoeL2.on_message(filters.user(SUDO_USERS) & filters.command(["leave"], prefixes=HNDLR))
@RiZoeL3.on_message(filters.user(SUDO_USERS) & filters.command(["leave"], prefixes=HNDLR))
@RiZoeL4.on_message(filters.user(SUDO_USERS) & filters.command(["leave"], prefixes=HNDLR))
@RiZoeL5.on_message(filters.user(SUDO_USERS) & filters.command(["leave"], prefixes=HNDLR))
@RiZoeL6.on_message(filters.user(SUDO_USERS) & filters.command(["leave"], prefixes=HNDLR))
@RiZoeL7.on_message(filters.user(SUDO_USERS) & filters.command(["leave"], prefixes=HNDLR))
@RiZoeL8.on_message(filters.user(SUDO_USERS) & filters.command(["leave"], prefixes=HNDLR))
@RiZoeL9.on_message(filters.user(SUDO_USERS) & filters.command(["leave"], prefixes=HNDLR))
@RiZoeL10.on_message(filters.user(SUDO_USERS) & filters.command(["leave"], prefixes=HNDLR))
@RiZoeL11.on_message(filters.user(SUDO_USERS) & filters.command(["leave"], prefixes=HNDLR))
@RiZoeL12.on_message(filters.user(SUDO_USERS) & filters.command(["leave"], prefixes=HNDLR))
@RiZoeL13.on_message(filters.user(SUDO_USERS) & filters.command(["leave"], prefixes=HNDLR))
@RiZoeL14.on_message(filters.user(SUDO_USERS) & filters.command(["leave"], prefixes=HNDLR))
@RiZoeL15.on_message(filters.user(SUDO_USERS) & filters.command(["leave"], prefixes=HNDLR))
@RiZoeL16.on_message(filters.user(SUDO_USERS) & filters.command(["leave"], prefixes=HNDLR))
@RiZoeL17.on_message(filters.user(SUDO_USERS) & filters.command(["leave"], prefixes=HNDLR))
@RiZoeL18.on_message(filters.user(SUDO_USERS) & filters.command(["leave"], prefixes=HNDLR))
@RiZoeL19.on_message(filters.user(SUDO_USERS) & filters.command(["leave"], prefixes=HNDLR))
@RiZoeL20.on_message(filters.user(SUDO_USERS) & filters.command(["leave"], prefixes=HNDLR))
async def leave(_, e: Message):
    rizoel = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
    if len(e.text) > 7:
        chat = rizoel[0]
        try:
           await e.leave_chat(chat)
           await e.reply("**Left Successfully ✅ **")
        except Exception as ex:
           await e.reply_text(f"**ERROR:** \n\n{str(ex)}")
    else:
        chat = e.chat.id
        if int(chat) == -1001321613309:
              return e.reply_text("**Error**")
        try:
           await e.leave_chat(chat)
           await e.reply("**Left Successfully ✅ **")
        except Exception as ex:
           await e.reply_text(f"**ERROR:** \n\n{str(ex)}")


