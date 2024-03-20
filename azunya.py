import discord
from discord.ext import commands

bot = commands.Bot(command_prefix =["a-","/"])

@bot.event
async def on_ready():
    print(">>","嗨嗨嗨!! {0.user}已經成功登陸嘍!!!".format(bot),"<<")
