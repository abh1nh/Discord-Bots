import json
import sys

import discord
from discord.ext import commands


import finnhub
finnhub_client = finnhub.Client(api_key="c1nr4si37fkv6lmc36ig")

allowedStks = finnhub_client.stock_symbols('US')
allowedSymbols = []

for stk in allowedStks:
    allowedSymbols.append(stk["displaySymbol"])


BOT_TOKEN = "MTA1NzgyNzUyOTU2MzU3MDMxNw.GOiqog.NGs9Vc0JmnfO4nThkYOfmq4x4_qN8vQlhUW8o0"
CHANNEL_ID = 1058177575874207845

dataPath = 'C:/Users/Abhi/Desktop/PROJECTS/Discord Bots/Stocks_bot'
sys.path.append(dataPath)


bot = commands.Bot(command_prefix="!",
                   intents=discord.Intents.all())  # set up bot


@bot.event
async def on_ready():
    print("The stocks bot has been set up successfully")


@bot.command()
async def stk(ctx, msg):

    if (ctx.channel.id != CHANNEL_ID):
        return

    res = finnhub_client.symbol_lookup(msg.lower())


    if (res["count"] == 0):
        await ctx.send("No results found for '" + msg + "' in the US markets. Try a different search.")
        return

    for stkInfo in res["result"]:
        if (stkInfo["displaySymbol"] in allowedSymbols):
            ticker = stkInfo["displaySymbol"]
            stkName = stkInfo["description"]

            stkQuote = finnhub_client.quote(ticker)
            
            #await ctx.send("Information for " + stkName + ":")
            #await ctx.send(stkQuote)

            return

        
    #await ctx.send("No results found for '" + msg + "' in the US markets. Try a different search.")
    return



bot.run(BOT_TOKEN)
