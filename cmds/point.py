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
    commandname = (f'{prefix}point')
    @app_commands.command(name = commandname, description = 'Ponit點數相關')
    @app_commands.describe(mod = '模式(需要權限)', user='輸入用戶', count='輸入數量')
    @app_commands.choices(mod=[app_commands.Choice(name = 'add',value = 'add'),app_commands.Choice(name = 'remove',value = 'remove)')])
    async def point(self,interaction:discord.Integration,mod: app_commands.Choice[str],user: Optional[str] = None, count: Optional[int] = None):
        role_list = ['1219645881838600293','1219645880831971408','1219645862502731876']
        id = interaction.user.id
        counter = 0
        for role in role_list:
            if counter == 1:
                break
            role_members = interaction.guild.get_role(int(f'{role}')).members
            if str(id) in str(role_members):
                counter += 1
                count = abs(count)
                
                
                
                
                
                
                
                if mod.name == "add":
                    await interaction.response.send_message(f'為User：{user}添加了{count}點')
                    


                if mod.name == "remove":
                    await interaction.response.send_message(f'為User：{user}添加了{count}點')
                    









        if counter == 0:
            await interaction.channel.send(f'沒有權限')
            
            
            
            
            
 



async def setup(bot):
    await bot.add_cog(Point(bot))