import discord
from discord.ext import commands
from core.classes import Cog_extension

import json
with open("setting.json","r",encoding="utf8") as setting_file:
    setting = json.load(setting_file)
import datetime ,random

class Main(Cog_extension):
        
    @commands.command()
    async def ping(self, ctx):      #延遲
        await ctx.send(f"{round(self.bot.latency)}/s\n"  f"{round(((self.bot.latency)-round(self.bot.latency))*1000)}/ms"),
    





















async def setup(bot):
    await bot.add_cog(Main(bot))