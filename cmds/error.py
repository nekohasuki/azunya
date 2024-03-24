import discord
from discord.ext import commands
from core.classes import Cog_extension

import json
with open("setting.json","r",encoding="utf8") as setting_file:
    setting = json.load(setting_file)
from cmds.main import Main

class Error(Cog_extension):
    #"指令"錯誤報錯(個別指令)
    @Main.say.error
    async def say_error(self,ctx,error):
        if isinstance(error,commands.errors.MissingRequiredArgument):
            await ctx.send(f"請輸入想要發送的訊息內文\n參考：\n```\n/say hellow```")
    #"指令"錯誤報錯    
    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):
        if hasattr(ctx.command,"on_error"):
            return
        if isinstance(error,commands.errors.MissingRequiredArgument):
            await ctx.send(f"參數缺失,以下為錯誤報告：\n```ex\ndiscord.ext.commands.errors.MissingRequiredArgument:\n    {error}```")
        elif isinstance(error,commands.errors.CommandNotFound):
            await ctx.send(f"未知指令，以下為錯誤報告：\n```ex\ndiscord.ext.commands.errors.CommandNotFound:\n    {error}```")
        elif isinstance(error,commands.errors.CommandError):
            await ctx.send(f"以下為錯誤報告：\n```ex\ndiscord.ext.commands.errors.CommandError:\n    {error}```")
        elif isinstance(error,commands.errors.ConversionError):
            await ctx.send(f"以下為錯誤報告：\n```ex\ndiscord.ext.commands.errors.ConversionError:\n    {error}```")
        elif isinstance(error,commands.errors.MissingRequiredAttachment):
            await ctx.send(f"以下為錯誤報告：\n```ex\ndiscord.ext.commands.errors.MissingRequiredAttachment:\n    {error}```")
        elif isinstance(error,commands.errors.ArgumentParsingError):
            await ctx.send(f"以下為錯誤報告：\n```ex\ndiscord.ext.commands.errors.ArgumentParsingError:\n    {error}```")
        elif isinstance(error,commands.errors.UnexpectedQuoteError):
            await ctx.send(f"以下為錯誤報告：\n```ex\ndiscord.ext.commands.errors.UnexpectedQuoteError:\n    {error}```")
        elif isinstance(error,commands.errors.ExpectedClosingQuoteError):
            await ctx.send(f"以下為錯誤報告：\n```ex\ndiscord.ext.commands.errors.ExpectedClosingQuoteError:\n    {error}```")   
        elif isinstance(error,commands.errors.BadArgument):
            await ctx.send(f"以下為錯誤報告：\n```ex\ndiscord.ext.commands.errors.BadArgument:\n    {error}```")   
        elif isinstance(error,commands.errors.BadUnionArgument):
            await ctx.send(f"以下為錯誤報告：\n```ex\ndiscord.ext.commands.errors.BadUnionArgument:\n    {error}```")   
        elif isinstance(error,commands.errors.BadLiteralArgument):
            await ctx.send(f"以下為錯誤報告：\n```ex\ndiscord.ext.commands.errors.BadLiteralArgument:\n    {error}```")   
        elif isinstance(error,commands.errors.PrivateMessageOnly):
            await ctx.send(f"以下為錯誤報告：\n```ex\ndiscord.ext.commands.errors.PrivateMessageOnly:\n    {error}```")   
        elif isinstance(error,commands.errors.NoPrivateMessage):
            await ctx.send(f"以下為錯誤報告：\n```ex\ndiscord.ext.commands.errors.NoPrivateMessage:\n    {error}```")   
        elif isinstance(error,commands.errors.CheckFailure):
            await ctx.send(f"以下為錯誤報告：\n```ex\ndiscord.ext.commands.errors.CheckFailure:\n    {error}```")   
        elif isinstance(error,commands.errors.CheckAnyFailure):
            await ctx.send(f"以下為錯誤報告：\n```ex\ndiscord.ext.commands.errors.CheckAnyFailure:\n    {error}```")   
        elif isinstance(error,commands.errors.DisabledCommand):
            await ctx.send(f"以下為錯誤報告：\n```ex\ndiscord.ext.commands.errors.DisabledCommand:\n    {error}```")   
        elif isinstance(error,commands.errors.CommandInvokeError):
            await ctx.send(f"以下為錯誤報告：\n```ex\ndiscord.ext.commands.errors.CommandInvokeError:\n    {error}```")   
        elif isinstance(error,commands.errors.UserInputError):
            await ctx.send(f"以下為錯誤報告：\n```ex\ndiscord.ext.commands.errors.UserInputError:\n    {error}```")   
        elif isinstance(error,commands.errors.TooManyArguments):
            await ctx.send(f"以下為錯誤報告：\n```ex\ndiscord.ext.commands.errors.TooManyArguments:\n    {error}```")











async def setup(bot):
    await bot.add_cog(Error(bot))