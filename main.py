
import discord
from discord.ext import commands

intents=discord.Intents.all()
bot = commands.Bot(command_prefix='$',intents=intents)

@bot.event
async def on_ready():
    print(">>Chemhuang is online<<")

@bot.event
async def on_member_join(member):
    channel=bot.get_channel(1051973556512231444)
    await channel.send(F'Welcome {member} join')

@bot.command()
async def ping(ctx):
    await ctx.send(F'{bot.latency*1000} ms')

@bot.command()
async def jpg(ctx):
    pic=discord.File('C:\\Users\\user\\Desktop\\裕禾2020~2022\\bobbin\\柏賓化學榜單.jpg')
    await ctx.send(File=pic)

@bot.command()
async def a17(ctx):
    await ctx.send(F'閉嘴')

@bot.command()
async def r(ctx,msg):
    await ctx.send(msg)




bot.run('OTQzMzIzMTM2NzQzNjAwMTY4.GkelDG.2GL4sDJMElXQU5QEYAghd6p2T0LzaRwSZEgdDI')