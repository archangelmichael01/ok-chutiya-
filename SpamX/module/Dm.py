import os
import sys
import asyncio
from random import choice
from SpamX import (RiZoeL1, RiZoeL2, RiZoeL3, RiZoeL4, RiZoeL5, 
                RiZoeL6, RiZoeL7, RiZoeL8, RiZoeL9, RiZoeL10, 
                RiZoeL11, RiZoeL12, RiZoeL13, RiZoeL14, RiZoeL15, 
                RiZoeL16, RiZoeL17, RiZoeL18, RiZoeL19, RiZoeL20, HNDLR,
                SUDO_USERS)
from pyrogram import Client, filters
from pyrogram.types import Message
from SpamX.data import *


@RiZoeL.on_message(filters.user(SUDO_USERS) & filters.command(["dmraid"], prefixes=HNDLR))
@RiZoeL2.on_message(filters.user(SUDO_USERS) & filters.command(["dmraid"], prefixes=HNDLR))
@RiZoeL3.on_message(filters.user(SUDO_USERS) & filters.command(["dmraid"], prefixes=HNDLR))
@RiZoeL4.on_message(filters.user(SUDO_USERS) & filters.command(["dmraid"], prefixes=HNDLR))
@RiZoeL5.on_message(filters.user(SUDO_USERS) & filters.command(["dmraid"], prefixes=HNDLR))
@RiZoeL6.on_message(filters.user(SUDO_USERS) & filters.command(["dmraid"], prefixes=HNDLR))
@RiZoeL7.on_message(filters.user(SUDO_USERS) & filters.command(["dmraid"], prefixes=HNDLR))
@RiZoeL8.on_message(filters.user(SUDO_USERS) & filters.command(["dmraid"], prefixes=HNDLR))
@RiZoeL9.on_message(filters.user(SUDO_USERS) & filters.command(["dmraid"], prefixes=HNDLR))
@RiZoeL10.on_message(filters.user(SUDO_USERS) & filters.command(["dmraid"], prefixes=HNDLR))
@RiZoeL11.on_message(filters.user(SUDO_USERS) & filters.command(["dmraid"], prefixes=HNDLR))
@RiZoeL12.on_message(filters.user(SUDO_USERS) & filters.command(["dmraid"], prefixes=HNDLR))
@RiZoeL13.on_message(filters.user(SUDO_USERS) & filters.command(["dmraid"], prefixes=HNDLR))
@RiZoeL14.on_message(filters.user(SUDO_USERS) & filters.command(["dmraid"], prefixes=HNDLR))
@RiZoeL15.on_message(filters.user(SUDO_USERS) & filters.command(["dmraid"], prefixes=HNDLR))
@RiZoeL16.on_message(filters.user(SUDO_USERS) & filters.command(["dmraid"], prefixes=HNDLR))
@RiZoeL17.on_message(filters.user(SUDO_USERS) & filters.command(["dmraid"], prefixes=HNDLR))
@RiZoeL18.on_message(filters.user(SUDO_USERS) & filters.command(["dmraid"], prefixes=HNDLR))
@RiZoeL19.on_message(filters.user(SUDO_USERS) & filters.command(["dmraid"], prefixes=HNDLR))
@RiZoeL20.on_message(filters.user(SUDO_USERS) & filters.command(["dmraid"], prefixes=HNDLR))
async def dmraid(_, e: Message): 
      Usage = f"**Module Name: dmraid** \n\n Command: {HNDLR}dmraid <count> <username or User id>"
      Rizoel = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
      if len(Rizoel) == 2:
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
              counts = int(Rizoel[0])
              await e.reply_text("⚜️ Dm Raid Strated Successfully ⚜️")
              for _ in range(counts):
                    reply = choice(RAID)
                    msg = f"{reply}"
                    await e.send_message(id, msg)
                    await asyncio.sleep(0.10)
      elif e.reply_to_message:
          msg_id = e.reply_to_message.message_id
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
              counts = int(Rizoel[0])
              await e.reply_text("⚜️ Dm Raid Strated Successfully ⚜️")
              for _ in range(counts):
                    reply = choice(RAID)
                    msg = f"{reply}"
                    await e.send_message(id, msg)
                    await asyncio.sleep(0.10)
      else:
          await e.reply(Usage)
 
         
@RiZoeL.on_message(filters.user(SUDO_USERS) & filters.command(["dm"], prefixes=HNDLR))
@RiZoeL2.on_message(filters.user(SUDO_USERS) & filters.command(["dm"], prefixes=HNDLR))
@RiZoeL3.on_message(filters.user(SUDO_USERS) & filters.command(["dm"], prefixes=HNDLR))
@RiZoeL4.on_message(filters.user(SUDO_USERS) & filters.command(["dm"], prefixes=HNDLR))
@RiZoeL5.on_message(filters.user(SUDO_USERS) & filters.command(["dm"], prefixes=HNDLR))
@RiZoeL6.on_message(filters.user(SUDO_USERS) & filters.command(["dm"], prefixes=HNDLR))
@RiZoeL7.on_message(filters.user(SUDO_USERS) & filters.command(["dm"], prefixes=HNDLR))
@RiZoeL8.on_message(filters.user(SUDO_USERS) & filters.command(["dm"], prefixes=HNDLR))
@RiZoeL9.on_message(filters.user(SUDO_USERS) & filters.command(["dm"], prefixes=HNDLR))
@RiZoeL10.on_message(filters.user(SUDO_USERS) & filters.command(["dm"], prefixes=HNDLR))
@RiZoeL11.on_message(filters.user(SUDO_USERS) & filters.command(["dm"], prefixes=HNDLR))
@RiZoeL12.on_message(filters.user(SUDO_USERS) & filters.command(["dm"], prefixes=HNDLR))
@RiZoeL13.on_message(filters.user(SUDO_USERS) & filters.command(["dm"], prefixes=HNDLR))
@RiZoeL14.on_message(filters.user(SUDO_USERS) & filters.command(["dm"], prefixes=HNDLR))
@RiZoeL15.on_message(filters.user(SUDO_USERS) & filters.command(["dm"], prefixes=HNDLR))
@RiZoeL16.on_message(filters.user(SUDO_USERS) & filters.command(["dm"], prefixes=HNDLR))
@RiZoeL17.on_message(filters.user(SUDO_USERS) & filters.command(["dm"], prefixes=HNDLR))
@RiZoeL18.on_message(filters.user(SUDO_USERS) & filters.command(["dm"], prefixes=HNDLR))
@RiZoeL19.on_message(filters.user(SUDO_USERS) & filters.command(["dm"], prefixes=HNDLR))
@RiZoeL20.on_message(filters.user(SUDO_USERS) & filters.command(["dm"], prefixes=HNDLR))
async def dm(_, e: Message):
      Usage = f"**Module Name: dmraid** \n\n Command: {HNDLR}dm <username or User id> <message>"
      Rizoel = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
      if len(Rizoel) == 2:
          xd = str(Rizoel[0])
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
              msg = str(Rizoel[1])
              await e.reply_text("🔸 Message Delivered 🔸")
              for _ in range(counts):
                    await e.send_message(id, msg)
                    await asyncio.sleep(0.10)
      elif e.reply_to_message:
          msg_id = e.reply_to_message.message_id
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
              msg = int(Rizoel[0])
              await e.reply_text("🔸 Message Delivered 🔸️")
              for _ in range(counts):
                    await e.send_message(id, msg)
                    await asyncio.sleep(0.10)
      else:
          await e.reply(Usage)




@RiZoeL.on_message(filters.user(SUDO_USERS) & filters.command(["dmspam"], prefixes=HNDLR))
@RiZoeL2.on_message(filters.user(SUDO_USERS) & filters.command(["dmspam"], prefixes=HNDLR))
@RiZoeL3.on_message(filters.user(SUDO_USERS) & filters.command(["dmspam"], prefixes=HNDLR))
@RiZoeL4.on_message(filters.user(SUDO_USERS) & filters.command(["dmspam"], prefixes=HNDLR))
@RiZoeL5.on_message(filters.user(SUDO_USERS) & filters.command(["dmspam"], prefixes=HNDLR))
@RiZoeL6.on_message(filters.user(SUDO_USERS) & filters.command(["dmspam"], prefixes=HNDLR))
@RiZoeL7.on_message(filters.user(SUDO_USERS) & filters.command(["dmspam"], prefixes=HNDLR))
@RiZoeL8.on_message(filters.user(SUDO_USERS) & filters.command(["dmspam"], prefixes=HNDLR))
@RiZoeL9.on_message(filters.user(SUDO_USERS) & filters.command(["dmspam"], prefixes=HNDLR))
@RiZoeL10.on_message(filters.user(SUDO_USERS) & filters.command(["dmspam"], prefixes=HNDLR))
@RiZoeL11.on_message(filters.user(SUDO_USERS) & filters.command(["dmspam"], prefixes=HNDLR))
@RiZoeL12.on_message(filters.user(SUDO_USERS) & filters.command(["dmspam"], prefixes=HNDLR))
@RiZoeL13.on_message(filters.user(SUDO_USERS) & filters.command(["dmspam"], prefixes=HNDLR))
@RiZoeL14.on_message(filters.user(SUDO_USERS) & filters.command(["dmspam"], prefixes=HNDLR))
@RiZoeL15.on_message(filters.user(SUDO_USERS) & filters.command(["dmspam"], prefixes=HNDLR))
@RiZoeL16.on_message(filters.user(SUDO_USERS) & filters.command(["dmspam"], prefixes=HNDLR))
@RiZoeL17.on_message(filters.user(SUDO_USERS) & filters.command(["dmspam"], prefixes=HNDLR))
@RiZoeL18.on_message(filters.user(SUDO_USERS) & filters.command(["dmspam"], prefixes=HNDLR))
@RiZoeL19.on_message(filters.user(SUDO_USERS) & filters.command(["dmspam"], prefixes=HNDLR))
@RiZoeL20.on_message(filters.user(SUDO_USERS) & filters.command(["dmspam"], prefixes=HNDLR))
async def dmspam(_, e: Message):
      Usage = f"**Module Name: dmraid** \n\n Command: {HNDLR}dmspam <username or User id> <count> <message>"
      Rizoel = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
      Rizoelop = Rizoel[1:]
      if len(Rizoelop) == 2:
          msg = str(Rizoelop[1])
          xd = str(Rizoel[0])
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
              counts = int(Rizoelop[0])
              await e.reply_text("☢️ Dm Spam Strated ☢️")
              for _ in range(counts):
                    await e.send_message(id, msg)
                    await asyncio.sleep(0.10)
      elif e.reply_to_message:
          msg_id = e.reply_to_message.message_id
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
              counts = int(Rizoel[0])
              msg = str(Rizoelop[0])
              await e.reply_text("☢️ Dm Spam Strated ☢️")
              for _ in range(counts):
                    await e.send_message(id, msg)
                    await asyncio.sleep(0.10)
      else:
          await e.reply(Usage)