import discord
from discord.ext import commands
import json

with open("config.json", "r") as f:
    data = json.load(f)

token = str(data["token"])
prefix = str(data["prefix"])

client = commands.AutoShardedBot(command_prefix=commands.when_mentioned_or(prefix), intents=discord.Intents.all())
cogs = ["cogs.Roulette", "cogs.Error"]

def load_cogs():
    for i in cogs:
        client.load_extension(i)

@client.event
async def on_ready():
    load_cogs()
    print("Online.")

client.run(token, reconnect=True, bot=True)