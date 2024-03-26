import discord
from discord.ext import commands

import json
with open("setting.json","r",encoding="utf8") as setting_file:
    setting = json.load(setting_file)
import datetime ,random

from core.classes import Cog_extension

class Main(Cog_extension):
    #查看延遲
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"{round(self.bot.latency)}/s\n"  f"{round(((self.bot.latency)-round(self.bot.latency))*1000)}/ms"),
    #回覆使用者訊息
    @commands.command()
    async def hello(self, ctx):
        await ctx.send("Hello, world!")
    #以梓喵身分發送訊息
    @commands.command()
    async def say(self,ctx, *,msg):
        await ctx.send(msg)
        await ctx.message.delete()
    #刪除訊息
    @commands.command()
    async def clear(self,ctx,count:int):
        member = self.bot.get_user(id(int))
        deleted = await ctx.channel.purge(limit=count+1)
        await ctx.channel.send(f'已為USER:{member}刪除{len(deleted)-1}條訊息')










async def setup(bot):
    await bot.add_cog(Main(bot))