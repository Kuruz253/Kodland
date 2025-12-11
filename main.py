import random
import discord
from discord.ext import commands
from bot_logic import gen_pass
# Zmienna intents przechowuje uprawnienia bota
intents = discord.Intents.default()
# Włączanie uprawnienia do czytania wiadomości
intents.message_content = True
# Tworzenie bota w zmiennej client i przekazanie mu uprawnień
bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')
@bot.command()
async def hello(ctx):
    await ctx.send(f"Cześć, jestem bot {bot.user}")
@bot.command()
async def haslo(ctx):
    await ctx.send(gen_pass(10))

@bot.command()
async def roll(ctx, dice: str):
    
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)



bot.run("Token")
