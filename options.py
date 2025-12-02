from functions import clear, center, pause
import threading
import asyncio
import functions
import time
import requests
import json as jsonic
import asyncio
import asyncio
import random
from datetime import datetime
#import asyncio
import asyncio
import random
import os

def nukebotstart():
    os.system("python ./UWUbot.py")

def iplookup():
    try:
        clear()
        functions.warning()
        clear()
        ip = functions.retardinput(False, center("IP/Domain > "))
        clear()
        time.sleep(0.9)
        response = requests.get(f"http://ip-api.com/json/{ip}")
        json = response.json()
        grabdata = f"""
    < GRABBED DATA >

    < IP >
    {json['query']}

    < Status >

    {json['status']}

    < Country >

    {json['country']}

    < Region >

    {json['region']}

    < Timezone >

    {json['timezone']}

    < ISP >

    {json['isp']}

    < Grabbed from >

    https://ip-api.com/json/{ip}

    """
        for line in grabdata.splitlines():
            functions.retardprint(False, center(line))
        pause()
    except Exception as _:
        pass

async def nuke():
    try:
        clear()
        functions.warning()
        clear()
        functions.retardprint(False, "open UWUbot.py retard")
    except Exception as e:
        functions.retardprint(True, "shit " + str(e))
        pause()
        clear()