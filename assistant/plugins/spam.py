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
        if grpp.startswith("https://t.me/") or grpp.startswith("@"):
              Group = grpp
              if re.search(GRP.lower(), Group.lower()):
                   return await rizx.send_message("Sorry !! I can't Spam there")
              k = await Riz.get_entity(Group)
              grp_id = k.id
              try:
                 if Riz:
                       await Riz(functions.channels.JoinChannelRequest(channel=Group))
                 if Riz2:
                       await Riz2(functions.channels.JoinChannelRequest(channel=Group))
                 if Riz3:
                       await Riz3(functions.channels.JoinChannelRequest(channel=Group))
                 if Riz4:
                       await Riz4(functions.channels.JoinChannelRequest(channel=Group))
                 if Riz5:
                       await Riz5(functions.channels.JoinChannelRequest(channel=Group))
                 if Riz6:
                       await Riz6(functions.channels.JoinChannelRequest(channel=Group))
                 if Riz7:
                       await Riz7(functions.channels.JoinChannelRequest(channel=Group))
                 if Riz8:
                       await Riz8(functions.channels.JoinChannelRequest(channel=Group))
                 if Riz9:
                       await Riz9(functions.channels.JoinChannelRequest(channel=Group))
                 if Riz10:
                       await Riz10(functions.channels.JoinChannelRequest(channel=Group))
                 if Riz11:
                       await Riz11(functions.channels.JoinChannelRequest(channel=Group))
                 if Riz12:
                       await Riz12(functions.channels.JoinChannelRequest(channel=Group))
                 if Riz13:
                       await Riz13(functions.channels.JoinChannelRequest(channel=Group))
                 if Riz14:
                       await Riz14(functions.channels.JoinChannelRequest(channel=Group))
                 if Riz15:
                       await Riz15(functions.channels.JoinChannelRequest(channel=Group))
                 if Riz16:
                       await Riz16(functions.channels.JoinChannelRequest(channel=Group))
                 if Riz17:
                       await Riz17(functions.channels.JoinChannelRequest(channel=Group))
                 if Riz18:
                       await Riz18(functions.channels.JoinChannelRequest(channel=Group))
                 if Riz19:
                       await Riz19(functions.channels.JoinChannelRequest(channel=Group))
                 if Riz20:
                       await Riz20(functions.channels.JoinChannelRequest(channel=Group))
                 if Riz21:
                       await Riz21(functions.channels.JoinChannelRequest(channel=Group))
                 if Riz22:
                       await Riz22(functions.channels.JoinChannelRequest(channel=Group))
                 if Riz23:
                       await Riz23(functions.channels.JoinChannelRequest(channel=Group))
                 if Riz24:
                       await Riz24(functions.channels.JoinChannelRequest(channel=Group))
                 if Riz25:
                       await Riz25(functions.channels.JoinChannelRequest(channel=Group))
                 if Riz26:
                       await Riz26(functions.channels.JoinChannelRequest(channel=Group))
                 if Riz27:
                       await Riz27(functions.channels.JoinChannelRequest(channel=Group))
                 if Riz28:
                       await Riz28(functions.channels.JoinChannelRequest(channel=Group))
                 if Riz29:
                       await Riz29(functions.channels.JoinChannelRequest(channel=Group))
                 if Riz30:
                       await Riz30(functions.channels.JoinChannelRequest(channel=Group))
                 if Riz31:
                       await Riz31(functions.channels.JoinChannelRequest(channel=Group))
                 if Riz32:
                       await Riz32(functions.channels.JoinChannelRequest(channel=Group))
                 if Riz33:
                       await Riz33(functions.channels.JoinChannelRequest(channel=Group))
                 if Riz34:
                       await Riz34(functions.channels.JoinChannelRequest(channel=Group))
                 if Riz35:
                       await Riz35(functions.channels.JoinChannelRequest(channel=Group))
                 if Riz36:
                       await Riz36(functions.channels.JoinChannelRequest(channel=Group))
                 if Riz37:
                       await Riz37(functions.channels.JoinChannelRequest(channel=Group))
                 if Riz38:
                       await Riz38(functions.channels.JoinChannelRequest(channel=Group))
                 if Riz39:
                       await Riz39(functions.channels.JoinChannelRequest(channel=Group))
                 if Riz40:
                       await Riz40(functions.channels.JoinChannelRequest(channel=Group))
              except Exception as ex:
                      print(ex)
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
        Fukoff = await rizx.send_message(f"__Starting Spam In {Group}__")
        await asyncio.sleep(2)
        await Fukoff.edit(f"**▪️Started Spam ▪️** \n\n__Group__ : `{Group}`\n__Spam Count__ : `{count}` \n__Spam Message__ : `{message}`")     
        ids = 0
        try:
           for _ in range(count):
            #  while count != 0:
              if Riz:
                  await Riz.send_message(grp_id, message)
                  await asyncio.sleep(0.3)
              if Riz2:
                  await Riz2.send_message(grp_id, message)
                  await asyncio.sleep(0.3)
              if Riz3:
                  await Riz3.send_message(grp_id, message)
                  await asyncio.sleep(0.3)
              if Riz4:
                  await Riz4.send_message(grp_id, message)
                  await asyncio.sleep(0.3)
              if Riz5:
                  await Riz5.send_message(grp_id, message)
                  await asyncio.sleep(0.3)
              if Riz6:
                  await Riz6.send_message(grp_id, message)
                  await asyncio.sleep(0.3)
              if Riz7:
                  await Riz7.send_message(grp_id, message)
                  await asyncio.sleep(0.3)
              if Riz8:
                  await Riz8.send_message(grp_id, message)
                  await asyncio.sleep(0.3)
              if Riz9:
                  await Riz9.send_message(grp_id, message)
                  await asyncio.sleep(0.3)
              if Riz10:
                  await Riz10.send_message(grp_id, message)
                  await asyncio.sleep(0.3)
              if Riz11:
                  await Riz11.send_message(grp_id, message)
                  await asyncio.sleep(0.3)
              if Riz12:
                  await Riz12.send_message(grp_id, message)
                  await asyncio.sleep(0.3)
              if Riz13:
                  await Riz13.send_message(grp_id, message)
                  await asyncio.sleep(0.3)
              if Riz14:
                  await Riz14.send_message(grp_id, message)
                  await asyncio.sleep(0.3)
              if Riz15:
                  await Riz15.send_message(grp_id, message)
                  await asyncio.sleep(0.3)
              if Riz16:
                  await Riz16.send_message(grp_id, message)
                  await asyncio.sleep(0.3)
              if Riz17:
                  await Riz17.send_message(grp_id, message)
                  await asyncio.sleep(0.3)
              if Riz18:
                  await Riz18.send_message(grp_id, message)
                  await asyncio.sleep(0.3)
              if Riz19:
                  await Riz19.send_message(grp_id, message)
                  await asyncio.sleep(0.3)
              if Riz20:
                  await Riz20.send_message(grp_id, message)
                  await asyncio.sleep(0.3)
              if Riz21:
                  await Riz21.send_message(grp_id, message)
                  await asyncio.sleep(0.3)
              if Riz22:
                  await Riz22.send_message(grp_id, message)
                  await asyncio.sleep(0.3)
              if Riz23:
                  await Riz23.send_message(grp_id, message)
                  await asyncio.sleep(0.3)
              if Riz24:
                  await Riz24.send_message(grp_id, message)
                  await asyncio.sleep(0.3)
              if Riz25:
                  await Riz25.send_message(grp_id, message)
                  await asyncio.sleep(0.3)
              if Riz26:
                  await Riz26.send_message(grp_id, message)
                  await asyncio.sleep(0.3)
              if Riz27:
                  await Riz27.send_message(grp_id, message)
                  await asyncio.sleep(0.3)
              if Riz28:
                  await Riz28.send_message(grp_id, message)
                  await asyncio.sleep(0.3)
              if Riz29:
                  await Riz29.send_message(grp_id, message)
                  await asyncio.sleep(0.3)
              if Riz30:
                  await Riz30.send_message(grp_id, message)
                  await asyncio.sleep(0.3)
              if Riz31:
                  await Riz31.send_message(grp_id, message)
                  await asyncio.sleep(0.3)
              if Riz32:
                  await Riz31.send_message(grp_id, message)
                  await asyncio.sleep(0.3)
              if Riz33:
                  await Riz33.send_message(grp_id, message)
                  await asyncio.sleep(0.3)
              if Riz34:
                  await Riz34.send_message(grp_id, message)
                  await asyncio.sleep(0.3)
              if Riz35:
                  await Riz35.send_message(grp_id, message)
              if Riz36:
                  await Riz36.send_message(grp_id, message)
              if Riz37:
                  await Riz37.send_message(grp_id, message)
              if Riz38:
                  await Riz38.send_message(grp_id, message)
                  await asyncio.sleep(0.3)
              if Riz39:
                  await Riz39.send_message(grp_id, message)
                  await asyncio.sleep(0.3)
              if Riz40:
                  await Riz40.send_message(grp_id, message)
                  await asyncio.sleep(0.3)
        except Exception as ex:
                print(ex)
