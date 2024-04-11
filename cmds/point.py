import discord
from discord.ext import commands
from discord import app_commands
import json
with open('setting.json','r',encoding='utf8') as setting_file:
    setting = json.load(setting_file)

from core.classes import Cog_extension

class Point(Cog_extension):
    pass
async def setup(bot):
    await bot.add_cog(Point(bot))