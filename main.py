# skidded imports as always
import threading
import colorama
import time
from functions import retardinput, retardprint, center, banner, clear, pause
import os
import asyncio
import sys
if os.name == "posix":
    retardprint(True, "Xeno is only supported on Windows.\nPlease re-download it on a Windows machine.")
    time.sleep(1.5)
    sys.exit(1)
import options

# why does colorama have to init??

helpme = banner(False)
colorama.init()

validoptions = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10
]

def lol(whattolaunch):
    if whattolaunch == "nukebot":
        os.system("python ./UWUbot.py")
    elif whattolaunch == "webhookdestroyer":
        os.system("python ./WebhookDiddler.py")

async def menu(errto=None):
    category = errto
    clear()

    for line in helpme.splitlines():
        retardprint(False, center(line))

    optionas = """
            1. IP Lookup                6.
            2. Nuke Server              7.
            3. Destroy DC Webhook       8.
            4.                          9.
            5.                          10.
"""

    for line in optionas.splitlines():
        retardprint(False, center(line))

    choice = retardinput(False, "Option > ").strip()

    if not choice.isdigit():
        clear()
        retardprint(True, "Invalid option.")
        

    choice = int(choice)

    if choice not in validoptions:
        clear()
        retardprint(True, "Invalid option.")
        

    if choice == 1:
        options.iplookup()
        clear()

    elif choice == 2:
            try:
                lol("nukebot")
                clear()
            except Exception as e:
                print(e)
                pause()
                clear()
            
    elif choice == 3:
        try:
            lol("webhookdestroyer")
            clear()
        except Exception as e:
            print(str(e))
            pause()
            clear()

    elif choice == 4:
        pass

    elif choice == 5:
        pass

    elif choice == 6:
        pass

    elif choice == 7:
        pass

    elif choice == 8:
        pass

    elif choice == 9:
        pass

    elif choice == 10:
        pass

        
def run_menu():
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(menu())

while True:
    run_menu()