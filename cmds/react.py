import discord
from discord.ext import commands
from discord import app_commands
import json
with open("setting.json","r",encoding="utf8") as setting_file:
    setting = json.load(setting_file)

from core.classes import Cog_extension
import asyncio,datetime,os,random

Current_Time = datetime.datetime.now().strftime("%H:%M")

class React(Cog_extension):
#指定圖片
    @app_commands.command(name = "imege", description = "指定圖片")
    async def imege(self, interaction: discord.Interaction):
        pic = discord.File(setting["Imege"])
        await interaction.response.send_message(file = pic)
#隨機圖片/PATH
    @app_commands.command(name = "logo", description = "隨機圖片")
    async def logo(self, interaction: discord.Interaction):
        random_pic = random.choice(setting["Logo"])
        pic = discord.File(random_pic)
        await interaction.response.send_message(file = pic)
#抽籤系統更新時間
    @app_commands.command(name = "omikujitime", description = "查詢抽籤系統更新時間")
    async def omikujitime(self, interaction: discord.Interaction):
        with open("setting.json","r",encoding="utf8") as setting_file:
            setting = json.load(setting_file)
        id = interaction.user.id
        await interaction.response.send_message(f'User：<@{id}>\n目前抽籤系統是每天的__{setting["OmikujiTime"]}__更新呦!')
#取得用戶ID
    @app_commands.command(name = "myid", description = "查詢自己的DiscordID")
    async def myid(self, interaction: discord.Interaction):
        id = interaction.user.id
        await interaction.response.send_message(f'User：<@{id}>的ID是__{id}__呦!')










async def setup(bot):
    await bot.add_cog(React(bot))