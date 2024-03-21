import discord
from discord.ext import commands
from core.classes import Cog_extension
import json,asyncio,datetime

class Task(Cog_extension):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

#        async def interval():
#            await self.bot.wait_until_ready()
#            self.channel = self.bot.get_channel(1219815148622057523)
#            while not self.bot.is_closed():
#                await self.channel.send("Hi i'm running")
#                await asyncio.sleep(5)#5/s
#
#        self.bg_task = self.bot.loop.create_task(interval())
           
        
async def setup(bot):
    await bot.add_cog(Task(bot))