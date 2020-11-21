import discord
from discord.ext import commands
import os
import asyncio


client = commands.Bot(command_prefix= "-", case_insensitive=True)
client.remove_command('help')

@client.event
async def on_ready():
    print("I'am ready")

@client.command()
async def ping(ctx):
    await ctx.send('**pong! {}ms**'.format(round(client.latency * 1000)))



client.run(os.environ['token'])