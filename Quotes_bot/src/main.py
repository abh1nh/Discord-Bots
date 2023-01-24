import json
import sys
import chardet

import discord
from discord.ext import commands

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger


BOT_TOKEN = "MTA1NjcwNTQxNjY2NDQ0OTEwNA.G02jNH.pHDSqKdgnaxRn1a5JO56ROV8SviE9GsKomgbnI"
CHANNEL_ID = 1056730128610234518

count = 0


dataPath = 'C:/Users/Abhi/Desktop/PROJECTS/Discord Bots/Quotes_bot'
sys.path.append(dataPath)
f_name = 'quotes.json'


enc = chardet.detect(open(f_name, 'rb').read())[
    'encoding']  # find encoding of the json file

with open(f_name, 'r', encoding=enc) as f:  # store json file as a list of python dicts
    data = json.load(f)
    f.close()


bot = commands.Bot(command_prefix="!",
                   intents=discord.Intents.all())  # set up bot


async def quoteSend():  # function logic
    global count

    channel = bot.get_channel(CHANNEL_ID)
    quoteStr = data[count]["Quote"]
    authorStr = data[count]["Author"]
    categoryStr = data[count]["Category"]

    await channel.send("Today's Quote: " + quoteStr)
    await channel.send("Said by: " + authorStr)
    await channel.send("Category: " + categoryStr)

    count += 1

    if (count >= len(data)):
        count = 0


@bot.event
async def on_ready():
    print("The bot has been set up successfully")

    # initializing scheduler
    scheduler = AsyncIOScheduler()

    # sends quote to the channel when time hit 9:00:00 AM
    scheduler.add_job(quoteSend, CronTrigger(
        hour="9", minute="0", second="0"))

    # starting the scheduler
    scheduler.start()


bot.run(BOT_TOKEN)
