import discord
from discord.ext import commands
from core.classes import Cog_extension

import json
with open("setting.json","r",encoding="utf8") as setting_file:
    setting = json.load(setting_file)
import datetime ,random

class Main(Cog_extension):
        
    @commands.command()
    async def ping(self,ctx):      #延遲
        await ctx.send(f"{round(self.bot.latency)}/s\n"  f"{round(((self.bot.latency)-round(self.bot.latency))*1000)}/ms"),
    




















    @commands.command()
    async def say(self,ctx, *,msg):
        await ctx.message.delete()
        await ctx.send(msg)

    @commands.command()
    async def clear(self,ctx,num:int):
        member = self.bot.get_user(id(int))
        deleted = await ctx.channel.purge(limit=num+1)
        await ctx.channel.send(f'已為USER:{member}刪除{len(deleted)-1}條訊息')


async def setup(bot):
    await bot.add_cog(Main(bot))