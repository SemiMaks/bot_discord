import discord
import os, sqlite3
from discord.ext import commands

bot = commands.Bot(command_prefix='!')
# bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())


@bot.event
async def on_ready():
    print('Ботан на старте. Nerd on start')

    global base, cur
    base = sqlite3.connect('nerd.db')
    cur = base.cursor()
    if base:
        print('DataBase connected...OK')

@bot.command()
async def test(ctx):
    await ctx.send('туточки я')

@bot.command()
async def info(ctx, *, arg):
    await ctx.send(arg)

bot.run(os.getenv('TOKEN'))
