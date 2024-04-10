import discord
from discord.ext import commands
from discord import app_commands
import json
with open("setting.json","r",encoding="utf8") as setting_file:
    setting = json.load(setting_file)

from core.classes import Cog_extension
import asyncio,math
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
        elif count > 200:
             count = 200
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
    @app_commands.command(name = "stopwatch", description = "碼表")
    @app_commands.describe(hours="輸入小時數",minutes="輸入分鐘數",seconds="輸入秒數")
    async def stopwatch(self,interaction: discord.Interaction,hours: Optional[int] = None,minutes: Optional[int] = None,seconds: Optional[int] = None):
        if hours == None:
            hours=0
        if minutes == None:
            minutes=0
        if seconds == None:
            seconds=0
        t = (hours*60*60)+(minutes*60)+(seconds)
        if t >= 604800:
            t = 604800
        d = math.floor(t/60/60/24)
        h = math.floor(t/60/60-d*24)
        m = math.floor(t/60-h*60-d*60*24)
        s = t-d*60*60*24-h*60*60-m*60
        if d >= 1 :
            await interaction.response.send_message(f'好的User : {interaction.user.mention} !\n已將時間設定為**{int(d)}**天**{h}**時**{m}**分**{s}**秒\n開始到計時')
            message = await interaction.channel.send(f'剩餘時間 : **{int(d)}**天 **{h}**時**{m}**分**{s}**秒')
            while t > 0:
                t -=1
                d = math.floor(t/60/60/24)
                h = math.floor(t/60/60-d*24)
                m = math.floor(t/60-h*60-d*60*24)
                s = t-d*60*60*24-h*60*60-m*60
                await asyncio.sleep(1)
                await message.edit(content=f'剩餘時間 : **{int(d)}**天 **{h}**時**{m}**分**{s}**秒')
        else:
            await interaction.response.send_message(f'好的User : {interaction.user.mention} !\n已將時間設定為**{h}**時**{m}**分**{s}**秒\n開始到計時')
            message = await interaction.channel.send(f'剩餘時間 :  **{h}**時**{m}**分**{s}**秒')
            while t > 0:
                t -=1
                h = math.floor(t/60/60)
                m = math.floor(t/60-h*60)
                s = t-h*60*60-m*60
                await asyncio.sleep(1)
                await message.edit(content=f'剩餘時間 :  **{h}**時**{m}**分**{s}**秒')
        await interaction.channel.purge(check=lambda m: m.id == int(message.id))
        await interaction.channel.send(f'User：{interaction.user.mention}!!!\n之前碼表設定的時間跑完啦啦啦!!!!!')
 









#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    #以梓喵身分發送訊息
    @commands.command()
    async def say(self,ctx, *,msg):
        print(msg)
        await ctx.channel.purge(limit=1)
        await ctx.send(msg)










async def setup(bot):
    await bot.add_cog(Main(bot))