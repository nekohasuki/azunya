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










async def setup(bot):
    await bot.add_cog(Data(bot))