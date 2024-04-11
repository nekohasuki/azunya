import discord
from discord.ext import tasks, commands
import json
with open('setting.json','r',encoding='utf8') as setting_file:
    setting = json.load(setting_file)

from core.classes import Cog_extension
import datetime,schedule

class Task(Cog_extension):
    tz = datetime.timezone(datetime.timedelta(hours = 8))
    everyday_time = datetime.time(hour = 3, minute = 57, tzinfo = tz)
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.omikujidataclear.start()
        self.onlinecount.start()
    def cog_unload(self):
        self.onlinecount.cancel()
        self.omikujidataclear.cancel()
#初始化'setting.json'
    @tasks.loop(seconds=1)
    async def omikujidataclear(self):
        with open('setting.json','r',encoding='utf8') as setting_file:
            setting = json.load(setting_file)
        Current_hours = datetime.datetime.now().strftime('%H')
        Current_minutes = datetime.datetime.now().strftime('%M')
        Current_seconds = datetime.datetime.now().strftime('%S')
        channel_id = 1219180207534243894
        channel = self.bot.get_channel(channel_id)
        if (f'{int(Current_hours)}:{int(Current_minutes)}') == setting['OmikujiTime']:
            print(f'{setting['OmikujiTime']}')
            print(f'{int(Current_hours)}:{int(Current_minutes)}:{int(Current_seconds)}')
            with open('cmds\data\omikuji.json','r',encoding='utf8') as omikuji_file:
                omikuji = json.load(omikuji_file)
                omikuji={'userdata': [],'namedata': []}
                omikuji.update(omikuji)
            with open('cmds\data\omikuji.json','w',encoding='utf8') as omikuji_file:
                json.dump(omikuji,omikuji_file)
#計數器
    @tasks.loop(seconds=1)
    async def onlinecount(self):
        with open('setting.json','r',encoding='utf8') as setting_file:
            setting = json.load(setting_file)
        count = int(setting['onlinetime'])
        count += 1
        onlinetime = {'onlinetime':f'{count}'}
        setting.update(onlinetime)
        with open('setting.json','w',encoding='utf8') as setting_file:
            json.dump(setting,setting_file,indent=0)
        
    @onlinecount.before_loop
    async def onlinecount_before(self):
        with open('setting.json','r',encoding='utf8') as setting_file:
            setting = json.load(setting_file)
            onlinetime = {'onlinetime':'0'}
            setting.update(onlinetime)
        with open('setting.json','w',encoding='utf8') as setting_file:
            json.dump(setting,setting_file,indent=0)
        await self.bot.wait_until_ready()









    
async def setup(bot):
    await bot.add_cog(Task(bot))