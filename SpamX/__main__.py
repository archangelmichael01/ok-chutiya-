import sys
from sys import argv
import glob
from pathlib import Path
import asyncio
from SpamX.utils import load_plugins
from pyrogram import idle
from . import (RiZoeL, RiZoeL2, RiZoeL3, RiZoeL4, RiZoeL5, 
                RiZoeL6, RiZoeL7, RiZoeL8, RiZoeL9, RiZoeL10, 
                RiZoeL11, RiZoeL12, RiZoeL13, RiZoeL14, RiZoeL15, 
                RiZoeL16, RiZoeL17, RiZoeL18, RiZoeL19, RiZoeL20, hl)

async def startup():
    # STARTING CLIENTS
    if RiZoeL:
        try:
            await RiZoeL.start()
            await RiZoeL.join_chat("DNHxHELL")
            await RiZoeL.join_chat("RiZoeLX")
        except Exception as e:
            print(str(e))

    if RiZoeL2:
        try:
            await RiZoeL2.start()
            await RiZoeL2.join_chat("DNHxHELL")
            await RiZoeL2.join_chat("RiZoeLX")
        except Exception as e:
            print(str(e))

    if RiZoeL3:
        try:
            await RiZoeL3.start()
            await RiZoeL3.join_chat("DNHxHELL")
            await RiZoeL3.join_chat("RiZoeLX")
        except Exception as e:
            print(str(e))

    if RiZoeL4:
        try:
            await RiZoeL4.start()
            await RiZoeL4.join_chat("DNHxHELL")
            await RiZoeL4.join_chat("RiZoeLX")
        except Exception as e:
            print(str(e))

    if RiZoeL5:
        try:
            await RiZoeL5.start()
            await RiZoeL5.join_chat("DNHxHELL")
            await RiZoeL5.join_chat("RiZoeLX")
        except Exception as e:
            print(str(e))

    if RiZoeL6:
        try:
            await RiZoeL6.start()
            await RiZoeL6.join_chat("DNHxHELL")
            await RiZoeL6.join_chat("RiZoeLX")
        except Exception as e:
            print(str(e))

    if RiZoeL7:
        try:
            await RiZoeL7.start()
            await RiZoeL7.join_chat("DNHxHELL")
            await RiZoeL7.join_chat("RiZoeLX")
        except Exception as e:
            print(str(e))

    if RiZoeL8:
        try:
            await RiZoeL8.start()
            await RiZoeL8.join_chat("DNHxHELL")
            await RiZoeL8.join_chat("RiZoeLX")
        except Exception as e:
            print(str(e))

    if RiZoeL9:
        try:
            await RiZoeL9.start()
            await RiZoeL9.join_chat("DNHxHELL")
            await RiZoeL9.join_chat("RiZoeLX")
        except Exception as e:
            print(str(e))

    if RiZoeL10:
        try:
            await RiZoeL10.start()
            await RiZoeL10.join_chat("DNHxHELL")
            await RiZoeL10.join_chat("RiZoeLX")
        except Exception as e:
            print(str(e))

    if RiZoeL11:
        try:
            await RiZoeL11.start()
            await RiZoeL11.join_chat("DNHxHELL")
            await RiZoeL11.join_chat("RiZoeLX")
        except Exception as e:
            print(str(e))

    if RiZoeL12:
        try:
            await RiZoeL12.start()
            await RiZoeL12.join_chat("DNHxHELL")
            await RiZoeL12.join_chat("RiZoeLX")
        except Exception as e:
            print(str(e))

    if RiZoeL13:
        try:
            await RiZoeL13.start()
            await RiZoeL13.join_chat("DNHxHELL")
            await RiZoeL13.join_chat("RiZoeLX")
        except Exception as e:
            print(str(e))

    if RiZoeL14:
        try:
            await RiZoeL14.start()
            await RiZoeL14.join_chat("DNHxHELL")
            await RiZoeL14.join_chat("RiZoeLX")
        except Exception as e:
            print(str(e))

    if RiZoeL15:
        try:
            await RiZoeL15.start()
            await RiZoeL15.join_chat("DNHxHELL")
            await RiZoeL15.join_chat("RiZoeLX")
        except Exception as e:
            print(str(e))

    if RiZoeL16:
        try:
            await RiZoeL16.start()
            await RiZoeL16.join_chat("DNHxHELL")
            await RiZoeL16.join_chat("RiZoeLX")
        except Exception as e:
            print(str(e))

    if RiZoeL17:
        try:
            await RiZoeL17.start()
            await RiZoeL17.join_chat("DNHxHELL")
            await RiZoeL17.join_chat("RiZoeLX")
        except Exception as e:
            print(str(e))

    if RiZoeL18:
        try:
            await RiZoeL18.start()
            await RiZoeL18.join_chat("DNHxHELL")
            await RiZoeL18.join_chat("RiZoeLX")
        except Exception as e:
            print(str(e))

    if RiZoeL19:
        try:
            await RiZoeL19.start()
            await RiZoeL19.join_chat("DNHxHELL")
            await RiZoeL19.join_chat("RiZoeLX")
        except Exception as e:
            print(str(e))

    if RiZoeL20:
        try:
            await RiZoeL20.start()
            await RiZoeL20.join_chat("DNHxHELL")
            await RiZoeL20.join_chat("RiZoeLX")
        except Exception as e:
            print(str(e))
  
    await idle()


loop = asyncio.get_event_loop()
loop.run_until_complete(startup())


path = "SpamX/module/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

print("Pyrogram Spam Successfully deployed -!")
print("Enjoy! Do visit @RiZoeLX")

if len(argv) not in (1, 3, 4):
    try:
        RiZoeL.disconnect()
    except Exception as e:
        pass
    try:
        RiZoeL2.disconnect()
    except Exception as e:
        pass
    try:
        RiZoeL3.disconnect()
    except Exception as e:
        pass
    try:
        RiZoeL4.disconnect()
    except Exception as e:
        pass
    try:
        RiZoeL5.disconnect()
    except Exception as e:
        pass
    try:
        RiZoeL6.disconnect()
    except Exception as e:
        pass
    try:
        RiZoeL7.disconnect()
    except Exception as e:
        pass
    try:
        RiZoeL8.disconnect()
    except Exception as e:
        pass
    try:
        RiZoeL9.disconnect()
    except Exception as e:
        pass
    try:
        RiZoeL10.disconnect()
    except Exception as e:
        pass
    try:
        RiZoeL11.disconnect()
    except Exception as e:
        pass
    try:
        RiZoeL12.disconnect()
    except Exception as e:
        pass
    try:
        RiZoeL13.disconnect()
    except Exception as e:
        pass
    try:
        RiZoeL14.disconnect()
    except Exception as e:
        pass
    try:
        RiZoeL15.disconnect()
    except Exception as e:
        pass
    try:
        RiZoeL16.disconnect()
    except Exception as e:
        pass
    try:
        RiZoeL17.disconnect()
    except Exception as e:
        pass
    try:
        RiZoeL18.disconnect()
    except Exception as e:
        pass
    try:
        RiZoeL19.disconnect()
    except Exception as e:
        pass
    try:
        RiZoeL20.disconnect()
    except Exception as e:
        pass
else:
    try:
        RiZoeL.run_until_disconnected()
    except Exception as e:
        pass
    try:
        RiZoeL2.run_until_disconnected()
    except Exception as e:
        pass
    try:
        RiZoeL3.run_until_disconnected()
    except Exception as e:
        pass
    try:
        RiZoeL4.run_until_disconnected()
    except Exception as e:
        pass
    try:
        RiZoeL5.run_until_disconnected()
    except Exception as e:
        pass
    try:
        RiZoeL6.run_until_disconnected()
    except Exception as e:
        pass
    try:
        RiZoeL7.run_until_disconnected()
    except Exception as e:
        pass
    try:
        RiZoeL8.run_until_disconnected()
    except Exception as e:
        pass
    try:
        RiZoeL9.run_until_disconnected()
    except Exception as e:
        pass
    try:
        RiZoeL10.run_until_disconnected()
    except Exception as e:
        pass
    try:
        RiZoeL11.run_until_disconnected()
    except Exception as e:
        pass
    try:
        RiZoeL12.run_until_disconnected()
    except Exception as e:
        pass
    try:
        RiZoeL13.run_until_disconnected()
    except Exception as e:
        pass
    try:
        RiZoeL14.run_until_disconnected()
    except Exception as e:
        pass
    try:
        RiZoeL15.run_until_disconnected()
    except Exception as e:
        pass
    try:
        RiZoeL16.run_until_disconnected()
    except Exception as e:
        pass
    try:
        RiZoeL17.run_until_disconnected()
    except Exception as e:
        pass
    try:
        RiZoeL18.run_until_disconnected()
    except Exception as e:
        pass
    try:
        RiZoeL19.run_until_disconnected()
    except Exception as e:
        pass
    try:
        RiZoeL20.run_until_disconnected()
    except Exception as e:
        pass
