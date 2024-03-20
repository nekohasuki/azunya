import discord
from discord.ext import commands


import json
with open("setting.json","r",encoding="utf8") as setting_file:
    setting = json.load(setting_file)





#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
intents = discord.Intents.all()
bot = commands.Bot(command_prefix =["a-","/"], intents = intents)
@bot.event
async def on_ready():
    print(">>","嗨嗨嗨!! {0.user}已經成功登陸嘍!!!".format(bot),"<<")


bot.run(setting["TOKEN"])