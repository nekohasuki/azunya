import discord
from discord.ext import commands
from discord import app_commands
import json
with open("setting.json","r",encoding="utf8") as setting_file:
    setting = json.load(setting_file)

from core.classes import Cog_extension
import asyncio,math
from typing import Optional

class Data(Cog_extension):
#查看延遲
    @app_commands.command(name = "ping", description = "查看延遲")
    async def ping(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"{round(self.bot.latency)}/s\n"  f"{round(((self.bot.latency)-round(self.bot.latency))*1000)}/ms"),
#查詢用戶ID
    @app_commands.command(name = "myid", description = "查詢Discird的ID")
    async def myid(self,interaction:discord.Integration):
        user = interaction.user
        # await interaction.response.send_message("好的!")
        await interaction.response.send_message(f"好的!")
        message = await interaction.channel.send(f"正在查詢User：{user.mention}的資料......")
        await asyncio.sleep(3)
        await message.edit(content=f"User：<@{user.id}>\n你的ID是__{user.id}__呦!")
#查身分資料
    @app_commands.command(name = "checkrole", description = "查身分資料")
    @app_commands.describe(role = "想查的身分")
    async def checkrole(self,interaction:discord.Integration,role:Optional[str] = None):
        if role == None:
            await interaction.response.send_message("請輸入需要刪除的訊息數量\n參考：\n```/checkrole @新身分```")
        if "@" in str(f"{role}"):
            if "&" in str(f"{role}"):
                A = interaction.guild.get_role(int(f"{role[3:-1]}"))
                await interaction.response.send_message(f"# color:\n   {A.color}\n# created_at:\n    {A.created_at}\n# id:\n   {A.id}\n# members:\n  {A.members}\n# permissions:\n    {A.permissions}")
            else:
                await interaction.response.send_message(f"這好像是某位User並不是身分組")










async def setup(bot):
    await bot.add_cog(Data(bot))