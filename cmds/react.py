import discord
from discord.ext import commands

import json
with open("setting.json","r",encoding="utf8") as setting_file:
    setting = json.load(setting_file)
with open("cmds\history.json","r",encoding="utf8") as history_file:
    history = json.load(history_file)

import random,datetime

from core.classes import Cog_extension

Current_Time = datetime.datetime.now().strftime("%H:%M")

class React(Cog_extension):
    #指定圖片/PATH
    @commands.command()
    async def imege(self, ctx):
        pic = discord.File(setting["Imege"])
        await ctx.send(file = pic)
    #隨機圖片/PATH
    @commands.command()
    async def logo(self, ctx):
        random_pic = random.choice(setting["Logo"])
        pic = discord.File(random_pic)
        await ctx.send(file = pic)
    #抽籤/URL
    @commands.command()
    async def omikuji(self, ctx):
        random_pic = random.choice(setting["Omikuji"])
        await ctx.send(random_pic)
    #取得用戶ID
    @commands.command()
    async def myid(self,ctx):
        user = ctx.author
        id = user.id
        name = user.name
        await ctx.send(f'User：<@{id}>的ID是{id}呦!')























    @commands.command()
    async def ttt(self,ctx):
        guild = ctx.guild
        channel = ctx.channel
        user = ctx.author.id
        if "history.json" != "history.json":
            await ctx.send(f"User : <@{user}>\n你今天已經抽過了啦!\n[點我看抽到的籤]({setting["Embed"]})")
        else:
            random_pic = random.choice(setting["Omikuji"])
            await ctx.send(random_pic)
            await ctx.send(f"{user}")
            # await ctx.send(f"[{guild}]|[{channel}]|[{user}]")
























async def setup(bot):
    await bot.add_cog(React(bot))