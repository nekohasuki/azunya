import discord
from discord.ext import commands
from discord import app_commands
import json
with open('setting.json','r',encoding='utf8') as setting_file:
    setting = json.load(setting_file)

from core.classes import Cog_extension
import asyncio,datetime
from typing import Optional

prefix = 's-'
class Setting(Cog_extension):
#設定頻道
    # @commands.command()
    # async def setchannel(self,ctx,channel:int):
    #     self.channel = self.bot.get_channel(channel)
    #     await ctx.send(f'set chammel:{self.channel.mention}')
#設定抽籤系統更新時間
    commandname = (f'{prefix}omikujitime')
    @app_commands.command(name = commandname, description = '抽籤系統更新時間相關')
    @app_commands.describe(mod = '模式(set模式需要權限)',hours='輸入小時(查閱模式不用輸入)',minutes='輸入分鐘(查閱模式不用輸入)')
    @app_commands.choices(mod=[app_commands.Choice(name = 'check',value = 'check'),app_commands.Choice(name = 'set',value = 'set)')])
    async def omikujitime(self, interaction: discord.Interaction,mod: app_commands.Choice[str],hours: Optional[int] = None,minutes: Optional[int] = None):
        name = interaction.user.mention
        if mod.name == 'check' :
            with open('setting.json','r',encoding='utf8') as setting_file:
                setting = json.load(setting_file)
            await interaction.response.send_message(f'User：{name}\n目前抽籤系統是每天的__{setting['OmikujiTime']}__更新呦!')
        elif mod.name == 'set':
            with open('setting.json','r',encoding='utf8') as setting_file:
                setting = json.load(setting_file)
            role_list = setting['manage_messages_role']
            id = interaction.user.id
            for role in role_list:
                role_members = interaction.guild.get_role(int(f'{role}')).members
                if str(id) in str(role_members):
                    with open('setting.json','r',encoding='utf8') as setting_file:
                        setting = json.load(setting_file)
                    if hours == None:
                        hours = 0
                    elif hours >= 23:
                        hours = 23
                    if minutes == None:
                        minutes = 0
                    elif minutes >= 59 :
                        minutes = 59
                    oldtime = setting['OmikujiTime']
                    setting['OmikujiTime'] = f'{hours}:{minutes}'
                    newtime = setting['OmikujiTime']
                    if oldtime == newtime:
                        await interaction.response.send_message(f'QAQ\n可是抽籤系統更新時間本來就是__{newtime}__了阿QQ')
                    else:
                        with open('setting.json','w',encoding='utf8') as setting_file:
                            json.dump(setting,setting_file,indent=4)
                            await interaction.response.send_message(f'已將抽籤系統更新時間從__{oldtime}__調整為__{newtime}__')
                else:
                    await interaction.response.send_message(f'User：{name}你沒有權限更改喔!')
    commandname = (f'{prefix}role')
    @app_commands.command(name = commandname, description = '添加/移除身分')
    @app_commands.describe(mod = '模式(需要權限)',role='輸入身分',user='輸入用戶')
    @app_commands.choices(mod=[app_commands.Choice(name = 'add',value = 'add'),app_commands.Choice(name = 'remove',value = 'remove)')])
    async def relo(self,interaction:discord.Integration,mod: app_commands.Choice[str],role: Optional[str] = None,user: Optional[str] = None):
        name = f'__`{interaction.user.global_name}`__'
        role_id = role[3:-1]
        user_id = user[2:-1]
        if mod.name == "add":
            if user == None and role == None:
                await interaction.response.send_message(f'輸入想要給予的身分及提及該用戶\n參考：\n```/s-roleset add @新身分 @新用戶```')
            elif role == None:
                await interaction.response.send_message(f'請輸入要給予的身分')
            elif user == None:
                await interaction.response.send_message(f'請提及要給予身分的用戶')
            else:    
                if "@" not in str(role):
                    await interaction.response.send_message(f'User：{name}請問...\nrole參數裡你放了甚麼??')
                else:
                    if "&" not in str(role):
                        await interaction.response.send_message(f'這好像是某位User並不是身分組')
                if "@" not in str(user):
                    await interaction.response.send_message(f'User：{name}請問...\nuser參數裡你放了甚麼??')
                else:
                    if "&" in str(user):
                        await interaction.response.send_message(f'這好像是某個身分組並不是某位User')
                    else:
                        count = 0
                        role_list = setting['MOD_role']
                        id = interaction.user.id
                        for role in role_list:
                            if count == 1:
                                break
                            role_members = interaction.guild.get_role(int(f'{role}')).members
                            if str(id) in str(role_members):
                                user = interaction.guild.get_member(int(user_id))
                                role = interaction.guild.get_role(int(role_id))
                                msg = await user.add_roles(role)
                                if msg == None:
                                    count += 1
                                    await interaction.response.send_message(f'已為__`{user.name}`__添加身分：@{role.name}')
                        if count == 0:
                            await interaction.response.send_message(f'沒有權限')
        if mod.name == "remove":
            if user == None and role == None:
                await interaction.response.send_message(f'輸入想要移除的身分及提及該用戶\n參考：\n```/s-roleset remove @新身分 @新用戶```')
            elif role == None:
                await interaction.response.send_message(f'請輸入要移除的身分')
            elif user == None:
                await interaction.response.send_message(f'請提及要移除身分的用戶')
            else:
                if "@" not in str(role):
                    await interaction.response.send_message(f'User：{name}請問...\nrole參數裡你放了甚麼??')
                else:
                    if "&" not in str(role):
                        await interaction.response.send_message(f'這好像是某位User並不是身分組')
                if "@" not in str(user):
                    await interaction.response.send_message(f'User：{name}請問...\nuser參數裡你放了甚麼??')
                else:
                    count = 0
                    if "&" in str(user):
                        await interaction.response.send_message(f'這好像是某個身分組並不是某位User')
                    else:
                        count = 0
                        role_list = setting['MOD_role']
                        id = interaction.user.id
                        for role in role_list:
                            if count == 1:
                                break
                            role_members = interaction.guild.get_role(int(f'{role}')).members
                            if str(id) in str(role_members):
                                user = interaction.guild.get_member(int(user_id))
                                role = interaction.guild.get_role(int(role_id))
                                msg = await user.remove_roles(role)
                                if msg == None:
                                    count += 1
                                    await interaction.response.send_message(f'已為__`{user.name}`__移除身分：@{role.name}')
                        if count == 0:
                            await interaction.response.send_message(f'沒有權限')




async def setup(bot):
    await bot.add_cog(Setting(bot))