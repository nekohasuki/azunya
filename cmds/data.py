import discord
from discord.ext import commands
from discord import app_commands
import json
with open('setting.json','r',encoding='utf-8') as setting_file:
    setting = json.load(setting_file)

from core.classes import Cog_extension
import asyncio,datetime,math
from typing import Optional

prefix = 'd-'
class Data(Cog_extension):
#查詢梓守的資料
    commandname = (f'{prefix}azudata')
    @app_commands.command(name = commandname, description = "查詢梓守的資料")
    async def azudata(self,interaction:discord.Interaction):
        with open("setting.json","r",encoding="utf-8") as setting_file:
            setting = json.load(setting_file)
        t = int(setting["onlinetime"])
        d = math.floor(t/60/60/24)
        H = math.floor(t/60/60-d*24)
        M = math.floor(t/60-H*60-d*60*24)
        S = t-M*60-H*60*60-d*60*60*24
        HMS = f"{H}:{M}:{S}"
        created_at = self.bot.user.created_at + datetime.timedelta(hours=8)
        created_at_y = created_at.strftime('%y')
        created_at_m = created_at.strftime('%m')
        created_at_d = created_at.strftime('%d')
        setuptime = (f'{int(created_at_y)}年{int(created_at_m)}月{int(created_at_d)}日')
        guilds = len(self.bot.guilds)
        counter =10
        await interaction.response.send_message(f"想要查看梓守我的資料是嗎?\n讓我想想喔...")
        await asyncio.sleep(1)
        if d >= 1:
            while counter > 0:
                counter -= 1
                with open("setting.json","r",encoding="utf-8") as setting_file:
                    setting = json.load(setting_file)
                t = int(setting["onlinetime"])
                d = math.floor(t/60/60/24)
                H = math.floor(t/60/60-d*24)
                M = math.floor(t/60-H*60-d*60*24)
                S = t-M*60-H*60*60-d*60*60*24
                HMS = f"{H}:{M}:{S}"
                await asyncio.sleep(1)
                await interaction.edit_original_response(content=f"梓守上線了**{d}天又{HMS}**這麼久`({counter}/s)`\n梓守是在**{setuptime}**建立\n梓守是<@938100109240074310>寫的\n目前有**{guilds}**個伺服器能看到梓守\n[__**邀請梓守按這裡!!!**__](https://reurl.cc/MRknq3)")
        else:
            while counter > 0:
                counter -= 1
                with open("setting.json","r",encoding="utf-8") as setting_file:
                    setting = json.load(setting_file)
                t = int(setting["onlinetime"])
                d = math.floor(t/60/60/24)
                H = math.floor(t/60/60-d*24)
                M = math.floor(t/60-H*60-d*60*24)
                S = t-M*60-H*60*60-d*60*60*24
                HMS = f"{H}:{M}:{S}"
                await asyncio.sleep(1)
                await interaction.edit_original_response(content=f"梓守上線了**{HMS}**這麼久`({counter}/s)`\n梓守是在**{setuptime}**建立\n梓守是<@938100109240074310>寫的\n目前有**{guilds}**個伺服器能看到梓守\n[__**邀請梓守按這裡!!!**__](https://reurl.cc/MRknq3)")
#查身分組資料
    commandname = (f'{prefix}checkrole')
    @app_commands.command(name = commandname, description = '查身分資料')
    @app_commands.describe(role = '想查的身分')
    async def checkrole(self,interaction:discord.Interaction,role:Optional[str] = None):
        if role == None:
            await interaction.response.send_message('請輸入需要查詢的訊息數量\n參考：\n```/checkrole @新身分```')
        if '@' in str(f'{role}'):
            if '&' in str(f'{role}'):
                data = interaction.guild.get_role(int(f'{role[3:-1]}'))
                await interaction.response.send_message(f'# color:\n   {data.color}\n# created_at:\n    {data.created_at}\n# id:\n   {data.id}\n# members:\n  {data.members}\n# position:\n    {data.position}')
            else:
                await interaction.response.send_message(f'這好像是某位User並不是身分組')
#查詢用戶ID
    commandname = (f'{prefix}myid')
    @app_commands.command(name = commandname, description = '查詢Discird的ID')
    async def myid(self,interaction:discord.Interaction):
        user = interaction.user
        await interaction.response.send_message(f'正在查詢User：{user.mention}的資料......')
        await asyncio.sleep(1)
        await interaction.edit_original_response(content=f'User：<@{user.id}>\n你的ID是__{user.id}__呦!')
#查看延遲
    commandname = (f'{prefix}ping')
    @app_commands.command(name = commandname, description = '查看延遲')
    async def ping(self, interaction: discord.Interaction):
        await interaction.response.send_message(f'正在計算延遲......')
        await asyncio.sleep(2)
        await interaction.edit_original_response(content=f'{round(self.bot.latency)}/s\n'  f'{round(((self.bot.latency)-round(self.bot.latency))*1000)}/ms'),
#查詢伺服器的資料
    commandname = (f'{prefix}serverdata')
    @app_commands.command(name = commandname, description = '查詢伺服器的資料')
    async def serverdata(self,interaction:discord.Interaction):
        guild = interaction.guild
        members = interaction.guild.member_count
        await interaction.response.send_message(f'正在查看......')
        await asyncio.sleep(round(members/2))
        await interaction.edit_original_response(content=f'伺服器名稱：**{guild}**\n用戶數：**{members}**人')
#查詢用戶頭像
    commandname = (f'{prefix}myavatar')
    @app_commands.command(name = commandname, description = '查詢Discird的頭像')
    async def myavatar(self,interaction:discord.Interaction):
        user = interaction.user
        await interaction.response.send_message(f'正在查詢User：{user.mention}的資料......')
        await asyncio.sleep(1)
        await interaction.edit_original_response(content=f'User：<@{user.id}>\n你的頭像是__[這個]({user.display_avatar})__呦!')








    commandname = (f'{prefix}name')
    @app_commands.command(name = commandname, description = '這是一段描述')
    async def name(self,interaction:discord.Interaction):
        user = interaction.guild.get_member(1010770145150517278)
        # await interaction.response.send_message(f'正在查詢User：{user}的資料......')
        await interaction.response.send_message(f'正在查詢User：{user.mention}的資料......')
        await asyncio.sleep(1)
        await interaction.edit_original_response(content=f'User：<@{user.id}>\n你的頭像是__[這個]({user.display_avatar})__呦!')

  
        # await interaction.response.send_message(f'123')
        # asyncio.sleep(1)
        # await interaction.edit_original_response(content=f'1234567890')
        # await interaction.response.send_message(f'{interaction.guild.create_category_channel}\n ** **\n** ** create_category_channel\n ** **\n** **{interaction.guild.id}\n ** **\n** ** id\n ** **\n** **{interaction.guild.members}\n ** **\n** ** members\n ** **\n** **{interaction.guild.member_count}\n ** **\n** ** member_count\n ** **\n** **{interaction.guild.owner_id}\n ** **\n** ** owner_id\n ** **\n** **{interaction.guild.preferred_locale}\n ** **\n** ** preferred_locale\n ** **\n** **{interaction.guild.roles}\n ** **\n** ** roles\n ** **\n** **')










async def setup(bot):
    await bot.add_cog(Data(bot))