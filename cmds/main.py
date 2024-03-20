import discord
from discord.ext import commands
from core.classes import Cog_extension

class Main(Cog_Exception):
        
    @commands.command()
    async def ping(self, ctx):    #延遲
        await ctx.send(f"{round(self.bot.latency*1000)} (ms)")

def setup(bot):
    bot.add_cog(Main(bot))