import os
import sys
import asyncio
import re
from random import choice
from SpamX import (RiZoeL, RiZoeL2, RiZoeL3, RiZoeL4, RiZoeL5, 
                RiZoeL6, RiZoeL7, RiZoeL8, RiZoeL9, RiZoeL10, 
                RiZoeL11, RiZoeL12, RiZoeL13, RiZoeL14, RiZoeL15, 
                RiZoeL16, RiZoeL17, RiZoeL18, RiZoeL19, RiZoeL20, HNDLR,
                SUDO_USERS)
from pyrogram import Client, filters
from pyrogram.types import Message
from SpamX.data import *


@RiZoeL.on_message(filters.user(SUDO_USERS) & filters.command(["spam"], prefixes=HNDLR))
@RiZoeL2.on_message(filters.user(SUDO_USERS) & filters.command(["spam"], prefixes=HNDLR))
@RiZoeL3.on_message(filters.user(SUDO_USERS) & filters.command(["spam"], prefixes=HNDLR))
@RiZoeL4.on_message(filters.user(SUDO_USERS) & filters.command(["spam"], prefixes=HNDLR))
@RiZoeL5.on_message(filters.user(SUDO_USERS) & filters.command(["spam"], prefixes=HNDLR))
@RiZoeL6.on_message(filters.user(SUDO_USERS) & filters.command(["spam"], prefixes=HNDLR))
@RiZoeL7.on_message(filters.user(SUDO_USERS) & filters.command(["spam"], prefixes=HNDLR))
@RiZoeL8.on_message(filters.user(SUDO_USERS) & filters.command(["spam"], prefixes=HNDLR))
@RiZoeL9.on_message(filters.user(SUDO_USERS) & filters.command(["spam"], prefixes=HNDLR))
@RiZoeL10.on_message(filters.user(SUDO_USERS) & filters.command(["spam"], prefixes=HNDLR))
@RiZoeL11.on_message(filters.user(SUDO_USERS) & filters.command(["spam"], prefixes=HNDLR))
@RiZoeL12.on_message(filters.user(SUDO_USERS) & filters.command(["spam"], prefixes=HNDLR))
@RiZoeL13.on_message(filters.user(SUDO_USERS) & filters.command(["spam"], prefixes=HNDLR))
@RiZoeL14.on_message(filters.user(SUDO_USERS) & filters.command(["spam"], prefixes=HNDLR))
@RiZoeL15.on_message(filters.user(SUDO_USERS) & filters.command(["spam"], prefixes=HNDLR))
@RiZoeL16.on_message(filters.user(SUDO_USERS) & filters.command(["spam"], prefixes=HNDLR))
@RiZoeL17.on_message(filters.user(SUDO_USERS) & filters.command(["spam"], prefixes=HNDLR))
@RiZoeL18.on_message(filters.user(SUDO_USERS) & filters.command(["spam"], prefixes=HNDLR))
@RiZoeL19.on_message(filters.user(SUDO_USERS) & filters.command(["spam"], prefixes=HNDLR))
@RiZoeL20.on_message(filters.user(SUDO_USERS) & filters.command(["spam"], prefixes=HNDLR))
async def spam(_, e: Message): 
    count = e.command[1]
    if int(e.chat.id) in GROUP:
         return await e.reply_text("**Sorry !! i Can't Spam Here.**")
    txt = ' '.join(e.command[2:])
    if re.search(Owners.lower(), msg.lower()):
         return await e.reply("**Sorry !!** I can't Spam On @RiZoeLX's owner")
    counts = int(count)
    msg = str(txt)
    if e.reply_to_message:
        reply_to_id = e.reply_to_message.message_id
        for _ in range(counts):
            await e.send_message(e.chat.id, msg, reply_to_message_id=reply_to_id)
            await asyncio.sleep(0.10)
        return
    for _ in range(counts):
        await e.send_message(e.chat.id, msg)
        await asyncio.sleep(0.10)

@RiZoeL.on_message(filters.user(SUDO_USERS) & filters.command(["delayspam"], prefixes=HNDLR))
@RiZoeL2.on_message(filters.user(SUDO_USERS) & filters.command(["delayspam"], prefixes=HNDLR))
@RiZoeL3.on_message(filters.user(SUDO_USERS) & filters.command(["delayspam"], prefixes=HNDLR))
@RiZoeL4.on_message(filters.user(SUDO_USERS) & filters.command(["delayspam"], prefixes=HNDLR))
@RiZoeL5.on_message(filters.user(SUDO_USERS) & filters.command(["delayspam"], prefixes=HNDLR))
@RiZoeL6.on_message(filters.user(SUDO_USERS) & filters.command(["delayspam"], prefixes=HNDLR))
@RiZoeL7.on_message(filters.user(SUDO_USERS) & filters.command(["delayspam"], prefixes=HNDLR))
@RiZoeL8.on_message(filters.user(SUDO_USERS) & filters.command(["delayspam"], prefixes=HNDLR))
@RiZoeL9.on_message(filters.user(SUDO_USERS) & filters.command(["delayspam"], prefixes=HNDLR))
@RiZoeL10.on_message(filters.user(SUDO_USERS) & filters.command(["delayspam"], prefixes=HNDLR))
@RiZoeL11.on_message(filters.user(SUDO_USERS) & filters.command(["delayspam"], prefixes=HNDLR))
@RiZoeL12.on_message(filters.user(SUDO_USERS) & filters.command(["delayspam"], prefixes=HNDLR))
@RiZoeL13.on_message(filters.user(SUDO_USERS) & filters.command(["delayspam"], prefixes=HNDLR))
@RiZoeL14.on_message(filters.user(SUDO_USERS) & filters.command(["delayspam"], prefixes=HNDLR))
@RiZoeL15.on_message(filters.user(SUDO_USERS) & filters.command(["delayspam"], prefixes=HNDLR))
@RiZoeL16.on_message(filters.user(SUDO_USERS) & filters.command(["delayspam"], prefixes=HNDLR))
@RiZoeL17.on_message(filters.user(SUDO_USERS) & filters.command(["delayspam"], prefixes=HNDLR))
@RiZoeL18.on_message(filters.user(SUDO_USERS) & filters.command(["delayspam"], prefixes=HNDLR))
@RiZoeL19.on_message(filters.user(SUDO_USERS) & filters.command(["delayspam"], prefixes=HNDLR))
@RiZoeL20.on_message(filters.user(SUDO_USERS) & filters.command(["delayspam"], prefixes=HNDLR))
async def delayspam(_, e: Message):
   usage = f"**Module Name: Delay Spam** \n\n Command: {HNDLR}delayspam <delay> <counts> <message for spam or reply to message>"
    Rizoel = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
    Rizoelop = Rizoel[1:]
    if len(Rizoelop) == 2:
       counts = int(Rizoelop[0])
       if int(e.chat.id) in GROUP:
            return await e.reply_text("**Sorry !! i Can't Spam Here.**")
       msg = str(Rizoelop[1])
       if re.search(Owners.lower(), msg.lower()):
            return await e.reply("**Sorry !!** I can't Spam On @RiZoeLX's owner")
       sleeptime = float(Rizoel[0])
       if e.reply_to_message:
          reply_to_id = e.reply_to_message.message_id
          for _ in range(counts):
              await e.send_message(e.chat.id, msg, reply_to_message_id=reply_to_id)
              await asyncio.sleep(sleeptime)
          return
       for _ in range(counts):
           await e.send_message(e.chat.id, msg)
           await asyncio.sleep(sleeptime)
    else:
        await e.reply_text(usage)   


@RiZoeL.on_message(filters.user(SUDO_USERS) & filters.command(["pornspam"], prefixes=HNDLR))
@RiZoeL2.on_message(filters.user(SUDO_USERS) & filters.command(["pornspam"], prefixes=HNDLR))
@RiZoeL3.on_message(filters.user(SUDO_USERS) & filters.command(["pornspam"], prefixes=HNDLR))
@RiZoeL4.on_message(filters.user(SUDO_USERS) & filters.command(["pornspam"], prefixes=HNDLR))
@RiZoeL5.on_message(filters.user(SUDO_USERS) & filters.command(["pornspam"], prefixes=HNDLR))
@RiZoeL6.on_message(filters.user(SUDO_USERS) & filters.command(["pornspam"], prefixes=HNDLR))
@RiZoeL7.on_message(filters.user(SUDO_USERS) & filters.command(["pornspam"], prefixes=HNDLR))
@RiZoeL8.on_message(filters.user(SUDO_USERS) & filters.command(["pornspam"], prefixes=HNDLR))
@RiZoeL9.on_message(filters.user(SUDO_USERS) & filters.command(["pornspam"], prefixes=HNDLR))
@RiZoeL10.on_message(filters.user(SUDO_USERS) & filters.command(["pornspam"], prefixes=HNDLR))
@RiZoeL11.on_message(filters.user(SUDO_USERS) & filters.command(["pornspam"], prefixes=HNDLR))
@RiZoeL12.on_message(filters.user(SUDO_USERS) & filters.command(["pornspam"], prefixes=HNDLR))
@RiZoeL13.on_message(filters.user(SUDO_USERS) & filters.command(["pornspam"], prefixes=HNDLR))
@RiZoeL14.on_message(filters.user(SUDO_USERS) & filters.command(["pornspam"], prefixes=HNDLR))
@RiZoeL15.on_message(filters.user(SUDO_USERS) & filters.command(["pornspam"], prefixes=HNDLR))
@RiZoeL16.on_message(filters.user(SUDO_USERS) & filters.command(["pornspam"], prefixes=HNDLR))
@RiZoeL17.on_message(filters.user(SUDO_USERS) & filters.command(["pornspam"], prefixes=HNDLR))
@RiZoeL18.on_message(filters.user(SUDO_USERS) & filters.command(["pornspam"], prefixes=HNDLR))
@RiZoeL19.on_message(filters.user(SUDO_USERS) & filters.command(["pornspam"], prefixes=HNDLR))
@RiZoeL20.on_message(filters.user(SUDO_USERS) & filters.command(["pornspam"], prefixes=HNDLR))
async def pornspam(_, e: Message): 
    counts = e.command[1]
    if int(e.chat.id) in GROUP:
         return await e.reply_text("**Sorry !! i Can't Spam Here.**")
    porno = choice(PORM)
    rizoel = "**#Pornspam**"
    for _ in range(counts):
         if ".jpg" in porno or ".png" in porno:
              await e.send_photo(e.chat.id, porn, caption=rizoel)
              await asyncio.sleep(0.4)
         if ".mp4" in porno or ".MP4," in porno:
              await e.send_video(e.chat.id, porno, caption=rizoel)
              await asyncio.sleep(0.4)


@RiZoeL.on_message(filters.user(SUDO_USERS) & filters.command(["raid"], prefixes=HNDLR))
@RiZoeL2.on_message(filters.user(SUDO_USERS) & filters.command(["raid"], prefixes=HNDLR))
@RiZoeL3.on_message(filters.user(SUDO_USERS) & filters.command(["raid"], prefixes=HNDLR))
@RiZoeL4.on_message(filters.user(SUDO_USERS) & filters.command(["raid"], prefixes=HNDLR))
@RiZoeL5.on_message(filters.user(SUDO_USERS) & filters.command(["raid"], prefixes=HNDLR))
@RiZoeL6.on_message(filters.user(SUDO_USERS) & filters.command(["raid"], prefixes=HNDLR))
@RiZoeL7.on_message(filters.user(SUDO_USERS) & filters.command(["raid"], prefixes=HNDLR))
@RiZoeL8.on_message(filters.user(SUDO_USERS) & filters.command(["raid"], prefixes=HNDLR))
@RiZoeL9.on_message(filters.user(SUDO_USERS) & filters.command(["raid"], prefixes=HNDLR))
@RiZoeL10.on_message(filters.user(SUDO_USERS) & filters.command(["raid"], prefixes=HNDLR))
@RiZoeL11.on_message(filters.user(SUDO_USERS) & filters.command(["raid"], prefixes=HNDLR))
@RiZoeL12.on_message(filters.user(SUDO_USERS) & filters.command(["raid"], prefixes=HNDLR))
@RiZoeL13.on_message(filters.user(SUDO_USERS) & filters.command(["raid"], prefixes=HNDLR))
@RiZoeL14.on_message(filters.user(SUDO_USERS) & filters.command(["raid"], prefixes=HNDLR))
@RiZoeL15.on_message(filters.user(SUDO_USERS) & filters.command(["raid"], prefixes=HNDLR))
@RiZoeL16.on_message(filters.user(SUDO_USERS) & filters.command(["raid"], prefixes=HNDLR))
@RiZoeL17.on_message(filters.user(SUDO_USERS) & filters.command(["raid"], prefixes=HNDLR))
@RiZoeL18.on_message(filters.user(SUDO_USERS) & filters.command(["raid"], prefixes=HNDLR))
@RiZoeL19.on_message(filters.user(SUDO_USERS) & filters.command(["raid"], prefixes=HNDLR))
@RiZoeL20.on_message(filters.user(SUDO_USERS) & filters.command(["raid"], prefixes=HNDLR))
async def raid(_, e: Message): 
      Usage = f"**Module Name: Raid** \n\n Command: {HNDLR}raid <count> <username or User id>"
      Rizoel = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
      if len(Rizoel) == 2:
          counts = int(Rizoel[0])
          if int(e.chat.id) in GROUP:
               return await e.reply_text("**Sorry !! i Can't Spam Here.**")
          xd = str(Rizoel[1])
          ok = await e.get_users(xd)
          id = ok.id
          if int(id) in RiZoeLX:
                text = f"I can't raid on @RiZoeLX's Owner"
                await e.reply(text)
          elif int(id) == OWNER_ID:
                text = f"This guy is Owner Of this Bots."
                await e.reply(text)
          elif int(id) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply(text)
          else:
              fname = ok.first_name
              mention = f"[{fname}](tg://user?id={id})"
              for _ in range(counts):
                    reply = choice(RAID)
                    msg = f"{mention} {reply}"
                    await e.send_message(e.chat.id, msg)
                    await asyncio.sleep(0.10)
      elif e.reply_to_message:
          msg_id = e.reply_to_message.message_id
          counts = int(Rizoel[0])
          if int(e.chat.id) in GROUP:
               return await e.reply_text("**Sorry !! i Can't Spam Here.**")
          RiZoeL = e.get_messages(e.chat.id, msg_id)
          ok = await e.get_users(RiZoeL.from_user.id)
          id = ok.id
          if int(id) in RiZoeLX:
                text = f"I can't raid on @RiZoeLX's Owner"
                await e.reply(text)
          elif int(id) == OWNER_ID:
                text = f"This guy is Owner Of this Bots."
                await e.reply(text)
          elif int(id) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply(text)
          else:
              fname = ok.first_name
              mention = f"[{fname}](tg://user?id={id})"
              for _ in range(counts):
                    reply = choice(RAID)
                    msg = f"{mention} {reply}"
                    await e.send_message(e.chat.id, msg)
                    await asyncio.sleep(0.10)
      else:
          await e.reply(Usage)
