import discord
from discord.ext import commands

import json
with open("setting.json","r",encoding="utf8") as setting_file:
    setting = json.load(setting_file)
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










async def setup(bot):
    await bot.add_cog(React(bot))