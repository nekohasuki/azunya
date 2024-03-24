import discord
from discord.ext import commands
from core.classes import Cog_extension,Logger
from core.error import Errors
from cmds.main import Main

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
    #"指令"錯誤報錯   
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        error_command = '{0}_error'.format(ctx.command)
        if hasattr(Errors, error_command):  # 檢查是否有 Custom Error Handler
            error_cmd = getattr(Errors, error_command)
            await error_cmd(self, ctx, error)
            return
        else:  # 使用 Default Error Handler
            await Errors.default_error(self, ctx, error)












    # #"指令"錯誤報錯(個別指令)
    # @Main.say.error
    # async def say_error(self,ctx,error):
    #     if isinstance(error,commands.errors.MissingRequiredArgument):
    #         await ctx.send(f"請輸入想要發送的訊息內文\n參考：\n```\n/say hellow```")
    # #"指令"錯誤報錯    
    # @commands.Cog.listener()
    # async def on_command_error(self,ctx,error):
    #     if hasattr(ctx.command,"on_error"):
    #         return
    #     if isinstance(error,commands.errors.MissingRequiredArgument):
    #         await ctx.send(f"參數缺失,以下為錯誤報告：\n```ex\ndiscord.ext.commands.errors.MissingRequiredArgument:\n    {error}```")
    #         Logger.log(self, ctx, error)
    #     elif isinstance(error,commands.errors.CommandNotFound):
    #         await ctx.send(f"未知指令,以下為錯誤報告：\n```ex\ndiscord.ext.commands.errors.CommandNotFound:\n    {error}```")
    #         Logger.log(self, ctx, error)
    #     elif isinstance(error,commands.errors.CommandError):
    #         await ctx.send(f"以下為錯誤報告：\n```ex\ndiscord.ext.cmmands.errors.TooManyArguments:\n    {error}```")
    #         Logger.log(self, ctx, error)
    #     else:
    #         await ctx.send(f"未知錯誤,以下為錯誤報告：\n```ex\ndiscord.ext.commands.errors.TooManyArguments:\n    {error}```")
    #         Logger.log(self, ctx, error)












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