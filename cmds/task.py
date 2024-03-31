import discord
from discord.ext import commands

import json
with open("setting.json","r",encoding="utf8") as setting_file:
    setting = json.load(setting_file)
    
import asyncio,datetime

Current_Time = datetime.datetime.now().strftime("%H:%M")
Current_seconds = datetime.datetime.now().strftime("%S")

from core.classes import Cog_extension

class Task(Cog_extension):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        async def omikuji():       
                await self.bot.wait_until_ready()
                channel = self.bot.get_channel(1219180207534243894)
                if Current_Time == ("06:16"):
                    while not self.bot.is_closed():
                        await channel.send(Current_seconds)
                        await asyncio.sleep(1)#單位:秒
        self.bg_task = self.bot.loop.create_task(omikuji())


# Clock = 0
# if Current_Time == ("18:00"):
#     Clock == 1
# if Current_Time == ("18:01") and Clock == 0:
#     # 清空 history.json
        
#     Clock += 1







async def setup(bot):
    await bot.add_cog(Task(bot))