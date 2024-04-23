import discord
from discord.ext import commands
from discord import app_commands
import json
with open('setting.json','r',encoding='utf8') as setting_file:
    setting = json.load(setting_file)

from core.classes import Cog_extension
from typing import Optional

prefix = 'p-'
class Point(Cog_extension):
#查看指定用戶點數
    commandname = (f'{prefix}checkpoint')
    @app_commands.command(name = commandname, description = '查看指定用戶點數')
    async def checkpoint(self,interaction:discord.Integration):
        pass
#給予指定用戶點數
    commandname = (f'{prefix}givepoint')
    @app_commands.command(name = commandname, description = '給予指定用戶點數')
    @app_commands.describe(user='輸入用戶', count='輸入數量')
    async def givepoint(self,interaction:discord.Integration,user: Optional[str] = None, count: Optional[int] = None):
        if "@" in user:
            if "&" not in user:
                if count == None:
                    count = 0
                count = abs(count)
                userA = interaction.user
                userB = interaction.guild.get_member(int(user[2:-1]))
                with open('cmds\\data\\user_data.json','r',encoding='utf8') as UserDataFile:
                    userdata = json.load(UserDataFile)
                if count <= userdata[f"{userA.id}"]['point']['now_count']:
                #抓取資料
                    userdata_updata_A = userdata[f"{userA.id}"]
                    now_count_A = userdata_updata_A['point']['now_count']
                    history_count_A = userdata_updata_A['point']['history_count']
                    userdata_updata_B = userdata[f"{userB.id}"]
                    now_count_B = userdata_updata_B['point']['now_count']
                    history_count_B = userdata_updata_B['point']['history_count']
                #刷入資料
                    userdata_updata_A['point']['now_count'] = int(now_count_A) - count
                    userdata_updata_A['point']['history_count'] = int(history_count_A) - count
                    userdata_updata_B['point']['now_count'] = int(now_count_B) + count
                    userdata_updata_B['point']['history_count'] = int(history_count_B) + count
                #更新資料
                    userdata.update(userdata_updata_A)
                    userdata.update(userdata_updata_B)
                    with open('cmds\\data\\user_data.json','w',encoding='utf8') as UserDataFile:
                        json.dump(userdata,UserDataFile,indent=4)
                    await interaction.response.send_message(f'User：{userA.mention}給予了User：{userB.mention}**{count}**點')
                else:
                    await interaction.response.send_message(f'User：{userA.mention}\n你的點數似乎不夠喔')
            else:
                await interaction.response.send_message(f'這好像是某個身分組並不是某位User')
        else:
            await interaction.response.send_message(f'User：__{interaction.user.global_name}__ 請問...\nuser參數裡你放了甚麼??')
#查看自己點數
    commandname = (f'{prefix}mypoint')
    @app_commands.command(name = commandname, description = '查看自己點數')
    async def mypoint(self,interaction:discord.Integration):
        pass
#添加點數給指定用戶
    commandname = (f'{prefix}point')
    @app_commands.command(name = commandname, description = '添加點數給指定用戶')
    @app_commands.describe(mod = '模式(需要權限)', user='輸入用戶', count='輸入數量')
    @app_commands.choices(mod=[app_commands.Choice(name = 'add',value = 'add'),app_commands.Choice(name = 'remove',value = 'remove)')])
    async def point(self,interaction:discord.Integration,mod: app_commands.Choice[str],user: Optional[str] = None, count: Optional[int] = None):        
        with open('setting.json','r',encoding='utf8') as setting_file:
            setting = json.load(setting_file)
        role_list = setting['MOD_roles']
        id = interaction.user.id
        counter = 0
        if count == None:
            count = 0
        for role in role_list:
            if counter == 1:
                break
            role_members = interaction.guild.get_role(int(f'{role}')).members
            if str(id) in str(role_members):
                counter += 1
                if "@" in user:
                    if "&" not in user:
                        user_id = user[2:-1]
                        user = interaction.guild.get_member(int(user[2:-1]))
                        if interaction.user != user:
                            if interaction.user.top_role.position >= user.top_role.position:
                                count = abs(count)
                            #添加點數
                                if mod.name == "add":
                                    with open('cmds\\data\\user_data.json','r',encoding='utf8') as UserDataFile:
                                        userdata = json.load(UserDataFile)
                                #抓取資料
                                    userdata_updata = userdata[f"{user_id}"]
                                    now_count = userdata_updata['point']['now_count']
                                    history_count = userdata_updata['point']['history_count']
                                #刷入資料
                                    userdata_updata['point']['now_count'] = int(now_count) + count
                                    userdata_updata['point']['history_count'] = int(history_count) + count
                                #更新資料
                                    userdata.update(userdata_updata)
                                    with open('cmds\\data\\user_data.json','w',encoding='utf8') as UserDataFile:
                                        json.dump(userdata,UserDataFile,indent=4)
                                    await interaction.response.send_message(f'已為User：{user.mention}添加了**{count}**點')
                            #移除點數                                
                                if mod.name == "remove":
                                    with open('cmds\\data\\user_data.json','r',encoding='utf8') as UserDataFile:
                                        userdata = json.load(UserDataFile)
                                #抓取資料
                                    userdata_updata = userdata[f"{user_id}"]
                                    now_count = userdata_updata['point']['now_count']
                                    history_count = userdata_updata['point']['history_count']
                                #刷入資料
                                    userdata_updata['point']['now_count'] = int(now_count) - count
                                    userdata_updata['point']['history_count'] = int(history_count) - count
                                #更新資料
                                    userdata.update(userdata_updata)
                                    with open('cmds\\data\\user_data.json','w',encoding='utf8') as UserDataFile:
                                        json.dump(userdata,UserDataFile,indent=4)
                                    await interaction.response.send_message(f'已為User：{user.mention}移除了**{count}**點')
                            else:
                                await interaction.response.send_message(f'沒有權限')
                        else:
                            await interaction.response.send_message(f'指令無法對自己使用')
                    else:
                        await interaction.response.send_message(f'這好像是某個身分組並不是某位User')
                else:
                    await interaction.response.send_message(f'User：__{interaction.user.global_name}__ 請問...\nuser參數裡你放了甚麼??')

        if counter == 0:
            await interaction.response.send_message(f'沒有權限')










async def setup(bot):
    await bot.add_cog(Point(bot))