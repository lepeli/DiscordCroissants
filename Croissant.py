import discord
from discord.ext import commands
import glob
import random
import os
from PIL import Image


bot = commands.Bot(command_prefix='Croissant! ', description="Croissants!")

Croissantimg = ['https://alexa.moe/2nDjV.png', 'https://alexa.moe/rTahn.png', 'https://alexa.moe/oV4Os.png', 'https://alexa.moe/fEPJB.png', 'https://alexa.moe/KaHyj.png', 'https://alexa.moe/yXpYN.png', 'https://alexa.moe/RJgk3.png']

@bot.event
async def on_ready():
    print(bot.user.name)
    print(bot.user.id)
    print(len(bot.guilds))

@bot.command()
async def aretheyhot(ctx):
    """Checks if the Croissants are hot!"""
    await ctx.send('Yes the Croissants are hot!!')

@bot.command()
async def croissant(ctx):
    """Croissant!!"""
    embed = discord.Embed(description=("**Croissants!**"))
    embed.set_image(url=random.choice(Croissantimg))
    await ctx.send(embed=embed)

bot.run('YOUR TOKEN GOES HERE')
