
import os
import sys
from random import choice
from SpamX import (RiZoeL1, RiZoeL2, RiZoeL3, RiZoeL4, RiZoeL5, 
                RiZoeL6, RiZoeL7, RiZoeL8, RiZoeL9, RiZoeL10, 
                RiZoeL11, RiZoeL12, RiZoeL13, RiZoeL14, RiZoeL15, 
                RiZoeL16, RiZoeL17, RiZoeL18, RiZoeL19, RiZoeL20, HNDLR,
                SUDO_USERS, hl)
from pyrogram import Client, filters
from pyrogram.types import Message
from SpamX.data import *


@RiZoeL.on_message(filters.user(SUDO_USERS) & filters.command(["help"], prefixes=HNDLR))
@RiZoeL2.on_message(filters.user(SUDO_USERS) & filters.command(["help"], prefixes=HNDLR))
@RiZoeL3.on_message(filters.user(SUDO_USERS) & filters.command(["help"], prefixes=HNDLR))
@RiZoeL4.on_message(filters.user(SUDO_USERS) & filters.command(["help"], prefixes=HNDLR))
@RiZoeL5.on_message(filters.user(SUDO_USERS) & filters.command(["help"], prefixes=HNDLR))
@RiZoeL6.on_message(filters.user(SUDO_USERS) & filters.command(["help"], prefixes=HNDLR))
@RiZoeL7.on_message(filters.user(SUDO_USERS) & filters.command(["help"], prefixes=HNDLR))
@RiZoeL8.on_message(filters.user(SUDO_USERS) & filters.command(["help"], prefixes=HNDLR))
@RiZoeL9.on_message(filters.user(SUDO_USERS) & filters.command(["help"], prefixes=HNDLR))
@RiZoeL10.on_message(filters.user(SUDO_USERS) & filters.command(["help"], prefixes=HNDLR))
@RiZoeL11.on_message(filters.user(SUDO_USERS) & filters.command(["help"], prefixes=HNDLR))
@RiZoeL12.on_message(filters.user(SUDO_USERS) & filters.command(["help"], prefixes=HNDLR))
@RiZoeL13.on_message(filters.user(SUDO_USERS) & filters.command(["help"], prefixes=HNDLR))
@RiZoeL14.on_message(filters.user(SUDO_USERS) & filters.command(["help"], prefixes=HNDLR))
@RiZoeL15.on_message(filters.user(SUDO_USERS) & filters.command(["help"], prefixes=HNDLR))
@RiZoeL16.on_message(filters.user(SUDO_USERS) & filters.command(["help"], prefixes=HNDLR))
@RiZoeL17.on_message(filters.user(SUDO_USERS) & filters.command(["help"], prefixes=HNDLR))
@RiZoeL18.on_message(filters.user(SUDO_USERS) & filters.command(["help"], prefixes=HNDLR))
@RiZoeL19.on_message(filters.user(SUDO_USERS) & filters.command(["help"], prefixes=HNDLR))
@RiZoeL20.on_message(filters.user(SUDO_USERS) & filters.command(["help"], prefixes=HNDLR))
async def help(_, e: Message):
        RiZoeL = e.text.split(" ")
        if len(RiZoeL) > 1:
            helping = RiZoeL[1]
            if helping.lower() == "spam":
                await e.reply(spam_help)
            elif helping.lower() == "raid":
                await e.reply(raid_help)
            elif helping.lower() == "dm":
                await e.reply(dm_help)
            elif helping.lower() == "userbot":
                await e.reply(userbot_help)
            elif helping.lower() == "join":
                await e.reply(join_help)
            elif helping.lower() == "leave":
                await e.reply(leave_help)
            elif helping.lower() == "owner":
                await e.reply(owner_help)
            else:
                await e.reply(help_menu)
        else:
            await e.reply(help_menu)


spam_help = f"""
**• Spam Cmds •**

**spam**: Spams a message for given counter, This Spam Cmd Have No Counts Limit !!.
commands:
 {hl}spam <count> <message to spam> 

**delayspam**: Delay spam a text for given counter after given time.
commands:
 {hl}delayspam <delay time(seconds)> <count> <message to spam> 


**pornspam**: Porn Spam for given counter.
commands:
 {hl}pornspam <counter>

**raid:** Activates raid on any individual user for given range.
commands:
 {hl}raid <count> <username or user id>

**© @RiZoeLX**
"""


dm_help = f"""
**• Dm Cmds •**

**Dm:** Dm to any individual using spam bots
command:
  {hl}dm <username or user id> <message>

**Dm Spam:** Spam in Dm of Any individual Users
command:
  {hl}dmspam <count> <username or user id> <message to spam>

**Dm Raid:** raid in Dm of Any individual Users
command:
  {hl}dmraid <count> <username or user id>

**© @RiZoeLX**
"""


join_help = f"""
**• Join Cmds •**

**join:** Join any Public Channel and group
command:
  {hl}join <private/public Chat invite link or username>


**© @RiZoeLX
"""

leave_help = f"""
**• Leave Cmds •**

**leave:** Leave any Public/private Group or Channel
commands:
i) {hl}leave <group Username or chat user id>
ii) {hl}leave

**© @RiZoeLX**
"""

userbot_help = f"""
**• Userbot Cmds •**

**Commands:**

- {hl}ping : To check Ping 

- {hl}alive : To check Bot Version and Other info

- {hl}restart : To Restart Your Spam Bots

**© @RiZoeLX**
"""


owner_help = f"""
**• Owner Cmds •**
__Note__ : Only Spam Bot's Owner Can Use this cmds.

**Scraping:** members adding In Group
command:
{hl}scrape <Public Group invite Link or username>

**Profile:** Profile And Other Cmds
commands:

1) {hl}setname <Profile Name>
2) {hl}setbio <coustom Bio>
3) {hl}setpic <reply to media>

**© @RiZoeLX **
"""

help_menu = f"""
**RiZoeL X Spam Help**

**There are following categories**

`owner` : Get all owner commands and its usage
`spam` : Get all spam commands and its usage
`dm` : Get all dm commands and its usage
`join` : Get join commands and its usage
`leave` : Get leave commands and its usage
`userbot` : Get all userbot commands

**Type** {hl}help <category> **to get all commands in that category and its usage**
**Example**: `{hl}help spam`

**© @RiZoeLX**
"""