
import os
import sys
from random import choice
from SpamX import (RiZoeL1, RiZoeL2, RiZoeL3, RiZoeL4, RiZoeL5, 
                RiZoeL6, RiZoeL7, RiZoeL8, RiZoeL9, RiZoeL10, 
                RiZoeL11, RiZoeL12, RiZoeL13, RiZoeL14, RiZoeL15, 
                RiZoeL16, RiZoeL17, RiZoeL18, RiZoeL19, RiZoeL20, HNDLR,
                OWNER_ID, hl, SUDO_USERS)
from pyrogram import Client, filters
from pyrogram.types import Message
from SpamX.data import *


@RiZoeL.on_message(filters.user(OWNER_ID) & filters.command(["setpic"], prefixes=HNDLR))
@RiZoeL2.on_message(filters.user(OWNER_ID) & filters.command(["setpic"], prefixes=HNDLR))
@RiZoeL3.on_message(filters.user(OWNER_ID) & filters.command(["setpic"], prefixes=HNDLR))
@RiZoeL4.on_message(filters.user(OWNER_ID) & filters.command(["setpic"], prefixes=HNDLR))
@RiZoeL5.on_message(filters.user(OWNER_ID) & filters.command(["setpic"], prefixes=HNDLR))
@RiZoeL6.on_message(filters.user(OWNER_ID) & filters.command(["setpic"], prefixes=HNDLR))
@RiZoeL7.on_message(filters.user(OWNER_ID) & filters.command(["setpic"], prefixes=HNDLR))
@RiZoeL8.on_message(filters.user(OWNER_ID) & filters.command(["setpic"], prefixes=HNDLR))
@RiZoeL9.on_message(filters.user(OWNER_ID) & filters.command(["setpic"], prefixes=HNDLR))
@RiZoeL10.on_message(filters.user(OWNER_ID) & filters.command(["setpic"], prefixes=HNDLR))
@RiZoeL11.on_message(filters.user(OWNER_ID) & filters.command(["setpic"], prefixes=HNDLR))
@RiZoeL12.on_message(filters.user(OWNER_ID) & filters.command(["setpic"], prefixes=HNDLR))
@RiZoeL13.on_message(filters.user(OWNER_ID) & filters.command(["setpic"], prefixes=HNDLR))
@RiZoeL14.on_message(filters.user(OWNER_ID) & filters.command(["setpic"], prefixes=HNDLR))
@RiZoeL15.on_message(filters.user(OWNER_ID) & filters.command(["setpic"], prefixes=HNDLR))
@RiZoeL16.on_message(filters.user(OWNER_ID) & filters.command(["setpic"], prefixes=HNDLR))
@RiZoeL17.on_message(filters.user(OWNER_ID) & filters.command(["setpic"], prefixes=HNDLR))
@RiZoeL18.on_message(filters.user(OWNER_ID) & filters.command(["setpic"], prefixes=HNDLR))
@RiZoeL19.on_message(filters.user(OWNER_ID) & filters.command(["setpic"], prefixes=HNDLR))
@RiZoeL20.on_message(filters.user(OWNER_ID) & filters.command(["setpic"], prefixes=HNDLR))
async def setpic(_, e: Message):
     if e.from_user.id in SUDO_USERS:
          return await e.reply_text("Only Owner Can Use This Cmds")
     replied = e.reply_to_message
     if replied.video or replied.photo:
        try:
            media = await replied.download_media()
        except:
            pass
        await e.set_profile_photo(media)
        await e.reply_text(f"**Changed profile picture successfully** ✅")
        try:
            os.remove(media)
        except Exception as e:
            print(str(e))
     else:
         await e.reply_text("Reply To Media or Video To Change Profile pic")



@RiZoeL.on_message(filters.user(OWNER_ID) & filters.command(["setname"], prefixes=HNDLR))
@RiZoeL2.on_message(filters.user(OWNER_ID) & filters.command(["setname"], prefixes=HNDLR))
@RiZoeL3.on_message(filters.user(OWNER_ID) & filters.command(["setname"], prefixes=HNDLR))
@RiZoeL4.on_message(filters.user(OWNER_ID) & filters.command(["setname"], prefixes=HNDLR))
@RiZoeL5.on_message(filters.user(OWNER_ID) & filters.command(["setname"], prefixes=HNDLR))
@RiZoeL6.on_message(filters.user(OWNER_ID) & filters.command(["setname"], prefixes=HNDLR))
@RiZoeL7.on_message(filters.user(OWNER_ID) & filters.command(["setname"], prefixes=HNDLR))
@RiZoeL8.on_message(filters.user(OWNER_ID) & filters.command(["setname"], prefixes=HNDLR))
@RiZoeL9.on_message(filters.user(OWNER_ID) & filters.command(["setname"], prefixes=HNDLR))
@RiZoeL10.on_message(filters.user(OWNER_ID) & filters.command(["setname"], prefixes=HNDLR))
@RiZoeL11.on_message(filters.user(OWNER_ID) & filters.command(["setname"], prefixes=HNDLR))
@RiZoeL12.on_message(filters.user(OWNER_ID) & filters.command(["setname"], prefixes=HNDLR))
@RiZoeL13.on_message(filters.user(OWNER_ID) & filters.command(["setname"], prefixes=HNDLR))
@RiZoeL14.on_message(filters.user(OWNER_ID) & filters.command(["setname"], prefixes=HNDLR))
@RiZoeL15.on_message(filters.user(OWNER_ID) & filters.command(["setname"], prefixes=HNDLR))
@RiZoeL16.on_message(filters.user(OWNER_ID) & filters.command(["setname"], prefixes=HNDLR))
@RiZoeL17.on_message(filters.user(OWNER_ID) & filters.command(["setname"], prefixes=HNDLR))
@RiZoeL18.on_message(filters.user(OWNER_ID) & filters.command(["setname"], prefixes=HNDLR))
@RiZoeL19.on_message(filters.user(OWNER_ID) & filters.command(["setname"], prefixes=HNDLR))
@RiZoeL20.on_message(filters.user(OWNER_ID) & filters.command(["setname"], prefixes=HNDLR))
async def setname(_, e: Message): 
      if e.from_user.id in SUDO_USERS:
          return await e.reply_text("Only Owner Can Use This Cmds")
      Usage = f"**Module Name: setname** \n\n Command: {HNDLR}setname <new name>"
      Rizoel = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
      if len(Rizoel) == 1:
          name = str(Rizoel[0])
          try:
            await e.update_profile(first_name=name)
            await e.reply_text(f"**Profile Name Changed Successfully !!** \n\n **New Name:** {name}")
          except Exception as ex:
            await e.reply_text(f"**Error !!** \n\n {ex}")
            print(ex)
      else:
          await e.reply(Usage)


@RiZoeL.on_message(filters.user(OWNER_ID) & filters.command(["setbio"], prefixes=HNDLR))
@RiZoeL2.on_message(filters.user(OWNER_ID) & filters.command(["setbio"], prefixes=HNDLR))
@RiZoeL3.on_message(filters.user(OWNER_ID) & filters.command(["setbio"], prefixes=HNDLR))
@RiZoeL4.on_message(filters.user(OWNER_ID) & filters.command(["setbio"], prefixes=HNDLR))
@RiZoeL5.on_message(filters.user(OWNER_ID) & filters.command(["setbio"], prefixes=HNDLR))
@RiZoeL6.on_message(filters.user(OWNER_ID) & filters.command(["setbio"], prefixes=HNDLR))
@RiZoeL7.on_message(filters.user(OWNER_ID) & filters.command(["setbio"], prefixes=HNDLR))
@RiZoeL8.on_message(filters.user(OWNER_ID) & filters.command(["setbio"], prefixes=HNDLR))
@RiZoeL9.on_message(filters.user(OWNER_ID) & filters.command(["setbio"], prefixes=HNDLR))
@RiZoeL10.on_message(filters.user(OWNER_ID) & filters.command(["setbio"], prefixes=HNDLR))
@RiZoeL11.on_message(filters.user(OWNER_ID) & filters.command(["setbio"], prefixes=HNDLR))
@RiZoeL12.on_message(filters.user(OWNER_ID) & filters.command(["setbio"], prefixes=HNDLR))
@RiZoeL13.on_message(filters.user(OWNER_ID) & filters.command(["setbio"], prefixes=HNDLR))
@RiZoeL14.on_message(filters.user(OWNER_ID) & filters.command(["setbio"], prefixes=HNDLR))
@RiZoeL15.on_message(filters.user(OWNER_ID) & filters.command(["setbio"], prefixes=HNDLR))
@RiZoeL16.on_message(filters.user(OWNER_ID) & filters.command(["setbio"], prefixes=HNDLR))
@RiZoeL17.on_message(filters.user(OWNER_ID) & filters.command(["setbio"], prefixes=HNDLR))
@RiZoeL18.on_message(filters.user(OWNER_ID) & filters.command(["setbio"], prefixes=HNDLR))
@RiZoeL19.on_message(filters.user(OWNER_ID) & filters.command(["setbio"], prefixes=HNDLR))
@RiZoeL20.on_message(filters.user(OWNER_ID) & filters.command(["setbio"], prefixes=HNDLR))
async def setbio(_, e: Message): 
      if e.from_user.id in SUDO_USERS:
          return await e.reply_text("Only Owner Can Use This Cmds")
      Usage = f"**Module Name: setbio** \n\n Command: {HNDLR}setbio <New Bio>"
      Rizoel = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
      if len(Rizoel) == 1:
          xd = str(Rizoel[0])
          try:
             await e.update_profile(bio=xd)
             await e.reply_text(f"**Profile Bio Changed Successfully !** \n\n **New Bio**: {xd}")
          except Exception as ex:
            await e.reply_text(f"**Error !!** \n\n {ex}")
            print(ex)
      else:
          await e.reply(Usage)

          
@RiZoeL.on_message(filters.user(OWNER_ID) & filters.command(["setprofile"], prefixes=HNDLR))
@RiZoeL2.on_message(filters.user(OWNER_ID) & filters.command(["setprofile"], prefixes=HNDLR))
@RiZoeL3.on_message(filters.user(OWNER_ID) & filters.command(["setprofile"], prefixes=HNDLR))
@RiZoeL4.on_message(filters.user(OWNER_ID) & filters.command(["setprofile"], prefixes=HNDLR))
@RiZoeL5.on_message(filters.user(OWNER_ID) & filters.command(["setprofile"], prefixes=HNDLR))
@RiZoeL6.on_message(filters.user(OWNER_ID) & filters.command(["setprofile"], prefixes=HNDLR))
@RiZoeL7.on_message(filters.user(OWNER_ID) & filters.command(["setprofile"], prefixes=HNDLR))
@RiZoeL8.on_message(filters.user(OWNER_ID) & filters.command(["setprofile"], prefixes=HNDLR))
@RiZoeL9.on_message(filters.user(OWNER_ID) & filters.command(["setprofile"], prefixes=HNDLR))
@RiZoeL10.on_message(filters.user(OWNER_ID) & filters.command(["setprofile"], prefixes=HNDLR))
@RiZoeL11.on_message(filters.user(OWNER_ID) & filters.command(["setprofile"], prefixes=HNDLR))
@RiZoeL12.on_message(filters.user(OWNER_ID) & filters.command(["setprofile"], prefixes=HNDLR))
@RiZoeL13.on_message(filters.user(OWNER_ID) & filters.command(["setprofile"], prefixes=HNDLR))
@RiZoeL14.on_message(filters.user(OWNER_ID) & filters.command(["setprofile"], prefixes=HNDLR))
@RiZoeL15.on_message(filters.user(OWNER_ID) & filters.command(["setprofile"], prefixes=HNDLR))
@RiZoeL16.on_message(filters.user(OWNER_ID) & filters.command(["setprofile"], prefixes=HNDLR))
@RiZoeL17.on_message(filters.user(OWNER_ID) & filters.command(["setprofile"], prefixes=HNDLR))
@RiZoeL18.on_message(filters.user(OWNER_ID) & filters.command(["setprofile"], prefixes=HNDLR))
@RiZoeL19.on_message(filters.user(OWNER_ID) & filters.command(["setprofile"], prefixes=HNDLR))
@RiZoeL20.on_message(filters.user(OWNER_ID) & filters.command(["setprofile"], prefixes=HNDLR))
async def setprofile(_, e: Message): 
      if e.from_user.id in SUDO_USERS:
          return await e.reply_text("Only Owner Can Use This Cmds")
      Usage = f"**Module Name: setprofile** \n\n Command: {HNDLR}setprofile <New Name> <New Bio>"
      Rizoel = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
      if len(Rizoel) == 2:
          xd = str(Rizoel[1])
          name = str(Rizoel[0])
          try:
            await e.update_profle(first_name=name, bio=xd)
            await e.reply_text(f"**Profile Updated !!** \n\n **New Name:** {name} \n **New Bio:** {xr}")
          except Exception as ex:
            await e.reply_text(f"**Error !!** \n\n {ex}")
            print(ex)
      else:
          await e.reply(Usage)
