import discord
from discord.ext import tasks, commands
import json
with open('setting.json','r',encoding='utf8') as setting_file:
    setting = json.load(setting_file)

from core.classes import Cog_extension
import asyncio,datetime,schedule

class Task(Cog_extension):
    utc = datetime.timezone(datetime.timedelta(hours = 8))
    everyday_time = datetime.time(hour = 3, minute = 57, tzinfo = utc)
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.omikujidatareload.start()
        self.onlinecount.start()
        self.test.start()
    def cog_unload(self):
        self.onlinecount.cancel()
        self.omikujidatareload.cancel()
        self.test.cancel()
#初始化'setting.json'
    @tasks.loop(seconds=1)
    async def omikujidatareload(self):
        with open('setting.json','r',encoding='utf8') as setting_file:
            setting = json.load(setting_file)
        Current_hours = datetime.datetime.now().strftime('%H')
        Current_minutes = datetime.datetime.now().strftime('%M')
        Current_seconds = datetime.datetime.now().strftime('%S')
        if (f'{int(Current_hours)}:{int(Current_minutes)}') == setting['OmikujiTime'] and int(Current_seconds) == 1:
            with open('cmds\data\omikuji.json','r',encoding='utf8') as omikuji_file:
                omikuji = json.load(omikuji_file)
            with open('cmds\\data\\user_data.json' , 'r' , encoding='utf8') as UserDataFile:
                userdata = json.load(UserDataFile)
    #於後台印出用戶及抽取內容
            for user in omikuji:
                print(omikuji[user]['name'],':\n    ',omikuji[user]['pic'][14:-4])
    #檔名處理為純數字
            for user in omikuji:
                user_pic = omikuji[user]['pic'][14:-4]
                if '¤' in user_pic:
                    if 'omikuji' in userdata[user]:
                        userdata[user]['omikuji'].update({'badluck':userdata[user]['omikuji']['badluck'],'today':0})
                    elif 'omikuji' not in userdata[user]:
                        userdata[user].update({'omikuji':{'badluck':0,'today':0,}})
                if '★' in user_pic:
                    counter = 0
                    while '★' in user_pic:
                        counter += 1
                        user_pic=user_pic[1:]
                    if 'x' in user_pic:
                        today = int(user_pic[1:])-1+counter
                    else:
                        today = counter
                    if 'omikuji' in userdata[user]:
                            userdata[user]['omikuji'].update({'badluck':userdata[user]['omikuji']['badluck'],'today':today})
                    elif 'omikuji' not in userdata[user]:
                        userdata[user].update({'omikuji':{'badluck':0,'today':today}})
                if '☆' in user_pic:
                    counter = 0
                    while '☆' in user_pic:
                        counter += 1
                        user_pic=user_pic[1:]
                    if 'x' in user_pic:
                        today = (int(user_pic[1:])-1+counter)*-1
                    else:
                        today = counter*-1
                    if 'omikuji' in userdata[user]:
                            userdata[user]['omikuji'].update({'badluck':userdata[user]['omikuji']['badluck'],'today':today})
                    elif 'omikuji' not in userdata[user]:
                        userdata[user].update({'omikuji':{'badluck':0,'today':today}})
            user ={}
    #比較數字大小
            for user_a in userdata:
                for user_b in userdata:
                    if 'omikuji' in userdata[user_a] and 'omikuji' in userdata[user_b] and user_a != user_b:
                        user.update({user_a:userdata[user_a],user_b:userdata[user_b]})
                        if user[user_a]['omikuji']['today'] != None and user[user_b]['omikuji']['today'] != None and user[user_a]['omikuji']['today'] != user[user_b]['omikuji']['today']:
                            if user[user_a]['omikuji']['today'] > user[user_b]['omikuji']['today']:
                                user[user_a]['omikuji'].update({'today':None})
                            else:
                                user[user_b]['omikuji'].update({'today':None})
            bad_luck_user = []
            for user_a in user:
                if user[user_a]['omikuji']['today'] != None:
                    bad_luck_user.append(f'**`{userdata[user_a]['display_name']}`**')
                    userdata[user_a].update({'omikuji':{'badluck':user[user_a]['omikuji']['badluck']+1,'today':None}})
                with open('cmds\\data\\user_data.json' , 'w' , encoding='utf8') as UserDataFile:
                    json.dump(userdata , UserDataFile , indent=4)
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
    #重置'omikuji.json'資料
            print(f'{setting['OmikujiTime']}')
            print(f'{int(Current_hours)}:{int(Current_minutes)}:{int(Current_seconds)}')
            omikuji={}
            omikuji.update(omikuji)
            with open('cmds\data\omikuji.json','w',encoding='utf8') as omikuji_file:
                json.dump(omikuji,omikuji_file)
    @omikujidatareload.before_loop
    async def omikujidatareload_before(self):
        await self.bot.wait_until_ready()
#計數器
    @tasks.loop(seconds=1)
    async def onlinecount(self):
        with open('setting.json','r',encoding='utf8') as setting_file:
            setting = json.load(setting_file)
        counter = int(setting['onlinetime'])
        counter += 1
        onlinetime = {'onlinetime':f'{counter}'}
        setting.update(onlinetime)
        with open('setting.json','w',encoding='utf8') as setting_file:
            json.dump(setting,setting_file,indent=4)

    @onlinecount.before_loop
    async def onlinecount_before(self):
        with open('setting.json','r',encoding='utf8') as setting_file:
            setting = json.load(setting_file)
            onlinetime = {'onlinetime':'0'}
            setting.update(onlinetime)
        with open('setting.json','w',encoding='utf8') as setting_file:
            json.dump(setting,setting_file,indent=0)
        await self.bot.wait_until_ready()
#測試用
    @tasks.loop(seconds=1)
    async def test(self):
        pass
    @test.before_loop
    async def test_before(self):
        pass









async def setup(bot):
    await bot.add_cog(Task(bot))