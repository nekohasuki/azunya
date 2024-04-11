import discord
from discord.ext import commands
from discord import app_commands
import json
with open('setting.json','r',encoding='utf8') as setting_file:
    setting = json.load(setting_file)

from core.classes import Cog_extension
import asyncio,math
from typing import Optional

prefix = 'd-'
class Data(Cog_extension):
#查詢梓守的資料
    commandname = (f'{prefix}azudata')
    @app_commands.command(name = commandname, description = '查詢梓守的資料')
    async def azudata(self,interaction:discord.Integration):
        with open('setting.json','r',encoding='utf8') as setting_file:
            setting = json.load(setting_file)
        t = int(setting['onlinetime'])
        d = math.floor(t/60/60/24)
        H = math.floor(t/60/60-d*24)
        M = math.floor(t/60-H*60-d*60*24)
        S = t-M*60-H*60*60-d*60*60*24
        HMS = f'{H}:{M}:{S}'

#查身分資料
    commandname = (f'{prefix}checkrole')
    @app_commands.command(name = commandname, description = '查身分資料')
    @app_commands.describe(role = '想查的身分')
    async def checkrole(self,interaction:discord.Integration,role:Optional[str] = None):
        if role == None:
            await interaction.response.send_message('請輸入需要查詢的訊息數量\n參考：\n```/checkrole @新身分```')
        if '@' in str(f'{role}'):
            if '&' in str(f'{role}'):
                data = interaction.guild.get_role(int(f'{role[3:-1]}'))
                await interaction.response.send_message(f'# color:\n   {data.color}\n# created_at:\n    {data.created_at}\n# id:\n   {data.id}\n# members:\n  {data.members}\n# permissions:\n    {data.permissions}')
            else:
                await interaction.response.send_message(f'這好像是某位User並不是身分組')
#查詢用戶ID
    commandname = (f'{prefix}myid')
    @app_commands.command(name = commandname, description = '查詢Discird的ID')
    async def myid(self,interaction:discord.Integration):
        user = interaction.user
        # await interaction.response.send_message('好的!')
        await interaction.response.send_message(f'好的!')
        message = await interaction.channel.send(f'正在查詢User：{user.mention}的資料......')
        await asyncio.sleep(3)
        await message.edit(content=f'User：<@{user.id}>\n你的ID是__{user.id}__呦!')
#查看延遲
    commandname = (f'{prefix}ping')
    @app_commands.command(name = commandname, description = '查看延遲')
    async def ping(self, interaction: discord.Interaction):
        await interaction.response.send_message(f'{round(self.bot.latency)}/s\n'  f'{round(((self.bot.latency)-round(self.bot.latency))*1000)}/ms'),

#///////////////////////////////////////////////////////////////////////////////////////////////////////

        setuptime = '某天(set)'
        channels = '2(set)'

#///////////////////////////////////////////////////////////////////////////////////////////////////////

        count =10
        await interaction.response.send_message(f'**__底下跑動時間僅顯示{count}秒__**')
        message = await interaction.channel.send(f'梓守上線了**{d}:{HMS}**這麼久\n梓守是在**{setuptime}**建立\n梓守是<@938100109240074310>寫的\n目前有**{channels}**個伺服器能看到梓守\n[__**邀請梓守按這裡!!!**__](https://reurl.cc/MRknq3)')
        if d >= 1:
            while count > 0:
                count -= 1
                with open('setting.json','r',encoding='utf8') as setting_file:
                    setting = json.load(setting_file)
                t = int(setting['onlinetime'])
                d = math.floor(t/60/60/24)
                H = math.floor(t/60/60-d*24)
                M = math.floor(t/60-H*60-d*60*24)
                S = t-M*60-H*60*60-d*60*60*24
                HMS = f'{H}:{M}:{S}'
                await asyncio.sleep(1)
                await message.edit(content=f'梓守上線了**{d}:{HMS}**這麼久\n梓守是在**{setuptime}**建立\n梓守是<@938100109240074310>寫的\n目前有**{channels}**個伺服器能看到梓守\n[__**邀請梓守按這裡!!!**__](https://reurl.cc/MRknq3)')
        else:
            while count > 0:
                count -= 1
                with open('setting.json','r',encoding='utf8') as setting_file:
                    setting = json.load(setting_file)
                t = int(setting['onlinetime'])
                d = math.floor(t/60/60/24)
                H = math.floor(t/60/60-d*24)
                M = math.floor(t/60-H*60-d*60*24)
                S = t-M*60-H*60*60-d*60*60*24
                HMS = f'{H}:{M}:{S}'
                await asyncio.sleep(1)
                await message.edit(content=f'梓守上線了**{HMS}**這麼久\n梓守是在**{setuptime}**建立\n梓守是<@938100109240074310>寫的\n目前有**{channels}**個伺服器能看到梓守\n[__**邀請梓守按這裡!!!**__](https://reurl.cc/MRknq3)')
#查詢伺服器的資料
    commandname = (f'{prefix}serverdata')
    @app_commands.command(name = commandname, description = '查詢伺服器的資料')
    async def serverdata(self,interaction:discord.Integration):
        guild = interaction.guild

#///////////////////////////////////////////////////////////////////////////////////////////////////////

        members = '未知(set)'

#///////////////////////////////////////////////////////////////////////////////////////////////////////

        await interaction.response.send_message(f'伺服器名稱：**{guild}**\n用戶數：**{members}**人')










async def setup(bot):
    await bot.add_cog(Data(bot))