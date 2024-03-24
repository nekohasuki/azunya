import discord
from discord.ext import commands
import datetime

class Cog_extension(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

class Logger:
    def log(self, ctx, data, type='error'):
        '''事件紀錄器'''
        time = datetime.datetime.now().strftime('[%Y-%m-%d] [%H:%M]')
        user = ctx.author.name
        channel = ctx.channel.name
        command = ctx.command
        if type == 'error':
            print(f'<Error Log>: {time}/[{user}][{channel}][{command}]: {data}')