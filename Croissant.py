from random import choice

import discord
from discord.ext import commands
from resources import images

bot = commands.Bot(command_prefix=['🥐', 'croissant! ', 'kwah-saunh '], description="Croissants!")


@bot.event
async def on_ready():
    print(f'{bot.user.name}\n{bot.user.id}\nIn {len(bot.guilds)} servers')


@bot.command()
async def aretheyhot(ctx):
    """Checks if the Croissants are hot!"""
    await ctx.send('Yes the Croissants are hot!!')


@bot.command()
async def croissant(ctx):
    """Croissant!!"""
    embed = discord.Embed(description=("**Croissants!**"))
    embed.set_image(url=choice(images.croissants))
    await ctx.send(embed=embed)


bot.run('croissant')
