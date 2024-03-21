import discord
from discord import app_commands
from discord.ext import commands
from core.classes import Cog_extension

import json
with open("setting.json","r",encoding="utf8") as setting_file:
    setting = json.load(setting_file)
import datetime ,random

class Main(Cog_extension):

    # name指令顯示名稱，description指令顯示敘述
    # name的名稱，中、英文皆可，但不能使用大寫英文

    #查看延遲
    @app_commands.command(name = "ping", description = "ping!")

    async def ping(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"{round(self.bot.latency)}/s\n"  f"{round(((self.bot.latency)-round(self.bot.latency))*1000)}/ms"),

    #回覆使用者訊息
    @app_commands.command(name = "hello", description = "Hello, world!")
    async def hello(self, interaction: discord.Interaction):
        await interaction.response.send_message("Hello, world!")

        #@app_commands.command(name = "say", description = "say msg")
        ##以梓喵身分發送訊息
        #async def say(self,interaction: discord.Interaction, *,msg):
        #    await interaction.response.message.delete()
        #    await interaction.response.send_message(msg)
    @commands.command()
    async def say(self,ctx, *,msg):
        await ctx.message.delete()
        await ctx.send(msg)

    @commands.command()
    async def clear(self,ctx,num:int):
        member = self.bot.get_user(id(int))
        deleted = await ctx.channel.purge(limit=num+1)
        await ctx.channel.send(f'已為USER:{member}刪除{len(deleted)-1}條訊息')


async def setup(bot):
    await bot.add_cog(Main(bot))