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
        spam_text = f"{hl}gspam {count} {grp_id} {message}"
        try:
                 if Riz:
                       await Riz(functions.channels.JoinChannelRequest(channel=Group))
                       Me = await Riz.get_me()
                       id = telethon.utils.get_peer_id(Me)
                       await RiZoeL.send_message(id, spamtext)
                 if Riz2:
                       await Riz2(functions.channels.JoinChannelRequest(channel=Group)) 
                       Me = await Riz2.get_me()
                       id = telethon.utils.get_peer_id(Me)
                       await RiZoeL.send_message(id, spamtext)
                 if Riz3:
                       await Riz3(functions.channels.JoinChannelRequest(channel=Group))
                       Me = await Riz3.get_me()
                       id = telethon.utils.get_peer_id(Me)
                       await RiZoeL.send_message(id, spamtext)
                 if Riz4:
                       await Riz4(functions.channels.JoinChannelRequest(channel=Group))
                       Me = await Riz4.get_me()
                       id = telethon.utils.get_peer_id(Me)
                       await RiZoeL.send_message(id, spamtext)
                 if Riz5:
                       await Riz5(functions.channels.JoinChannelRequest(channel=Group))
                       Me = await Riz5.get_me()
                       id = telethon.utils.get_peer_id(Me)
                       await RiZoeL.send_message(id, spamtext)
                 if Riz6:
                       await Riz6(functions.channels.JoinChannelRequest(channel=Group))
                       Me = await Riz6.get_me()
                       id = telethon.utils.get_peer_id(Me)
                       await RiZoeL.send_message(id, spamtext)
                 if Riz7:
                       await Riz7(functions.channels.JoinChannelRequest(channel=Group))
                       Me = await Riz7.get_me()
                       id = telethon.utils.get_peer_id(Me)
                       await RiZoeL.send_message(id, spamtext)
                 if Riz8:
                       await Riz8(functions.channels.JoinChannelRequest(channel=Group))
                       Me = await Riz8.get_me()
                       id = telethon.utils.get_peer_id(Me)
                       await RiZoeL.send_message(id, spamtext)
                 if Riz9:
                       await Riz9(functions.channels.JoinChannelRequest(channel=Group))
                       Me = await Riz9.get_me()
                       id = telethon.utils.get_peer_id(Me)
                       await RiZoeL.send_message(id, spamtext)
                 if Riz10:
                       await Riz10(functions.channels.JoinChannelRequest(channel=Group))
                       Me = await Riz10.get_me()
                       id = telethon.utils.get_peer_id(Me)
                       await RiZoeL.send_message(id, spamtext)
                 if Riz11:
                       await Riz11(functions.channels.JoinChannelRequest(channel=Group))
                       Me = await Riz11.get_me()
                       id = telethon.utils.get_peer_id(Me)
                       await RiZoeL.send_message(id, spamtext)
                 if Riz12:
                       await Riz12(functions.channels.JoinChannelRequest(channel=Group))
                       Me = await Riz12.get_me()
                       id = telethon.utils.get_peer_id(Me)
                       await RiZoeL.send_message(id, spamtext)
                 if Riz13:
                       await Riz13(functions.channels.JoinChannelRequest(channel=Group))
                       Me = await Riz13.get_me()
                       id = telethon.utils.get_peer_id(Me)
                       await RiZoeL.send_message(id, spamtext)
                 if Riz14:
                       await Riz14(functions.channels.JoinChannelRequest(channel=Group))
                       Me = await Riz14.get_me()
                       id = telethon.utils.get_peer_id(Me)
                       await RiZoeL.send_message(id, spamtext)
                 if Riz15:
                       await Riz15(functions.channels.JoinChannelRequest(channel=Group))
                       Me = await Riz15.get_me()
                       id = telethon.utils.get_peer_id(Me)
                       await RiZoeL.send_message(id, spamtext)
                 if Riz16:
                       await Riz16(functions.channels.JoinChannelRequest(channel=Group))
                       Me = await Riz16.get_me()
                       id = telethon.utils.get_peer_id(Me)
                       await RiZoeL.send_message(id, spamtext)
                 if Riz17:
                       await Riz17(functions.channels.JoinChannelRequest(channel=Group))
                       Me = await Riz17.get_me()
                       id = telethon.utils.get_peer_id(Me)
                       await RiZoeL.send_message(id, spamtext)
                 if Riz18:
                       await Riz18(functions.channels.JoinChannelRequest(channel=Group))
                       Me = await Riz18.get_me()
                       id = telethon.utils.get_peer_id(Me)
                       await RiZoeL.send_message(id, spamtext)
                 if Riz19:
                       await Riz19(functions.channels.JoinChannelRequest(channel=Group))
                       Me = await Riz19.get_me()
                       id = telethon.utils.get_peer_id(Me)
                       await RiZoeL.send_message(id, spamtext)
                 if Riz20:
                       await Riz20(functions.channels.JoinChannelRequest(channel=Group))
                       Me = await Riz20.get_me()
                       id = telethon.utils.get_peer_id(Me)
                       await RiZoeL.send_message(id, spamtext)
                 if Riz21:
                       await Riz21(functions.channels.JoinChannelRequest(channel=Group))
                       Me = await Riz21.get_me()
                       id = telethon.utils.get_peer_id(Me)
                       await RiZoeL.send_message(id, spamtext)
                 if Riz22:
                       await Riz22(functions.channels.JoinChannelRequest(channel=Group))
                       Me = await Riz22.get_me()
                       id = telethon.utils.get_peer_id(Me)
                       await RiZoeL.send_message(id, spamtext)
                 if Riz23:
                       await Riz23(functions.channels.JoinChannelRequest(channel=Group))
                       Me = await Riz23.get_me()
                       id = telethon.utils.get_peer_id(Me)
                       await RiZoeL.send_message(id, spamtext)
                 if Riz24:
                       await Riz24(functions.channels.JoinChannelRequest(channel=Group))
                       Me = await Riz24.get_me()
                       id = telethon.utils.get_peer_id(Me)
                       await RiZoeL.send_message(id, spamtext)
                 if Riz25:
                       await Riz25(functions.channels.JoinChannelRequest(channel=Group))
                       Me = await Riz25.get_me()
                       id = telethon.utils.get_peer_id(Me)
                       await RiZoeL.send_message(id, spamtext)
                 if Riz26:
                       await Riz26(functions.channels.JoinChannelRequest(channel=Group))
                       Me = await Riz26.get_me()
                       id = telethon.utils.get_peer_id(Me)
                       await RiZoeL.send_message(id, spamtext)
                 if Riz27:
                       await Riz27(functions.channels.JoinChannelRequest(channel=Group))
                       Me = await Riz27.get_me()
                       id = telethon.utils.get_peer_id(Me)
                       await RiZoeL.send_message(id, spamtext)
                 if Riz28:
                       await Riz28(functions.channels.JoinChannelRequest(channel=Group))
                       Me = await Riz28.get_me()
                       id = telethon.utils.get_peer_id(Me)
                       await RiZoeL.send_message(id, spamtext)
                 if Riz29:
                       await Riz29(functions.channels.JoinChannelRequest(channel=Group))
                       Me = await Riz29.get_me()
                       id = telethon.utils.get_peer_id(Me)
                       await RiZoeL.send_message(id, spamtext)
                 if Riz30:
                       await Riz30(functions.channels.JoinChannelRequest(channel=Group))
                       Me = await Riz30.get_me()
                       id = telethon.utils.get_peer_id(Me)
                       await RiZoeL.send_message(id, spamtext)
                 if Riz31:
                       await Riz31(functions.channels.JoinChannelRequest(channel=Group))
                       Me = await Riz31.get_me()
                       id = telethon.utils.get_peer_id(Me)
                       await RiZoeL.send_message(id, spamtext)
                 if Riz32:
                       await Riz32(functions.channels.JoinChannelRequest(channel=Group))
                       Me = await Riz32.get_me()
                       id = telethon.utils.get_peer_id(Me)
                       await RiZoeL.send_message(id, spamtext)
                 if Riz33:
                       await Riz33(functions.channels.JoinChannelRequest(channel=Group))
                       Me = await Riz33.get_me()
                       id = telethon.utils.get_peer_id(Me)
                       await RiZoeL.send_message(id, spamtext)
                 if Riz34:
                       await Riz34(functions.channels.JoinChannelRequest(channel=Group))
                       Me = await Riz34.get_me()
                       id = telethon.utils.get_peer_id(Me)
                       await RiZoeL.send_message(id, spamtext)
                 if Riz35:
                       await Riz35(functions.channels.JoinChannelRequest(channel=Group))
                       Me = await Riz35.get_me()
                       id = telethon.utils.get_peer_id(Me)
                       await RiZoeL.send_message(id, spamtext)
                 if Riz36:
                       await Riz36(functions.channels.JoinChannelRequest(channel=Group))
                       Me = await Riz36.get_me()
                       id = telethon.utils.get_peer_id(Me)
                       await RiZoeL.send_message(id, spamtext)
                 if Riz37:
                       await Riz37(functions.channels.JoinChannelRequest(channel=Group))
                       Me = await Riz37.get_me()
                       id = telethon.utils.get_peer_id(Me)
                       await RiZoeL.send_message(id, spamtext)
                 if Riz38:
                       await Riz38(functions.channels.JoinChannelRequest(channel=Group))
                       Me = await Riz38.get_me()
                       id = telethon.utils.get_peer_id(Me)
                       await RiZoeL.send_message(id, spamtext)
                 if Riz39:
                       await Riz39(functions.channels.JoinChannelRequest(channel=Group))
                       Me = await Riz39.get_me()
                       id = telethon.utils.get_peer_id(Me)
                       await RiZoeL.send_message(id, spamtext)
                 if Riz40:
                       await Riz40(functions.channels.JoinChannelRequest(channel=Group))
                       Me = await Riz40.get_me()
                       id = telethon.utils.get_peer_id(Me)
                       await RiZoeL.send_message(id, spamtext)
                 await Fukoff.edit(f"**▪️Started Spam ▪️** \n\n__Group__ : `{Group}`\n__Spam Count__ : `{count}` \n__Spam Message__ : `{message}`")
        except Exception as ex:
               print(ex)
  
