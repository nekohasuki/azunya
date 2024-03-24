import discord
from discord.ext import commands
import os

import json
with open("setting.json","r",encoding="utf8") as setting_file:
    setting = json.load(setting_file)
import asyncio,random,keep_alive
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
intents = discord.Intents.all()
bot = commands.Bot(command_prefix =["a-","/",""],intents = intents)
@bot.event  #機器人登陸通知(僅後台)
async def on_ready():
    print(">>","嗨嗨嗨!! {0.user}已經成功登陸嘍!!!".format(bot),"<<")

@bot.event  #機器人登陸通知(僅後台)
async def on_ready():
    print(">>","嗨嗨嗨!! {0.user}已經成功登陸嘍!!!".format(bot),"<<")
    try:
        synced = await bot.tree.sync()
        print(f"已為您同步{len(synced)}條命令")
    except Exception as e:
        print("命令同步時發生錯誤: ", e)

@bot.command()      #加載類別
async def load(ctx,extension):
    await bot.load_extension(f"cmds.{extension}")
    await ctx.send(f"Loaded {extension} done.")

@bot.command()      #重新加載類別
async def reload(ctx,extension):
    await bot.reload_extension(f"cmds.{extension}")
    await ctx.send(f"Reloaded {extension} done.")

@bot.command()      #取消加載類別
async def unload(ctx,extension):
    await bot.unload_extension(f"cmds.{extension}")
    await ctx.send(f"Unloaded {extension} done.")







async def main():
    for Filename in  os.listdir("./cmds"):
        if Filename.endswith("py"):
            await bot.load_extension(f"cmds.{Filename[:-3]}")
    await bot.start(setting["TOKEN"])
if __name__=="__main__":
    if setting["keep_alive"] == "True":
        keep_alive.keep_alive()
        asyncio.run(main())
    elif setting["keep_alive"] == "False":
        asyncio.run(main())
    else:
        print("EROR")
