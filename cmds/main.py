import discord
from discord.ext import commands
from discord import app_commands
import json
with open("setting.json","r",encoding="utf8") as setting_file:
    setting = json.load(setting_file)

from core.classes import Cog_extension
import asyncio
from typing import Optional

class Main(Cog_extension):
    #查看延遲
    @app_commands.command(name = "ping", description = "查看延遲")
    async def ping(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"{round(self.bot.latency)}/s\n"  f"{round(((self.bot.latency)-round(self.bot.latency))*1000)}/ms"),
    #刪除訊息  
    @app_commands.command(name = "clear", description = "刪除訊息(需要權限)")
    @app_commands.describe(count="輸入數量")
    @app_commands.checks.has_permissions (administrator=True)
    async def clear(self, interaction: discord.Interaction,count: Optional[int] = None):
        user = interaction.user.id
        if count == None:
            await interaction.response.send_message(f"請輸入需要刪除的訊息數量\n參考：\n```/clear 1```")
        else:
            if count == -402:
                await interaction.response.send_message(f"請User：<@{user}>稍等片刻\n正在啟動執行402號刪除程序 ")
                await asyncio.sleep(5)
                await interaction.channel.purge(limit=1)
                deleted = await interaction.channel.purge(limit=2147483648)
                await interaction.channel.send(f'已為USER : <@{user}>刪除{len(deleted)}條訊息')
            else:
                await interaction.response.send_message(f"請User：<@{user}>稍等片刻\n正在刪除{count}項訊息")
                await asyncio.sleep(3)
                await interaction.channel.purge(limit=1)
                deleted = await interaction.channel.purge(limit=count)
                await interaction.channel.send(f'已為USER : <@{user}>刪除{len(deleted)}條訊息')
            async for message in interaction.channel.history(limit=1):
                await asyncio.sleep(5)
                await interaction.channel.purge(check=lambda m: m.id == int(message.id))
    #碼表
    @commands.command()
    async def stopwatch(self,ctx, t: int):
        await ctx.send(f'好的User : {ctx.message.author.mention} !\n已將時間設定為**{t}**秒\n開始到計時')
        message = await ctx.send(f'剩餘時間 : __ **{t}** __秒')
        while t > 0:
            t -=1
            await asyncio.sleep(1)
            await message.edit(content=f'剩餘時間 : __ **{t}** __秒')
        await ctx.channel.purge(check=lambda m: m.id == int(message.id))
        await ctx.send(f'User：{ctx.message.author.mention}!!!\n之前碼表設定的時間跑完啦啦啦!!!!!')










#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    #以梓喵身分發送訊息
    @commands.command()
    async def say(self,ctx, *,msg):
        print(msg)
        await ctx.send(msg)





        




async def setup(bot):
    await bot.add_cog(Main(bot))