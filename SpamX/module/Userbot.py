
import os
import sys
import asyncio
import datetime
import time
from pyrogram import __version__ as pyro_vr
from SpamX import (RiZoeL1, RiZoeL2, RiZoeL3, RiZoeL4, RiZoeL5, 
                RiZoeL6, RiZoeL7, RiZoeL8, RiZoeL9, RiZoeL10, 
                RiZoeL11, RiZoeL12, RiZoeL13, RiZoeL14, RiZoeL15, 
                RiZoeL16, RiZoeL17, RiZoeL18, RiZoeL19, RiZoeL20, HNDLR,
                SUDO_USERS, ALIVE_PIC, ALIVE_MSG, PING_MSG, __version__)
from pyrogram import Client, filters
from pyrogram.types import Message
                
                

pongg = PING_MSG if PING_MSG else "ʀɪᴢᴏᴇʟ X sᴘᴀᴍ"
RIZ_PIC = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/ba87c58f01a6fcb5ef512.jpg"
Alivemsg = ALIVE_MSG if ALIVE_MSG else "𝗥𝗶𝗭𝗼𝗲𝗟 𝗫 𝗦𝗽𝗮𝗺 𝗛𝗲𝗿𝗲."


rizoel = f"✧ {Alivemsg} ✧\n\n"
rizoel += f"════════════════════\n"
rizoel += f"► **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `3.10.4`\n"
rizoel += f"► **ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ** : `{pyro_vr}`\n"
rizoel += f"► **ʀɪᴢᴏᴇʟXsᴘᴀᴍ ᴠᴇʀsɪᴏɴ**  : `{__version__}`\n"
rizoel += f"► **ᴄʜᴀɴɴᴇʟ** : [Join.](https://t.me/RiZoeLX)\n"
rizoel += f"════════════════════\n\n"
rizoel += f"► **Source Code:** [•Repo•](https://github.com/RiZoeLX/SpamX)"


async def get_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]
    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    hmm = len(time_list)
    for x in range(hmm):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "
    time_list.reverse()
    up_time += ":".join(time_list)
    return up_time


@RiZoeL.on_message(filters.user(SUDO_USERS) & filters.command(["ping"], prefixes=HNDLR))
@RiZoeL2.on_message(filters.user(SUDO_USERS) & filters.command(["ping"], prefixes=HNDLR))
@RiZoeL3.on_message(filters.user(SUDO_USERS) & filters.command(["ping"], prefixes=HNDLR))
@RiZoeL4.on_message(filters.user(SUDO_USERS) & filters.command(["ping"], prefixes=HNDLR))
@RiZoeL5.on_message(filters.user(SUDO_USERS) & filters.command(["ping"], prefixes=HNDLR))
@RiZoeL6.on_message(filters.user(SUDO_USERS) & filters.command(["ping"], prefixes=HNDLR))
@RiZoeL7.on_message(filters.user(SUDO_USERS) & filters.command(["ping"], prefixes=HNDLR))
@RiZoeL8.on_message(filters.user(SUDO_USERS) & filters.command(["ping"], prefixes=HNDLR))
@RiZoeL9.on_message(filters.user(SUDO_USERS) & filters.command(["ping"], prefixes=HNDLR))
@RiZoeL10.on_message(filters.user(SUDO_USERS) & filters.command(["ping"], prefixes=HNDLR))
@RiZoeL11.on_message(filters.user(SUDO_USERS) & filters.command(["ping"], prefixes=HNDLR))
@RiZoeL12.on_message(filters.user(SUDO_USERS) & filters.command(["ping"], prefixes=HNDLR))
@RiZoeL13.on_message(filters.user(SUDO_USERS) & filters.command(["ping"], prefixes=HNDLR))
@RiZoeL14.on_message(filters.user(SUDO_USERS) & filters.command(["ping"], prefixes=HNDLR))
@RiZoeL15.on_message(filters.user(SUDO_USERS) & filters.command(["ping"], prefixes=HNDLR))
@RiZoeL16.on_message(filters.user(SUDO_USERS) & filters.command(["ping"], prefixes=HNDLR))
@RiZoeL17.on_message(filters.user(SUDO_USERS) & filters.command(["ping"], prefixes=HNDLR))
@RiZoeL18.on_message(filters.user(SUDO_USERS) & filters.command(["ping"], prefixes=HNDLR))
@RiZoeL19.on_message(filters.user(SUDO_USERS) & filters.command(["ping"], prefixes=HNDLR))
@RiZoeL20.on_message(filters.user(SUDO_USERS) & filters.command(["ping"], prefixes=HNDLR))
async def ping(_, e: Message):       
      start = datetime.datetime.now()
      uptime = await get_time((time.time() - start_time))
      Fuk = await e.reply_text("**Pong !!**")
      end = datetime.datetime.now()
      ms = (end-start).microseconds / 1000
      await Fuk.edit_text(f"⌾ {pongg} ⌾ \n\n ༝ ᴘɪɴɢ: `{ms}` ᴍs \n ༝ ᴜᴘᴛɪᴍᴇ: `{uptime}` \n ༝ ᴠᴇʀsɪᴏɴ: `{__version__}`")




@RiZoeL.on_message(filters.user(SUDO_USERS) & filters.command(["alive"], prefixes=HNDLR))
@RiZoeL2.on_message(filters.user(SUDO_USERS) & filters.command(["alive"], prefixes=HNDLR))
@RiZoeL3.on_message(filters.user(SUDO_USERS) & filters.command(["alive"], prefixes=HNDLR))
@RiZoeL4.on_message(filters.user(SUDO_USERS) & filters.command(["alive"], prefixes=HNDLR))
@RiZoeL5.on_message(filters.user(SUDO_USERS) & filters.command(["alive"], prefixes=HNDLR))
@RiZoeL6.on_message(filters.user(SUDO_USERS) & filters.command(["alive"], prefixes=HNDLR))
@RiZoeL7.on_message(filters.user(SUDO_USERS) & filters.command(["alive"], prefixes=HNDLR))
@RiZoeL8.on_message(filters.user(SUDO_USERS) & filters.command(["alive"], prefixes=HNDLR))
@RiZoeL9.on_message(filters.user(SUDO_USERS) & filters.command(["alive"], prefixes=HNDLR))
@RiZoeL10.on_message(filters.user(SUDO_USERS) & filters.command(["alive"], prefixes=HNDLR))
@RiZoeL11.on_message(filters.user(SUDO_USERS) & filters.command(["alive"], prefixes=HNDLR))
@RiZoeL12.on_message(filters.user(SUDO_USERS) & filters.command(["alive"], prefixes=HNDLR))
@RiZoeL13.on_message(filters.user(SUDO_USERS) & filters.command(["alive"], prefixes=HNDLR))
@RiZoeL14.on_message(filters.user(SUDO_USERS) & filters.command(["alive"], prefixes=HNDLR))
@RiZoeL15.on_message(filters.user(SUDO_USERS) & filters.command(["alive"], prefixes=HNDLR))
@RiZoeL16.on_message(filters.user(SUDO_USERS) & filters.command(["alive"], prefixes=HNDLR))
@RiZoeL17.on_message(filters.user(SUDO_USERS) & filters.command(["alive"], prefixes=HNDLR))
@RiZoeL18.on_message(filters.user(SUDO_USERS) & filters.command(["alive"], prefixes=HNDLR))
@RiZoeL19.on_message(filters.user(SUDO_USERS) & filters.command(["alive"], prefixes=HNDLR))
@RiZoeL20.on_message(filters.user(SUDO_USERS) & filters.command(["alive"], prefixes=HNDLR))
async def alive(_, e: Message):
      if ".jpg" in RIZ_PIC or ".png" in RIZ_PIC:
             await e.send_photo(e.chat.id, RIZ_PIC, caption=rizoel)
      if ".mp4" in RIZ_PIC or ".MP4," in RIZ_PIC:
             await e.send_video(e.chat.id, RIZ_PIC, caption=rizoel)
             






             
