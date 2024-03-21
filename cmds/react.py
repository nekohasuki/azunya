import discord
from discord.ext import commands
from core.classes import Cog_extension

import json
with open("setting.json","r",encoding="utf8") as setting_file:
    setting = json.load(setting_file)
import random

class React(Cog_extension):
    
    @commands.command()     #指定圖片
    async def imege(self,ctx):     #PATH
        pic = discord.File(setting["Imege"])
        await ctx.send(file = pic)

    @commands.command()     #隨機圖片
    async def logo(self,ctx):      #PATH
        random_pic = random.choice(setting["Logo"])
        pic = discord.File(random_pic)
        await ctx.send(file = pic)

    @commands.command()     #抽籤
    async def omikuji(self,ctx):     #URL
        random_pic = random.choice(setting["Omikuji"])
        await ctx.send(random_pic)


async def setup(bot):
    await bot.add_cog(React(bot))