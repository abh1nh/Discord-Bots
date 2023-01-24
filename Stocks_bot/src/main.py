import discord
from discord.ext import commands


import finnhub
finnhub_client = finnhub.Client(api_key="your_key_here")

allowedStks = finnhub_client.stock_symbols('US')
allowedSymbols = []

for stk in allowedStks:
    allowedSymbols.append(stk["displaySymbol"])


BOT_TOKEN = "your_token_here"
CHANNEL_ID = your_channelID_here


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
