import discord
from discord.ext import tasks, commands
import json
with open("setting.json","r",encoding="utf8") as setting_file:
    setting = json.load(setting_file)

from core.classes import Cog_extension
import datetime,schedule

class Task(Cog_extension):
    tz = datetime.timezone(datetime.timedelta(hours = 8))
    everyday_time = datetime.time(hour = 3, minute = 57, tzinfo = tz)
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.omikujidataclear.start()
    def cog_unload(self):
        self.omikujidataclear.cancel()
 
    @tasks.loop(seconds=1)
    async def omikujidataclear(self):
        with open("setting.json","r",encoding="utf8") as setting_file:
            setting = json.load(setting_file)
        Current_Time = datetime.datetime.now().strftime("%H:%M")
        Current_seconds = datetime.datetime.now().strftime("%S")
        channel_id = 1219180207534243894
        channel = self.bot.get_channel(channel_id)
        if Current_Time == setting["OmikujiTime"]:
            print(f"{setting["OmikujiTime"]}")
            print(f"{Current_Time}:{Current_seconds}")
            with open("cmds\data\omikuji.json","r",encoding="utf8") as omikuji_file:
                omikuji = json.load(omikuji_file)
                omikuji={"userdata": [],"namedata": []}
                omikuji.update(omikuji)
            with open("cmds\data\omikuji.json","w",encoding="utf8") as omikuji_file:
                json.dump(omikuji,omikuji_file)









    
async def setup(bot):
    await bot.add_cog(Task(bot))