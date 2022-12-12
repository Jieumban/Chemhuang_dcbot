
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='$17',intents=None)

@bot.event
async def on_ready():
    print(">>Chemhuang is online<<")


bot.run('OTQzMzIzMTM2NzQzNjAwMTY4.Gn_qv-.GtOaBjFJ3d_NT-WlQsIM08rcOpVSdnPRIvrVYk')