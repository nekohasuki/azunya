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
@bot.event  #機器人登陸通知(僅後台)
async def on_ready():
    print(">>","嗨嗨嗨!! {0.user}已經成功登陸嘍!!!".format(bot),"<<")

@bot.event  #成員加入通知
async def on_member_join(member):
    print(f'User {member} 加入了伺服器!')
    channel = bot.get_channel(int(setting["Welcome_channel"]))
    await channel.send(f'User** {member} **加入了伺服器!')

@bot.event  #成員退出通知
async def on_member_remove(member):
    print(f'User {member} 離開了伺服器!')
    channel = bot.get_channel(int(setting["Welcome_channel"]))
    await channel.send(f'User** {member} **離開了伺服器!')















    

import asyncio
async def main():
    for Filename in  os.listdir("./cmds"):
        if Filename.endswith("py"):
            await bot.load_extension(f"cmds.{Filename[:-3]}")
    await bot.start(setting["TOKEN"])
if __name__=="__main__":
    asyncio.run(main())
