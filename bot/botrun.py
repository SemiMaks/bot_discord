import string
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

@bot.event
async def on_message(message):
    # if 'дела' in message.content.lower():
    #     await message.channel.send('норм')
    if {i.lower().translate(str.maketrans('','',string.punctuation)) for i in message.content.split(' ')}\
            .intersection() != set():
        await message.channel.send('получи бан!')
@bot.command()
# async def info(ctx, *, arg):
# захват всего текста после !info
async def info(ctx, arg=None):
    author = ctx.message.author
    if arg == None:
        await ctx.send(f'{author.mention} Введите:\n!info all\n!info pati')
    elif arg == 'all':
        await ctx.send(f'{author.mention} Я Ботан и слежу за порядком в чате. 3-е предупреждение за мат ведёт к бану!')
    elif arg == 'pati':
        await ctx.send(f'{author.mention} !test - Бот онлайн?\n!статус - мои предупреждения')
    else:
        await ctx.send(f'{author.mention} такой команды нет...')

bot.run(os.getenv('TOKEN'))
