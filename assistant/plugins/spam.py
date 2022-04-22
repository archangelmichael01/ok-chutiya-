import os 
import asyncio
import random
import re
from telethon import events
from datetime import datetime
from resources.data import *
from telethon.tl import functions
from RiZoeLXSpam import OWNER_ID, hl, CLIENTS
from assistant import RiZoeL

SEND_GRP = "**Send Group Link Where You want to spam**"
SEND_COUNT ="**Send Counts**"
SEND_SPAM = "**Send spam message to spam**"
ABORT = "**All process Cancelled !**"

@RiZoeL.on(events.NewMessage(pattern="[!/]spam"))
async def spam(event):
  if event.sender_id in DEV or event.sender_id in SUDO_USERS:
     if event.is_group:
          return await event.reply("**Use This Cmd In PM**")
     async with RiZoeL.conversation(event.chat_id) as rizx:
        await rizx.send_message(SEND_GRP)
        response = rizx.wait_event(events.NewMessage(chats=event.chat_id))
        res = await response
        if "/cancel" in res.message.message:
            return await rizx.send_message(ABORT)
        grpp = res.message.message
        if grpp.startswith("@"):
              Group = grpp
              if re.search(GRP.lower(), Group.lower()):
                   return await rizx.send_message("Sorry !! I can't Spam there")
        elif grpp.startswith("https://t.me/"):
            hash = grpp.split('/t.me/')[1]
            Group = "@" + grpp
        else:
            await rizx.send_message("Error! Send Group link or Username")
            return
        await rizx.send_message(SEND_COUNT)
        response = rizx.wait_event(events.NewMessage(chats=event.chat_id))
        res = await response
        if "/cancel" in res.message.message:
            return await rizx.send_message(ABORT)
        Num = res.message.message
        if Num.isnumeric():
             count = int(Num)
        else:
            await rizx.send_message("Error! Send Count in Numbers")
            return
        await rizx.send_message(SEND_SPAM)
        response = rizx.wait_event(events.NewMessage(chats=event.chat_id))
        res = await response
        if "/cancel" in res.message.message:
            return await rizx.send_message(ABORT)
        message = res.message.message
        if re.search(TheRiZoeL.lower(), message.lower()):
                   return await rizx.send_message("Sorry !! I can't Spam On @RiZoeLX's Owner")
        Fukoff = await rizx.send_message(f"__Starting Spam In {Group}__")
        spam_text = f"{hl}gspam {count} {Group} {message}"
        join_text = f"{hl}join {Group}"
        async for sex in CLIENTS:
           try:
               await RiZoeL.send_message([sex], join_text)
               await asyncio.sleep(0.4)
               await RiZoeL.send_message([sex], spam_text)
           except Exception as ex:
               print(ex)
        await Fukoff.edit(f"**▪️Started Spam ▪️** \n\n__Group__ : `{Group}`\n__Spam Count__ : `{count}` \n__Spam Message__ : `{message}`")
