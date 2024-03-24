import discord
from discord.ext import commands
from core.classes import Cog_extension

import json
with open("setting.json","r",encoding="utf8") as setting_file:
    setting = json.load(setting_file)
import random

class Event(Cog_extension):
    #成員加入通知
    @commands.Cog.listener()
    async def on_member_join(self,member):
        print(f'User {member} 加入了伺服器!')
        channel = self.bot.get_channel(int(setting["WELCOME_CHANNEL_ID"]))
        await channel.send(f'User** {member} **加入了伺服器!')
    #成員退出通知
    @commands.Cog.listener()
    async def on_member_remove(self,member):
        print(f'User {member} 離開了伺服器!')
        channel = self.bot.get_channel(int(setting["WELCOME_CHANNEL_ID"]))
        await channel.send(f'User** {member} **離開了伺服器!')
    #添加身分組
    @commands.Cog.listener()
    async def on_raw_reaction_add(self,reaction):
        if str(reaction.emoji)  == "🆓":
            print("hi??????????")
            guild = self.bot.get_guild(reaction.guild_id)
            role = guild.get_role(1219645862502731876)
            await reaction.member.add_roles(role)
    #移除身分組
    @commands.Cog.listener()
    async def on_raw_reaction_remove(self,reaction):
        if str(reaction.emoji)  == "🆓":
            print("hi!!!!!!!!!!!")
            guild = self.bot.get_guild(reaction.guild_id)
            role = guild.get_role(1219645862502731876)
            await reaction.member.remove_roles(role)
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    #對話
    @commands.Cog.listener()
    async def on_message(self,msg):
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

        key= ["apple","banana"]
        if any(word in msg.content for word in (key)):
            random_count = random.choice(setting["count"])
            if (random_count) == "0" or (random_count) == "2" or (random_count) == "4" or (random_count) == "6" or (random_count) == "8":
                await msg.channel.send("text")
            if (random_count) == "1" or (random_count) == "3" or (random_count) == "5" or (random_count) == "7" or (random_count) == "9":
                await msg.channel.send("!!!")

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////








async def setup(bot):
    await bot.add_cog(Event(bot))