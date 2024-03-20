import discord
from discord.ext import commands
from core.classes import Cog_extension

import json
with open("setting.json","r",encoding="utf8") as setting_file:
    setting = json.load(setting_file)
import random


class Event(Cog_extension):
        
    @commands.Cog.listener()      #成員加入通知
    async def on_member_join(self, member):
        print(f'User {member} 加入了伺服器!')
        channel = self.bot.get_channel(int(setting["Welcome_channel"]))
        await channel.send(f'User** {member} **加入了伺服器!')

    @commands.Cog.listener()      #成員退出通知
    async def on_member_remove(self, member):
        print(f'User {member} 離開了伺服器!')
        channel = self.bot.get_channel(int(setting["Welcome_channel"]))
        await channel.send(f'User** {member} **離開了伺服器!')


    @commands.Cog.listener()        #對話
    async def on_message(self, msg):
        #==:等於/!=:不等於
        #in:等於/not in:不等於
        #endswith:結束詞/startswith:開始詞
        #列表:<key= ["apple","banana"]>
        #and:以及/or:

        #……以及訊息不為自身(機器人)發出
        #<and msg.author != self.bot.user:>

        #……以及訊息中如果有包含關鍵字(key)
        #<and any(word in msg.content for word in key)>

        #……以及訊息等於關鍵字(key)
        #<and msg.content == key>

        if msg.content == key and msg.author != self.bot.user:
            await msg.channel.send("1")     #完全等於

        if msg.content.endswith("apple") and msg.author != self.bot.user:
            await msg.channel.send("2")     #結束詞

        key= ["apple","banana"]
        if any(word in msg.content for word in key):
            await msg.channel.send("3")  










async def setup(bot):
    await bot.add_cog(Event(bot))