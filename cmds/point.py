import discord
from discord.ext import commands
from discord import app_commands
import json
with open('setting.json' , 'r' , encoding='utf-8') as setting_file:
    setting = json.load(setting_file)

from core.classes import Cog_extension
from typing import Optional
import asyncio,datetime

prefix = 'p-'
class Point(Cog_extension):
#查看指定用戶點數
    commandname = (f'{prefix}checkpoint')
    @app_commands.command(name = commandname , description = '查看指定用戶點數')
    @app_commands.describe(user='輸入用戶')
    async def checkpoint(self , interaction:discord.Interaction , user: Optional[str] = None):
        if user == None:
            await interaction.response.send_message(f'請輸入用戶')
        else:
            with open('setting.json' , 'r' , encoding='utf-8') as setting_file:
                setting = json.load(setting_file)
            role_list = setting['MOD_roles']
            id = interaction.user.id
            color = interaction.user.color
            if interaction.user.id == 697842681082281985:
                id = 938100109240074310
                color = interaction.guild.get_member(int(id)).color
            counter = 0
            for role in role_list:
                if counter == 1:
                    break
                role_members = interaction.guild.get_role(int(f'{role}')).members
                if str(id) in str(role_members):
                    counter += 1
                    if "<@" in user:
                        if "&" not in user:
                            with open('cmds\\data\\user_data.json' , 'r' , encoding='utf-8') as userdata_file:
                                userdata = json.load(userdata_file)
                            user = interaction.guild.get_member(int(user[2:-1]))
                            if f'{user.id}' not in userdata:
                                global_name = user.global_name
                                if global_name == None:
                                    global_name = f'"name":/{user.name}/'
                                if user.bot == False:
                                    code=[]
                                    for data in userdata:
                                        if userdata[data]['code'] != "#NO":
                                            code.append(userdata[data]['code'])
                                    userdata_update = {f'{user.id}':{'name':f'{user.name}','display_name':f'{user.display_name}','global_name':f'{user.global_name}','code':str(int(max(code))+1).zfill(3),'top_role':f'<@&{user.top_role.id}>','name_card':True,'point':{'state':True,'now_count':0,'history_count':0,'consumption':0,'give':0,'deprivation':0},'trade_count': 0,'VIP_tickets': 0,'VIP_chip': 0,"omikuji": {"badluck": 0,"today": None},"RPG":{},"recent_messages":{"url":"","time":""}}}
                                else:
                                    userdata_update = {f'{user.id}':{'name':f'{user.name}','display_name':f'{user.display_name}','global_name':f'{user.global_name}','code':f'#NO','top_role':f'<@&{user.top_role.id}>','name_card':True,'point':{'state':True,'now_count':0,'history_count':0,'consumption':0,'give':0,'deprivation':0},'trade_count': 0,'VIP_tickets': 0,'VIP_chip': 0,"omikuji": {"badluck": 0,"today": None},"RPG":{},"recent_messages":{"url":"","time":""}}}
                                userdata.update(userdata_update)
                                with open('cmds\\data\\user_data.json','w',encoding='utf-8') as userdata_file:
                                    json.dump(userdata , userdata_file , indent=4)
                            state = userdata[f'{user.id}']['point']['state']
                            now_count = userdata[f'{user.id}']['point']['now_count']
                            history_count = userdata[f'{user.id}']['point']['history_count']
                            consumption = userdata[f'{user.id}']['point']['consumption']
                            give = userdata[f'{user.id}']['point']['give']
                            deprivation = userdata[f'{user.id}']['point']['deprivation']
                            trade_count = userdata[f'{user.id}']['trade_count']
                            if state == True:
                                state = '已註冊'
                            if state == False:
                                state = '已收回'
                            if state == None:
                                state = '未註冊'
                            if now_count > 2147483647 :
                                now_count = '無上限'
                            if history_count > 2147483647 :
                                history_count = '無上限'
                            if consumption > 2147483647 :
                                consumption = '無上限'
                            if give > 2147483647 :
                                give = '無上限'
                            if deprivation > 2147483647 :
                                deprivation = '無上限'
                            if trade_count > 2147483647 :
                                trade_count = '無上限'
                            if interaction.user.top_role.position >= user.top_role.position:
                                embed = discord.Embed(title=f'**"{user.display_name}"的點數資料 :**',url=f'https://discord.com/channels/{interaction.guild.id}/{interaction.channel.id}',description=f'**當前總量：    {now_count}**\n**歷史總量：    {history_count}**\n**總消耗：    {consumption}**\n**曾給出：    {give}**\n**被剝奪：    {deprivation}**\n**交易量：    {trade_count}**\n**註冊狀態：    __{state}__**',color=color)
                                await interaction.response.send_message(embed=embed)
                            else:
                                await interaction.response.send_message(f'沒有權限')
                        else:
                            await interaction.response.send_message(f'這好像是某個身分組並不是某位User')
                    else:
                        await interaction.response.send_message(f'User：**{interaction.user.global_name}** 請問...\nuser參數裡你放了甚麼??')
#給予指定用戶點數
    commandname = (f'{prefix}givepoint')
    @app_commands.command(name = commandname , description = '給予指定用戶點數')
    @app_commands.describe(user='輸入用戶' , count='輸入數量')
    async def givepoint(self , interaction:discord.Interaction , user: Optional[str] = None , count: Optional[int] = None):
        if user == None:
            user = f'<@{interaction.user.id}>'
            if interaction.user.id == 697842681082281985:
                user = f'<@938100109240074310>'
        if count == None:
            count = 0
        if "<@" in user:
            if "&" not in user:
                count = abs(count)
                userA = interaction.user
                if interaction.user.id == 697842681082281985:
                    userA = interaction.guild.get_member(int(938100109240074310))                       
                userB = interaction.guild.get_member(int(user[2:-1]))                       
                with open('cmds\\data\\user_data.json' , 'r' , encoding='utf-8') as userdata_file:
                    userdata = json.load(userdata_file)
                if userdata[f'{userA.id}']['point']['state'] == True:
                    if userdata[f'{userB.id}']['point']['state'] == True or userdata[f'{userB.id}']['point']['state'] == False:
                    #抓取資料
                        userdata_update_A = userdata[f"{userA.id}"]
                        now_count_A = userdata_update_A['point']['now_count']
                        give_A = userdata_update_A['point']['give']
                        if int(now_count_A) > 2147483647:
                            now_count_A = int(now_count_A)+count
                        userdata_update_B = userdata[f"{userB.id}"]
                        now_count_B = userdata_update_B['point']['now_count'] 
                        history_count_B = userdata_update_B['point']['history_count']
                        if count <= now_count_A:
                        #刷入資料
                            userdata_update_A['point']['now_count'] = int(now_count_A) - count
                            userdata_update_A['point']['give'] = int(give_A) + count

                            userdata_update_B['point']['now_count'] = int(now_count_B) + count
                            userdata_update_B['point']['history_count'] = int(history_count_B) + count
                        #更新資料
                            userdata[f'{userA.id}'].update(userdata_update_A)
                            userdata[f'{userB.id}'].update(userdata_update_B)
                            with open('cmds\\data\\user_data.json' , 'w' , encoding='utf-8') as userdata_file:
                                json.dump(userdata , userdata_file , indent=4)
                            await interaction.response.send_message(f'User：{userA.mention}給予了User：{userB.mention}**{count}**點')
                        else:
                            await interaction.response.send_message(f'User：{userA.mention}\n你的點數似乎不夠喔')
                    elif userdata[f'{userB.id}']['point']['state'] == None:
                        await interaction.response.send_message(f'可是User：{userB.mention}\n從未註冊過P卡\n請先讓{userB.mention}回[__領取身分的地方__](https://ptb.discord.com/channels/{interaction.guild.id}/{setting['ROLE_MESSAGE_CHANNEL_ID']}/{setting['ROLE_MESSAGE_ID']})註冊')
                    else:
                        await interaction.response.send_message(f'對方用戶資料損毀，請聯絡管理員檢查用戶資料')
                elif userdata[f'{userA.id}']['point']['state'] == False:
                    await interaction.response.send_message(f'User：{userA.mention}\n你的P卡註冊狀態為收回\n請先回[__領取身分的地方__](https://ptb.discord.com/channels/{interaction.guild.id}/{setting['ROLE_MESSAGE_CHANNEL_ID']}/{setting['ROLE_MESSAGE_ID']})重新註冊')
                elif userdata[f'{userA.id}']['point']['state'] == None:
                    await interaction.response.send_message(f'可是User：{userA.mention}\n你從未註冊過P卡\n請先回[__領取身分的地方__](https://ptb.discord.com/channels/{interaction.guild.id}/{setting['ROLE_MESSAGE_CHANNEL_ID']}/{setting['ROLE_MESSAGE_ID']})註冊')
                else:
                    await interaction.response.send_message(f'用戶資料損毀，請聯絡管理員檢查用戶資料')
            else:
                await interaction.response.send_message(f'這好像是某個身分組並不是某位User')
        else:
            await interaction.response.send_message(f'User：{interaction.user.global_name} 請問...\nuser參數裡你放了甚麼??')
#查看自己點數
    commandname = (f'{prefix}mypoint')
    @app_commands.command(name = commandname , description = '查看自己點數')
    async def mypoint(self , interaction:discord.Interaction):
        user = interaction.user
        if interaction.user.id == 697842681082281985:
            user = interaction.guild.get_member(int(938100109240074310))
        color = user.color
        with open('cmds\\data\\user_data.json' , 'r' , encoding='utf-8') as userdata_file:
            userdata = json.load(userdata_file)
        if f'{user.id}' not in userdata:
            global_name = user.global_name
            if global_name == None:
                global_name = f'name:{user.name}'
            userdata_update = {f'{user.id}':{'name':f'{user.name}','display_name':f'{user.display_name}','global_name':f'{global_name}','code':f'#NO','top_role':f'<@&{user.top_role.id}>','name_card':None,'point':{'state':None,'now_count':0,'history_count':0,'consumption':0,'give':0,'deprivation':0},'trade_count': 0,'VIP_tickets': 0,'VIP_chip': 0}}
            userdata.update(userdata_update)
            with open('cmds\\data\\user_data.json','w',encoding='utf-8') as userdata_file:
                json.dump(userdata , userdata_file , indent=4)
        state = userdata[f'{user.id}']['point']['state']
        now_count = userdata[f'{user.id}']['point']['now_count']
        history_count = userdata[f'{user.id}']['point']['history_count']
        consumption = userdata[f'{user.id}']['point']['consumption']
        give = userdata[f'{user.id}']['point']['give']
        deprivation = userdata[f'{user.id}']['point']['deprivation']
        trade_count = userdata[f'{user.id}']['trade_count']
        if state == True:
            state = '已註冊'
        if state == False:
            state = '已收回'
        if state == None:
            state = '未註冊'
        if now_count > 2147483647 :
            now_count = '無上限'
        if history_count > 2147483647 :
            history_count = '無上限'
        if consumption > 2147483647 :
            consumption = '無上限'
        if give > 2147483647 :
            give = '無上限'
        if deprivation > 2147483647 :
            deprivation = '無上限'
        if trade_count > 2147483647 :
            trade_count = '無上限'
        embed = discord.Embed(title=f'**"{user.display_name}"的點數資料 :**',url=f'https://discord.com/channels/{interaction.guild.id}/{interaction.channel.id}',description=f'**當前總量：    {now_count}**\n**歷史總量：    {history_count}**\n**總消耗：    {consumption}**\n**曾給出：    {give}**\n**被剝奪：    {deprivation}**\n**交易量：    {trade_count}**\n**註冊狀態：    __{state}__**',color=color)
        await interaction.response.send_message(embed=embed)
#添加點數給指定用戶
    commandname = (f'{prefix}point')
    @app_commands.command(name = commandname , description = '添加點數給指定用戶')
    @app_commands.describe(mod = '模式(需要權限)' , users='輸入用戶' , count='輸入數量' , reason = '輸入原因')
    @app_commands.choices(mod=[app_commands.Choice(name = 'add' , value = 'add') , app_commands.Choice(name = 'remove' , value = 'remove')])
    async def point(self , interaction:discord.Interaction , mod: app_commands.Choice[str] , users: Optional[str] = None , count: Optional[int] = None , reason: Optional[str] = None):        
        if count == None:
            count = 0
        if reason == None:
            reason = '沒什麼特別的原因'
        if users == None:
            await interaction.response.send_message(f'請輸入使用者')
        else:
            with open('setting.json' , 'r' , encoding='utf-8') as setting_file:
                setting = json.load(setting_file)
            role_list = setting['MOD_roles']
            author = interaction.user
            if interaction.user.id == 938100109240074310:
                author =  interaction.guild.get_member(int(697842681082281985))
            id = author.id
            counter = 0
            for role in role_list:
                if counter == 1:
                    break
                role_members = interaction.guild.get_role(int(f'{role}')).members
                if str(id) in str(role_members):
                    counter += 1
                    user = (users.replace('>','> ')).split()
                    userlist = {'mod':mod.name,'role':[],'succeeded':[],'state_None':[],'state_corruption':[],'insufficient':[],'unknown':[],'author':None}
                    for user in user:
                        if "<@" in user:
                            if "&" not in user:
                                user = interaction.guild.get_member(int(user[2:-1]))
                                if author != user:
                                    if author.top_role.position >= user.top_role.position:
                                        with open('cmds\\data\\user_data.json' , 'r' , encoding='utf-8') as userdata_file:
                                            userdata = json.load(userdata_file)
                                        if userdata[f'{user.id}']['point']['state'] == True or userdata[f'{user.id}']['point']['state'] == False:
                                            count = abs(count)
                                        #抓取資料
                                            userdata_update = userdata[f"{user.id}"]
                                            now_count = userdata_update['point']['now_count']
                                            history_count = userdata_update['point']['history_count']
                                            consumption = userdata_update['point']['consumption']
                                        #添加點數
                                            if mod.name == "add":
                                                userlist['mod'] = '添加'
                                            #刷入資料
                                                userdata_update['point']['now_count'] = int(now_count) + count
                                                userdata_update['point']['history_count'] = int(history_count) + count
                                        #移除點數
                                            elif mod.name == "remove":
                                                userlist['mod'] = '移除'
                                            #刷入資料
                                                userdata_update['point']['now_count'] = int(now_count) - count
                                                userdata_update['point']['consumption'] = int(consumption) + count
                                        #更新資料
                                            userdata[f"{user.id}"].update(userdata_update)
                                            with open('cmds\\data\\user_data.json' , 'w' , encoding='utf-8') as userdata_file:
                                                json.dump(userdata , userdata_file , indent=4)
                                            userlist['succeeded'].append(user.mention)
                                        elif userdata[f'{user.id}']['point']['state'] == None:
                                            userlist['state_None'].append(user.mention)
                                        else:
                                            userlist['state_corruption'].append(user.mention)
                                    else:
                                        userlist['insufficient'].append(user.mention)
                                else:
                                    userlist['author']=True
                            else:
                                userlist['role'].append(user)
                        else:
                                userlist['unknown'].append(f'"{user}"')
                    succeeded = '、'.join(userlist['succeeded'])
                    role = '、'.join(userlist['role'])
                    state_None = '、'.join(userlist['state_None'])
                    state_corruption = '、'.join(userlist['state_corruption'])
                    insufficient = '、'.join(userlist['insufficient'])
                    unknown = '、'.join(userlist['unknown'])
                    message = []
                    if succeeded != '':
                        message.append(f'已為User：{succeeded}{userlist['mod']}了**{count}**點\n原因：{reason}\n')
                    if insufficient != '':
                        message.append(f'權限不足，無法為{insufficient}進行點數的加減')
                    if role != '':
                        message.append(f'\n{role}\n以上好像是身分組而不是User')
                    if state_corruption != '':
                        message.append(f'用戶{state_corruption}資料損毀，請聯絡管理員檢查用戶資料')
                    if unknown != '':
                        message.append(f'無法理解{unknown}代表的對象')
                    if userlist['author'] == True:
                        message.append(f'> `注意:指令無法對自己使用`')
                    await interaction.response.send_message('\n'.join(message))
                    await asyncio.sleep(1)
                    if state_None != '':
                        await interaction.channel.send(f'{state_None}\n以上User還從未註冊過P卡\n請以上提到的User\n自行回[__領取身分的地方__](https://ptb.discord.com/channels/{interaction.guild.id}/{setting['ROLE_MESSAGE_CHANNEL_ID']}/{setting['ROLE_MESSAGE_ID']})註冊')
            if counter == 0:
                await interaction.response.send_message(f'沒有任何一個可以加減點數的權限')
                










async def setup(bot):
    await bot.add_cog(Point(bot))