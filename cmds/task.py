import discord
from discord.ext import tasks, commands
import json
open_file='''
with open('setting.json','r',encoding='utf-8') as setting_file:
    setting = json.load(setting_file)
with open('cmds/data/user_data.json' , 'r' , encoding='utf-8') as userdata_file:
    userdata = json.load(userdata_file)
with open('cmds/data/omikuji.json','r',encoding='utf-8') as omikuji_file:
    omikuji = json.load(omikuji_file)
with open(f'cmds/rpg_define/rpg_definitions.json','r',encoding='utf-8') as RPG_definitions_fill:
    rpg_definitions = json.load(RPG_definitions_fill)
'''
dump_setting="""
with open('setting.json','w',encoding='utf-8') as setting_file:
    json.dump(setting,setting_file,indent=4)
"""
dump_userdata="""
with open('cmds/data/user_data.json' , 'w' , encoding='utf-8') as userdata_file:
    json.dump(userdata , userdata_file , indent=4)
"""
dump_omikuji="""
with open('cmds/data/omikuji.json','w',encoding='utf-8') as omikuji_file:
    json.dump(omikuji,omikuji_file)
"""
dump_rpg_definitions='''
with open(f'cmds/rpg_define/rpg_definitions.json','w',encoding='utf-8') as RPG_definitions_fill: 
    json.dump(rpg_definitions,RPG_definitions_fill,indent=4)
'''
with open('setting.json','r',encoding='utf-8') as setting_file:
    setting = json.load(setting_file)

from core.classes import Cog_extension
import asyncio,datetime,schedule,shutil

class Task(Cog_extension):
    utc = datetime.timezone(datetime.timedelta(hours = 8))
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.omikujidatareload.start()
        self.onlinecount.start()
        self.Exchange_rate.start()
        self.test.start()
    def cog_unload(self):
        self.onlinecount.cancel()
        self.omikujidatareload.cancel()
        self.Exchange_rate.cancel()
        self.test.cancel()
#初始化'setting.json'
    @tasks.loop(seconds=1)
    async def omikujidatareload(self):
        with open('setting.json','r',encoding='utf-8') as setting_file:
            setting = json.load(setting_file)
        today =  datetime.datetime.now().strftime('%d')
        Current_hours = datetime.datetime.now().strftime('%H')
        Current_minutes = datetime.datetime.now().strftime('%M')
        Current_seconds = datetime.datetime.now().strftime('%S')
        if (f'{int(Current_hours)}:{int(Current_minutes)}') == setting['omikuji_reload_time'] and int(Current_seconds) == 1:
            with open('cmds\data\omikuji.json','r',encoding='utf-8') as omikuji_file:
                omikuji = json.load(omikuji_file)
            with open('cmds\\data\\user_data.json' , 'r' , encoding='utf-8') as userdata_file:
                userdata = json.load(userdata_file)
    #於後台印出用戶及抽取內容
            for user in omikuji:
                print(f'"{omikuji[user]['name']}":\n    {omikuji[user]['pic'][14:-4]}')
    #找出運氣最差的人
            min_number = []
            for user in userdata:
                if "omikuji" in userdata[user] and userdata[user]['omikuji']['today'] != None:
                    min_number.append(userdata[user]['omikuji']['today'])
            bad_luck_user = []
            if min_number == []:
                min_number.append(0)
            for user in userdata:
                if "omikuji" in userdata[user]:
                    if userdata[user]['omikuji']['today'] == (min(min_number)):
                        bad_luck_user.append(f'**`{userdata[user]['display_name']}`**')
                        userdata[user].update({'omikuji':{'badluck':userdata[user]['omikuji']['badluck']+1,'today':None}})
                    else:
                        userdata[user].update({'omikuji':{'badluck':userdata[user]['omikuji']['badluck'],'today':None}})
            with open('cmds\\data\\user_data.json' , 'w' , encoding='utf-8') as userdata_file:
                json.dump(userdata , userdata_file , indent=4)
        #聊天室留言
            channel = self.bot.get_guild(int(setting['GUILD_ID'])).get_channel(int(setting['MESSAGE_CHANNEL_ID']))
            if bad_luck_user != []:
                await channel.send(f'今天運氣最差的是 :\n{((str(bad_luck_user).replace("'", '')[1:-1]).replace(',','、'))}')
            else:
                await channel.send(f'今天運氣最差的是!!')
                await asyncio.sleep(.5)
                await channel.send(f'???')
                await asyncio.sleep(2)
                await channel.send(f'難道今天沒有人抽籤嗎?QQ')
                await asyncio.sleep(1)
                await channel.send(f'梓守我不被需要了嗎Q^O')
            await channel.send(f'對了')
            await channel.send(f'去投稿')
        #每月固定日期
            add_ponit_count = int(setting['add_ponit_count'])
            max_number = []
            add_ponit_user = []
            add_ponit_user_mention = []
            if today == setting['omikuji_reload_day']:
        #比較壞運氣值最大的人給予P點並重置所有人壞運氣值
                for user in userdata:
                    if 'omikuji' in userdata[user] and userdata[user]['omikuji']['badluck'] != None:
                        max_number.append(userdata[user]['omikuji']['badluck'])
                if max_number == []:
                    max_number.append(0)
                if max(max_number) != 0:
                    for user in userdata:
                        if 'omikuji' in userdata[user]:
                            if userdata[user]['omikuji']['badluck'] == max(max_number):
                                add_ponit_user.append(f'**`{userdata[user]['display_name']}`**')
                                add_ponit_user_mention.append(f'<@{str(user).replace('`','')}>')
                                userdata[user]['point'].update({'now_count':userdata[user]['point']['now_count']+add_ponit_count,'history_count':userdata[user]['point']['history_count']+add_ponit_count})
                            userdata[user]['omikuji'].update({'badluck':0})
                    with open('cmds\\data\\user_data.json' , 'w' , encoding='utf-8') as userdata_file:
                        json.dump(userdata , userdata_file , indent=4)
            #聊天室留言
                channel = self.bot.get_guild(int(setting['GUILD_ID'])).get_channel(int(setting['MESSAGE_CHANNEL_ID']))
                await channel.send(f'**__本月運氣最差的人__**結果出來了!!!')
                if add_ponit_user != []:
                    await asyncio.sleep(6)
                    await channel.send(f'運氣最差的是 :\n{((str(add_ponit_user).replace("'", '')[1:-1]).replace(',','、'))}')
                    await asyncio.sleep(8)
                    await channel.send(f'雖然命運很坎坷，但請不要放棄生活的希望\n說不定前方等著你的是~~ ||更加黑暗|| ~~一片大好前程呢~')
                    await asyncio.sleep(12)
                    await channel.send(f'不過運氣不好確實不怎麼開心La，嗯...<:KANGAERU:1147177506294730752>\n這樣!這裡的{add_ponit_count}點P點就收下吧!\n怎麼樣有稍微開心點了嗎?\n未來也要好好打起精神窩=W=')
                    channel = self.bot.get_guild(int(setting['GUILD_ID'])).get_channel(int(setting['POINT_LOG_CHANNEL_ID']))
                    await channel.send(f'已為User：{str(add_ponit_user_mention).replace("'",'').replace('[','').replace(']','').replace(',','、')}添加了**35**點\n原因：本月運氣太差，給予慰問金')
                else:
                    await asyncio.sleep(3)
                    await channel.send(f'本月運氣最差的人居然沒有嗎...')
                    await asyncio.sleep(5)
                    await channel.send(f'既然是這個結果就說明至少整整一個月都沒有人玩抽籤系統...')
                    await asyncio.sleep(2)
                    await channel.send(f'梓守我不信，難道沒有人想抽籤嗎?')
                    await asyncio.sleep(1)
                    await channel.send(f'看來這個伺服器不需要我了...')      
                shutil.copy('cmds/data/user_data.json',f'cmds/data/user_data_history/{datetime.datetime.now().strftime('%Y-%m-%d')}.json')          
                await channel.send(f'<@&1079939318371582043>\n記得拔管')      
    #重置'omikuji.json'資料
            omikuji={}
            omikuji.update(omikuji)
            with open('cmds\data\omikuji.json','w',encoding='utf-8') as omikuji_file:
                json.dump(omikuji,omikuji_file)
    @omikujidatareload.before_loop
    async def omikujidatareload_before(self):
        await self.bot.wait_until_ready()
#計數器
    @tasks.loop(seconds=1)
    async def onlinecount(self):
        with open('setting.json','r',encoding='utf-8') as setting_file:
            setting = json.load(setting_file)
        counter = int(setting['onlinetime'])
        counter += 1
        onlinetime = {'onlinetime':f'{counter}'}
        setting.update(onlinetime)
        with open('setting.json','w',encoding='utf-8') as setting_file:
            json.dump(setting,setting_file,indent=4)

    @onlinecount.before_loop
    async def onlinecount_before(self):
        with open('setting.json','r',encoding='utf-8') as setting_file:
            setting = json.load(setting_file)
            onlinetime = {'onlinetime':'0'}
            setting.update(onlinetime)
        with open('setting.json','w',encoding='utf-8') as setting_file:
            json.dump(setting,setting_file,indent=0)
        await self.bot.wait_until_ready()
#RPG匯率更新
    @tasks.loop(minutes=1)
    async def Exchange_rate(self):
        variable = {}
        exec(open_file,globals(),variable)
        userdata = variable.get('userdata')
        rpg_definitions = variable.get('rpg_definitions')
        point_list = []
        for line in userdata:
            if line == str(697842681082281985):
                pass
            elif 'RPG' in userdata[line] and 'setting_mod' in userdata[line]['RPG'] and not userdata[line]['RPG']['setting_mod']:
                if 'point' in userdata[line] and userdata[line]['point']['now_count'] != 0:
                    point_list.append(userdata[line]['point']['now_count'])
        if point_list == []:
            point_list.append(1)
        point_total = sum(point_list)
        point_max = max(point_list)
        point_len = len(point_list)
        if point_max <= 0:
            point_len = 0
        rpg_definitions['Exchange_rate'] = (point_total/point_max-point_total) / ((point_len**2*point_total)/point_max/(point_len+1)) *-1+1
        with open(f'cmds/rpg_define/rpg_definitions.json','w',encoding='utf-8') as RPG_definitions_fill: 
            json.dump(rpg_definitions,RPG_definitions_fill,indent=4)
    @Exchange_rate.before_loop
    async def Exchange_rate_before(self):
        now = datetime.datetime.now().strftime('%S')
        while int(now) != 0:
            await asyncio.sleep(1)
            now = datetime.datetime.now().strftime('%S')
#測試用
    @tasks.loop(seconds=1)
    async def test(self):
        pass
    @test.before_loop
    async def test_before(self):
        pass









async def setup(bot):
    await bot.add_cog(Task(bot))