import discord
from discord.ext import commands
import json
with open('setting.json','r',encoding='utf8') as setting_file:
    setting = json.load(setting_file)

from core.classes import Logger
from cmds.tool import Tool

class Errors():
    
    #個別'指令'錯誤報錯    
    @Tool.say.error
    async def say_error(self,ctx,error):
        if isinstance(error,commands.errors.MissingRequiredArgument):
            await ctx.send(f'請輸入想要發送的訊息內文\n參考：\n```\n/say hellow```或是```{setting['prefix']}-say hellow```')
    #預設'指令'錯誤報錯    
    async def default_error(self,ctx,error):
        if isinstance(error,commands.errors.MissingRequiredArgument):
            err = str(error).split(' ')[0]
            await ctx.send(f'**__`<{err}>`__**參數缺失,以下為錯誤報告：\n```ex\ndiscord.ext.commands.errors.MissingRequiredArgument:\n    {error}```')
            Logger.log(self, ctx, error)
        elif isinstance(error,commands.errors.CommandNotFound):
            await ctx.send(f'未知指令,以下為錯誤報告：\n```ex\ndiscord.ext.commands.errors.CommandNotFound:\n    {error}```')
            Logger.log(self, ctx, error)
        elif isinstance(error,commands.errors.CommandError):
            await ctx.send(f'以下為錯誤報告：\n```ex\ndiscord.ext.cmmands.errors.TooManyArguments:\n    {error}```')
            Logger.log(self, ctx, error)
        else:
            await ctx.send(f'未知錯誤,以下為錯誤報告：\n```ex\ndiscord.ext.commands.errors.TooManyArguments:\n    {error}```')
            Logger.log(self, ctx, error)