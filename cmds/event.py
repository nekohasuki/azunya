import discord
from discord.ext import commands

import json
with open("setting.json","r",encoding="utf8") as setting_file:
    setting = json.load(setting_file)
import random

from core.classes import Cog_extension,Logger
from core.error import Errors
from cmds.main import Main

class Event(Cog_extension):
    #成員加入通知
    @commands.Cog.listener()
    async def on_member_join(self,member):
        print(f'User {member} 加入了伺服器!')
        channel = self.bot.get_channel(int(setting["Welcome_channel_ID"]))
        await channel.send(f'User** {member} **加入了伺服器!')
    #成員退出通知
    @commands.Cog.listener()
    async def on_member_remove(self,member):
        print(f'User {member} 離開了伺服器!')
        channel = self.bot.get_channel(int(setting["Welcome_channel_ID"]))
        await channel.send(f'User** {member} **離開了伺服器!')  
    #"指令"錯誤報錯
    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):
        error_command = '{0}_error'.format(ctx.command)
        if hasattr(Errors,error_command):      # 檢查是否有 Custom Error Handler
            error_cmd = getattr(Errors,error_command)
            await error_cmd(self,ctx,error)
            return
        else:       # 使用 Default Error Handler
            await Errors.default_error(self,ctx,error)
    #添加身分組
    @commands.Cog.listener()
    async def on_raw_reaction_add(self,reaction):
        guild = self.bot.get_guild(reaction.guild_id)
        user = guild.get_member(reaction.user_id)
        role = guild.get_role(int(setting["ROLE_ID"]))
        #第一組
        if reaction.message_id == int(setting["ROLE_MESSAGE_ID"]):
            if str(reaction.emoji) == setting["EMOJI_FREE"]:
                print(f"{guild} add {user}/{role}")
                await user.add_roles(role)
        #第二組
        if reaction.message_id == "1219818319889043476":
            if str(reaction.emoji) == "✨":
                print(f"{user} add role")
                await user.add_roles(role)
        #第三組
        if reaction.message_id == "1219818319889043476":
            if str(reaction.emoji) == "<:LOGO1:12213786144641332>":
                print(f"{user} add role")
                await user.add_roles(role)
    #移除身分組
    @commands.Cog.listener()
    async def on_raw_reaction_remove(self,reaction):
        guild = self.bot.get_guild(reaction.guild_id)
        user = guild.get_member(reaction.user_id)
        role = guild.get_role(int(setting["ROLE_ID"]))
        #第一組
        if reaction.message_id == int(setting["ROLE_MESSAGE_ID"]):
            if str(reaction.emoji) == setting["EMOJI_FREE"]:
                print(f"{guild} remove {user}/{role}")
                await user.remove_roles(role,reason=f"User{user}不想要{role}的身分了QQ")
        #第二組
        if reaction.message_id == "1219818319889043476":
            if str(reaction.emoji) == "✨":
                print(f"{user} remove role")
                await user.remove_roles(role)
        #第三組
        if reaction.message_id == "1219818319889043476":
            if str(reaction.emoji) == "<:LOGO1:12213786144641332>":
                print(f"{user} remove role")
                await user.remove_roles(role) 
    #"指令"錯誤報錯
    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):
        error_command = '{0}_error'.format(ctx.command)
        if hasattr(Errors,error_command):      # 檢查是否有 Custom Error Handler
            error_cmd = getattr(Errors,error_command)
            await error_cmd(self,ctx,error)
            return
        else:       # 使用 Default Error Handler
            await Errors.default_error(self,ctx,error)










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