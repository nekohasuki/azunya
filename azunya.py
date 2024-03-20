import json
with open("setting.json","r",encoding="utf8") as setting_file:
    setting = json.load(setting_file)
import discord
from discord.ext import commands
import random
import asyncio
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
intents = discord.Intents.all()
bot = commands.Bot(command_prefix = "/", intents = intents)
@bot.event
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

#指令
@bot.command() 
async def zping(ctx):    #延遲
    await ctx.send(f"{round(bot.latency)}/s\n"  f"{round(((bot.latency)-round(bot.latency))*1000)}/ms"),
@bot.command()
async def imege(ctx):   #指定圖片
    pic = discord.File(setting["Imege"])
    await ctx.send(file = pic)
@bot.command()
async def logo(ctx):    #隨機圖片
    random_pic = random.choice(setting["Logo"])
    pic = discord.File(random_pic)
    await ctx.send(file = pic)
@bot.command()
async def omikuji(ctx):    #抽籤
    random_pic = random.choice(setting["Omikuji"])
    await ctx.send(random_pic)








bot.run(setting["TOKEN"])