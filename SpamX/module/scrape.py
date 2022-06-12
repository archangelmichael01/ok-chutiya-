
import os
import sys
import asyncio
from SpamX import (RiZoeL1, RiZoeL2, RiZoeL3, RiZoeL4, RiZoeL5, 
                RiZoeL6, RiZoeL7, RiZoeL8, RiZoeL9, RiZoeL10, 
                RiZoeL11, RiZoeL12, RiZoeL13, RiZoeL14, RiZoeL15, 
                RiZoeL16, RiZoeL17, RiZoeL18, RiZoeL19, RiZoeL20, HNDLR,
                OWNER_ID, hl)
from pyrogram import Client, filters
from pyrogram.types import Message


@RiZoeL.on_message(filters.user(OWNER_ID) & filters.command(["scrape"], prefixes=HNDLR))
@RiZoeL2.on_message(filters.user(OWNER_ID) & filters.command(["scrape"], prefixes=HNDLR))
@RiZoeL3.on_message(filters.user(OWNER_ID) & filters.command(["scrape"], prefixes=HNDLR))
@RiZoeL4.on_message(filters.user(OWNER_ID) & filters.command(["scrape"], prefixes=HNDLR))
@RiZoeL5.on_message(filters.user(OWNER_ID) & filters.command(["scrape"], prefixes=HNDLR))
@RiZoeL6.on_message(filters.user(OWNER_ID) & filters.command(["scrape"], prefixes=HNDLR))
@RiZoeL7.on_message(filters.user(OWNER_ID) & filters.command(["scrape"], prefixes=HNDLR))
@RiZoeL8.on_message(filters.user(OWNER_ID) & filters.command(["scrape"], prefixes=HNDLR))
@RiZoeL9.on_message(filters.user(OWNER_ID) & filters.command(["scrape"], prefixes=HNDLR))
@RiZoeL10.on_message(filters.user(OWNER_ID) & filters.command(["scrape"], prefixes=HNDLR))
@RiZoeL11.on_message(filters.user(OWNER_ID) & filters.command(["scrape"], prefixes=HNDLR))
@RiZoeL12.on_message(filters.user(OWNER_ID) & filters.command(["scrape"], prefixes=HNDLR))
@RiZoeL13.on_message(filters.user(OWNER_ID) & filters.command(["scrape"], prefixes=HNDLR))
@RiZoeL14.on_message(filters.user(OWNER_ID) & filters.command(["scrape"], prefixes=HNDLR))
@RiZoeL15.on_message(filters.user(OWNER_ID) & filters.command(["scrape"], prefixes=HNDLR))
@RiZoeL16.on_message(filters.user(OWNER_ID) & filters.command(["scrape"], prefixes=HNDLR))
@RiZoeL17.on_message(filters.user(OWNER_ID) & filters.command(["scrape"], prefixes=HNDLR))
@RiZoeL18.on_message(filters.user(OWNER_ID) & filters.command(["scrape"], prefixes=HNDLR))
@RiZoeL19.on_message(filters.user(OWNER_ID) & filters.command(["scrape"], prefixes=HNDLR))
@RiZoeL20.on_message(filters.user(OWNER_ID) & filters.command(["scrape"], prefixes=HNDLR))
async def scrape(_, e: Message):
      chat_id = e.chat.id
      user_id = e.fron_user.id
      if chat_id == user_id:
         return await e.reply_text("Use This Cmd In Group")
      scrape_grp = e.text[6:]
      if not scrape_grp:
         return await e.reply_text("Need a chat username or invite link to Scrape Users")
      if scrape_grp.startswith("https://t.me/") or scrape_grp.startswith("@"):
           await e.join_chat(scrape_grp)
           k = await e.get_chat(scrape_grp)
           chatt = k.id
           msg = f"**Scraping Users ** \n\n **From Chat**: {scrape_grp}"
           await e.send_message(chat_id, msg)
           add = 0
           async for Users in e.get_members(chatt)
           
               try:
                 await e.add_chat_member(chat_id, [Users])
                 await asyncio.sleep(0.3)
               except Exception as ex:
                 await e.send_message(chat_id, f"**Error !!** \n\n {ex}")
                 print(ex)

           return await e.send_message(chat_id, f"**Scraped Users** \n\n **From Chat:** {scrape_grp} \n **Users Added:** {add}")
