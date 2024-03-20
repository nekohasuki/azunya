import discord
from discord.ext import commands
import os

import json
with open("setting.json","r",encoding="utf8") as setting_file:
    setting = json.load(setting_file)
import random
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
intents = discord.Intents.all()
bot = commands.Bot(command_prefix =["a-","/",""], intents = intents)
@bot.event
async def on_ready():
    print(">>","嗨嗨嗨!! {0.user}已經成功登陸嘍!!!".format(bot),"<<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(int(setting["Welcome_channel"]))
    await channel.send(f"{member} join!")
    
@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(int(setting["Welcome_channel"]))
    await channel.send(f"{member} leave!")
    

import asyncio
async def main():
    for Filename in  os.listdir("./cmds"):
        if Filename.endswith("py"):
            await bot.load_extension(f"cmds.{Filename[:-3]}")
    await bot.start(setting["TOKEN"])
if __name__=="__main__":
    asyncio.run(main())
