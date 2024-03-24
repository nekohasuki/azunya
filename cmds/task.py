import discord
from discord.ext import commands
from core.classes import Cog_extension
import json,asyncio,datetime

class Task(Cog_extension):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

#        async def interval():
#            await self.bot.wait_until_ready()
#            self.channel = self.bot.get_channel(1221262279484510310)
#            while not self.bot.is_closed():
#                await self.channel.send("Hi i'm running")
#                await asyncio.sleep(5)#單位:秒
#        self.bg_task = self.bot.loop.create_task(interval())
#    @commands.command()
#    async def setchannel(self,ctx,channel_id:int):
#        self.channel = self.bot.get_channel(channel_id)
#        await ctx.sand(f"Set channel:{self.channel.mention}")







async def setup(bot):
    await bot.add_cog(Task(bot))