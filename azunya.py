import discord
from discord.ext import commands
intents = discord.Intents.all()
intents.typing = False
intents.presences = False
import json
with open('setting.json','r',encoding='utf8') as setting_file:
    setting = json.load(setting_file)
bot = commands.Bot(command_prefix =[f'{setting["prefix"]}-','/'],intents = intents)

import asyncio,keep_alive,os
from typing import Optional

prefix = 'a-'
#機器人登陸通知
@bot.event
async def on_ready():
    print('>>','嗨嗨嗨!! {0.user}已經成功登陸嘍!!!'.format(bot),'<<')
    try:
        synced = await bot.tree.sync()
        print(f'已為您同步{len(synced)}條命令')
    except Exception as e:
        print('命令同步時發生錯誤: ', e)
#加載類別
commandname = (f'{prefix}load')
@bot.tree.command(name = commandname, description = '加載擴充類別')
async def load(interaction: discord.Interaction,extension: Optional[str] = None):
    user = interaction.user.id
    extension_list = []
    for allfile in os.listdir('./cmds'):
        if 'task.py' in allfile:
            pass
        else:
            if allfile.endswith('.py'):extension_list.append(allfile[:-3])
    if extension == None:
        await interaction.response.send_message(f'請輸入需要加載類別\n參考：```/load data```\n如果User：<@{user}>不知道目前類別有哪些\n請參考：\n{extension_list}')
    elif extension == 'a' or extension == 'A' or extension == 'ALL' or extension == 'All' or extension == 'all':
        extension = "all"
        for load in extension_list:
            await bot.load_extension(f'cmds.{load}')
        await interaction.response.send_message(f'已成功加載__{len(extension_list)}__項擴充類別')
    else:
        if extension in extension_list:
            await bot.load_extension(f'cmds.{extension}')
            await interaction.response.send_message(f'已成功加載擴充類別：__{extension}__')
        else:
            await interaction.response.send_message(f'沒有擴充類別："{extension}"')
#重新加載類別
commandname = (f'{prefix}reload')
@bot.tree.command(name = commandname, description = '重新加載擴充類別')
async def reload(interaction: discord.Interaction,extension: Optional[str] = None):
    user = interaction.user.id
    extension_list = []
    for allfile in os.listdir('./cmds'):
        if 'task.py' in allfile:
            pass
        else:
            if allfile.endswith('.py'):extension_list.append(allfile[:-3])
    if extension == None:
        await interaction.response.send_message(f'請輸入需要重新加載類別\n參考：```/reload data```\n如果User：<@{user}>不知道目前類別有哪些\n請參考：\n{extension_list}')
    elif extension == 'a' or extension == 'A' or extension == 'ALL' or extension == 'All' or extension == 'all':
        extension = "all"
        for reload in extension_list:
            await bot.reload_extension(f'cmds.{reload}')
        await interaction.response.send_message(f'已成功重新加載__{len(extension_list)}__項擴充類別')
    else:
        if extension in extension_list:
            await bot.reload_extension(f'cmds.{extension}')
            await interaction.response.send_message(f'已成功重新加載擴充類別：__{extension}__')
        else:
            await interaction.response.send_message(f'沒有擴充類別："{extension}"')
#取消加載類別
commandname = (f'{prefix}unload')
@bot.tree.command(name = commandname, description = '取消加載擴充類別')
async def unload(interaction: discord.Interaction,extension: Optional[str] = None):
    user = interaction.user.id
    extension_list = []
    for allfile in os.listdir('./cmds'):
        if 'task.py' in allfile:
            pass
        else:
            if allfile.endswith('.py'):extension_list.append(allfile[:-3])
    if extension == None:
        await interaction.response.send_message(f'請輸入需要取消加載類別\n參考：```/unload data```\n如果User：<@{user}>不知道目前類別有哪些\n請參考：\n{extension_list}')
    elif extension == 'a' or extension == 'A' or extension == 'ALL' or extension == 'All' or extension == 'all':
        extension = "all"
        for unload in extension_list:
            await bot.unload_extension(f'cmds.{unload}')
        await interaction.response.send_message(f'已成功取消加載__{len(extension_list)}__項擴充類別')
    else:
        if extension in extension_list:
            await bot.unload_extension(f'cmds.{extension}')
            await interaction.response.send_message(f'已成功取消加載擴充類別：__{extension}__')
        else:
            await interaction.response.send_message(f'沒有擴充類別："{extension}"')



async def main():
    for Filename in os.listdir('./cmds'):
        if Filename.endswith('py'):
            await bot.load_extension(f'cmds.{Filename[:-3]}')
    await bot.start(setting['TOKEN'])
if __name__ == '__main__':
    if setting['keep_alive'] == 'True':
        keep_alive.keep_alive()
        asyncio.run(main())
    elif setting['keep_alive'] == 'False':
        asyncio.run(main())
    else:
        print('ERROR')