import discord
from discord.ext import commands
from discord import app_commands
import json
with open('setting.json','r',encoding='utf-8') as setting_file:
    setting = json.load(setting_file)

from core.classes import Cog_extension
import asyncio,datetime,os,random

prefix = 'r-'
class React(Cog_extension):
#指定圖片
    commandname = (f'{prefix}imege')
    @app_commands.command(name = commandname, description = '指定圖片')
    async def imege(self, interaction: discord.Interaction):
        pic = discord.File(setting['Imege'])
        await interaction.response.send_message(file = pic)
#隨機圖片/PATH
    commandname = (f'{prefix}logo')
    @app_commands.command(name = commandname, description = '隨機圖片')
    async def logo(self, interaction: discord.Interaction):
        random_pic = random.choice(setting['Logo'])
        pic = discord.File(random_pic)
        await interaction.response.send_message(file = pic)










async def setup(bot):
    await bot.add_cog(React(bot))