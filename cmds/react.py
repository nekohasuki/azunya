import discord
from discord import app_commands
from discord.ext import commands
from core.classes import Cog_extension

import json
with open("setting.json","r",encoding="utf8") as setting_file:
    setting = json.load(setting_file)
import random

class React(Cog_extension):
    
    #指定圖片/PATH
    @app_commands.command(name = "imege", description = "imege!")
    async def imege(self, interaction: discord.Interaction):
        pic = discord.File(setting["Imege"])
        await interaction.response.send_message(file = pic)
    #隨機圖片
    @app_commands.command(name = "logo", description = "logo!")
    async def logo(self, interaction: discord.Interaction):      #PATH
        random_pic = random.choice(setting["Logo"])
        pic = discord.File(random_pic)
        await interaction.response.send_message(file = pic)
    #抽籤
    @app_commands.command(name = "omikuji", description = "omikuji!")
    async def omikuji(self, interaction: discord.Interaction):     #URL
        random_pic = random.choice(setting["Omikuji"])
        await interaction.response.send_message(random_pic)
   #name：命令的名稱。如果未指定，則默認為函數的名稱。
   #help：命令的幫助文本。
   #brief：命令的簡要描述。
   #usage：命令的使用方法。
   #aliases：命令的別名列表。
   #enabled：指定命令是否啟用。如果設置為False，則該命令將無法使用
   #hidden：指定命令是否隱藏。如果設置為True，則該命令將不會出現在幫助信息中。
   #rest_is_raw：指定是否將剩餘的參數作為原始字符串傳遞給命令。
   #with_app_command：指定是否將該命令作為應用程序命令（即斜槓命令）註冊。
    #@commands.command(name='hello', help='Greets the user')
    #async def hello(self,ctx,):
    #    await interaction.response.send_message("Hello!!")




async def setup(bot):
    await bot.add_cog(React(bot))