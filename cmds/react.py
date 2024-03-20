import discord
from discord.ext import commands
from core.classes import Cog_extension

import json
with open("setting.json","r",encoding="utf8") as setting_file:
    setting = json.load(setting_file)
import random

class React(Cog_extension):
    
    @commands.command()
    async def imege(self, ctx):   #指定圖片
        pic = discord.File(setting["Imege"])
        await ctx.send(file = pic)

    @commands.command()
    async def logo(self, ctx):    #隨機圖片
        random_pic = random.choice(setting["Logo"])
        pic = discord.File(random_pic)
        await ctx.send(file = pic)

def setup(bot):
    bot.add_cog(React(bot))