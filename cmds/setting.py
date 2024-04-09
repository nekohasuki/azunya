import discord
from discord.ext import commands
from discord import app_commands
import json
with open("setting.json","r",encoding="utf8") as setting_file:
    setting = json.load(setting_file)

from core.classes import Cog_extension
import datetime
from typing import Optional

Current_Time = datetime.datetime.now().strftime("%H:%M")
Current_seconds = datetime.datetime.now().strftime("%S")

class Setting(Cog_extension):
    
    # @commands.command()
    # async def setchannel(self,ctx,channel:int):
    #     self.channel = self.bot.get_channel(channel)
    #     await ctx.send(f"set chammel:{self.channel.mention}")
    #設定抽籤系統更新時間
    @app_commands.command(name = "setomikujitime", description = "設定抽籤系統更新時間(需要權限)")
    @app_commands.describe(hours="輸入小時",minutes="輸入分鐘")
    @app_commands.checks.has_permissions (administrator=True)
    async def setomikujitime(self,interaction: discord.Interaction,hours: Optional[int] = None,minutes: Optional[int] = None):
        if hours == None:
            hours = 0
        elif hours >= 23:
            hours = 23
        if minutes == None:
            minutes = 0
        elif minutes >= 59 :
            minutes = 59
        oldtime = setting["OmikujiTime"]
        setting["OmikujiTime"] = f"{hours}:{minutes}"
        newtime = setting["OmikujiTime"]
        if oldtime == newtime:
            await interaction.response.send_message(f"QAQ\n可是抽籤系統更新時間本來就是__{newtime}__了阿QQ")
        else:
            with open("setting.json","w",encoding="utf8") as setting_file:
                json.dump(setting,setting_file,indent=4)
                await interaction.response.send_message(f"已將抽籤系統更新時間從__{oldtime}__調整為__{newtime}__")










async def setup(bot):
    await bot.add_cog(Setting(bot))