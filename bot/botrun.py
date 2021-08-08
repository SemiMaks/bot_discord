import discord
import os, sqlite3
from discord.ext import commands

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())


@bot.event
async def on_ready():
    print('Ботан на старте. Nerd on start')

    global base, cur
    base = sqlite3.connect('nerd.db')
    cur = base.cursor()
    if base:
        print('DataBase connected...OK')


bot.run(os.getenv('TOKEN'))
