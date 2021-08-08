import os

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())


@bot.event
async def on_ready():
    print('Ботан на старте/ Nerd on start')


bot.run(os.getenv('TOKEN'))
