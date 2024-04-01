import discord
from discord.ext import commands

import json
with open("setting.json","r",encoding="utf8") as setting_file:
    setting = json.load(setting_file)
    
import datetime
from core.classes import Cog_extension

Current_Time = datetime.datetime.now().strftime("%H:%M")
Current_seconds = datetime.datetime.now().strftime("%S")

class Setting(Cog_extension):
    
    # @commands.command()
    # async def setchannel(self,ctx,channel:int):
    #     self.channel = self.bot.get_channel(channel)
    #     await ctx.send(f"set chammel:{self.channel.mention}")
    @commands.command()
    async def setomikujitime(self,ctx,time):
        oldtime = setting["OmikujiTime"]
        setting["OmikujiTime"] = time
        newtime = setting["OmikujiTime"]
        if oldtime == newtime:
            await ctx.send(f"QAQ\n可是抽籤系統更新時間本來就是__{newtime}__了阿QQ")
        else:
            with open("setting.json","w",encoding="utf8") as setting_file:
                json.dump(setting,setting_file,indent=4)
                await ctx.send(f"已將抽籤系統更新時間從__{oldtime}__調整為__{newtime}__")









async def setup(bot):
    await bot.add_cog(Setting(bot))