import keep_alive

import discord
from discord.ext import commands

import os

client = commands.Bot(command_prefix = '!')

cogs = ["cogs.ping"]

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
    for cog in cogs:
        client.load_extension(cog)
    return


keep_alive.keep_alive

client.run(os.environ['BOT_TOKEN'])