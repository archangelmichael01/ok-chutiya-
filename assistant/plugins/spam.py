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
from RiZoeLXSpam import (id_1, id_2, id_3, id_4, id_5 , id_6, id_7, id_8, id_9, id_10, id_11, id_12, id_13, id_14, id_15, id_16, id_17, id_18, id_19, id_20, id_21, id_22, id_23, id_24, id_25, id_26, id_27, id_28, id_29, id_30, id_31, id_32, id_33, id_34, id_35, id_36, id_37, id_38, id_39, id_40)

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
                   await RiZoeL.send_message(id_1, spamtext)
            if Riz2:
                   await Riz2(functions.channels.JoinChannelRequest(channel=Group)) 
                   await RiZoeL.send_message(id_2, spamtext)
            if Riz3:
                   await Riz3(functions.channels.JoinChannelRequest(channel=Group))
                   await RiZoeL.send_message(id_3, spamtext)
            if Riz4:
                   await Riz4(functions.channels.JoinChannelRequest(channel=Group))
                   await RiZoeL.send_message(id_4, spamtext)
            if Riz5:
                   await Riz5(functions.channels.JoinChannelRequest(channel=Group))
                   await RiZoeL.send_message(id_5, spamtext)
            if Riz6:
                   await Riz6(functions.channels.JoinChannelRequest(channel=Group))
                   await RiZoeL.send_message(id_6, spamtext)
            if Riz7:
                   await Riz7(functions.channels.JoinChannelRequest(channel=Group))
                   await RiZoeL.send_message(id_7, spamtext)
            if Riz8:
                   await Riz8(functions.channels.JoinChannelRequest(channel=Group))
                   await RiZoeL.send_message(id_8, spamtext)
            if Riz9:
                   await Riz9(functions.channels.JoinChannelRequest(channel=Group))
                   await RiZoeL.send_message(id_9, spamtext)
            if Riz10:
                   await Riz10(functions.channels.JoinChannelRequest(channel=Group))
                   await RiZoeL.send_message(id_10, spamtext)
            if Riz11:
                   await Riz11(functions.channels.JoinChannelRequest(channel=Group))
                   await RiZoeL.send_message(id_11, spamtext)
            if Riz12:
                   await Riz12(functions.channels.JoinChannelRequest(channel=Group))
                   await RiZoeL.send_message(id_12, spamtext)
            if Riz13:
                   await Riz13(functions.channels.JoinChannelRequest(channel=Group))
                   await RiZoeL.send_message(id_13, spamtext)
            if Riz14:
                   await Riz14(functions.channels.JoinChannelRequest(channel=Group))
                   await RiZoeL.send_message(id_14, spamtext)
            if Riz15:
                   await Riz15(functions.channels.JoinChannelRequest(channel=Group))
                   await RiZoeL.send_message(id_15, spamtext)
            if Riz16:
                   await Riz16(functions.channels.JoinChannelRequest(channel=Group))
                   await RiZoeL.send_message(id_16, spamtext)
            if Riz17:
                   await Riz17(functions.channels.JoinChannelRequest(channel=Group))
                   await RiZoeL.send_message(id_17, spamtext)
            if Riz18:
                   await Riz18(functions.channels.JoinChannelRequest(channel=Group))
                   await RiZoeL.send_message(id_18, spamtext)
            if Riz19:
                   await Riz19(functions.channels.JoinChannelRequest(channel=Group))
                   await RiZoeL.send_message(id_19, spamtext)
            if Riz20:
                   await Riz20(functions.channels.JoinChannelRequest(channel=Group))
                   await RiZoeL.send_message(id_20, spamtext)
            if Riz21:
                   await Riz21(functions.channels.JoinChannelRequest(channel=Group))
                   await RiZoeL.send_message(id_21, spamtext)
            if Riz22:
                   await Riz22(functions.channels.JoinChannelRequest(channel=Group))
                   await RiZoeL.send_message(id_22, spamtext)
            if Riz23:
                   await Riz23(functions.channels.JoinChannelRequest(channel=Group))
                   await RiZoeL.send_message(id_23, spamtext)
            if Riz24:
                   await Riz24(functions.channels.JoinChannelRequest(channel=Group))
                   await RiZoeL.send_message(id_24, spamtext)
            if Riz25:
                   await Riz25(functions.channels.JoinChannelRequest(channel=Group))
                   await RiZoeL.send_message(id_25, spamtext)
            if Riz26:
                   await Riz26(functions.channels.JoinChannelRequest(channel=Group))
                   await RiZoeL.send_message(id_26, spamtext)
            if Riz27:
                   await Riz27(functions.channels.JoinChannelRequest(channel=Group))
                   await RiZoeL.send_message(id_27, spamtext)
            if Riz28:
                   await Riz28(functions.channels.JoinChannelRequest(channel=Group))
                   await RiZoeL.send_message(id_28, spamtext)
            if Riz29:
                   await Riz29(functions.channels.JoinChannelRequest(channel=Group))
                   await RiZoeL.send_message(id_29, spamtext)
            if Riz30:
                   await Riz30(functions.channels.JoinChannelRequest(channel=Group))
                   await RiZoeL.send_message(id_30, spamtext)
            if Riz31:
                   await Riz31(functions.channels.JoinChannelRequest(channel=Group))
                   await RiZoeL.send_message(id_31, spamtext)
            if Riz32:
                   await Riz32(functions.channels.JoinChannelRequest(channel=Group))
                   await RiZoeL.send_message(id_32, spamtext)
            if Riz33:
                   await Riz33(functions.channels.JoinChannelRequest(channel=Group))
                   await RiZoeL.send_message(id_33, spamtext)
            if Riz34:
                   await Riz34(functions.channels.JoinChannelRequest(channel=Group))
                   await RiZoeL.send_message(id_34, spamtext)
            if Riz35:
                   await Riz35(functions.channels.JoinChannelRequest(channel=Group))
                   await RiZoeL.send_message(id_35, spamtext)
            if Riz36:
                   await Riz36(functions.channels.JoinChannelRequest(channel=Group))
                   await RiZoeL.send_message(id_36, spamtext)
            if Riz37:
                   await Riz37(functions.channels.JoinChannelRequest(channel=Group))
                   await RiZoeL.send_message(id_37, spamtext)
            if Riz38:
                   await Riz38(functions.channels.JoinChannelRequest(channel=Group))
                   await RiZoeL.send_message(id_38, spamtext)
            if Riz39:
                   await Riz39(functions.channels.JoinChannelRequest(channel=Group))
                   await RiZoeL.send_message(id_39, spamtext)
            if Riz40:
                   await Riz40(functions.channels.JoinChannelRequest(channel=Group))
                   await RiZoeL.send_message(id_40, spamtext)
            await Fukoff.edit(f"**▪️Started Spam ▪️** \n\n__Group__ : `{Group}`\n__Spam Count__ : `{count}` \n__Spam Message__ : `{message}`")
        except Exception as ex:
               print(ex)
  
