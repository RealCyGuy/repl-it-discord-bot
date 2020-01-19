import keep_alive

import discord
from discord.ext import commands

import os

client = commands.Bot(command_prefix = 'hi')

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

keep_alive.keep_alive

client.run(os.environ['BOT_TOKEN'])