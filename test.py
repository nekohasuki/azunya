import json,os
from discord import SelectOption
B=True
A="""
with open('setting.json','r',encoding='utf-8') as setting_file:
    setting = json.load(setting_file)
"""
setting={}
exec(A,globals(),setting)
setting=setting.get('setting')
print(setting)

# # # /////////////////////////////////////////////////////////////////////////////////////////////////////////////
# if ('此處用於測試時代替真實玩家資料' == "with open('uesr_data.json','r',encoding='utf-8')") == False:
#     data={
#         "123": {
#             "name": "nekoha__suki",
#             "display_name": "\u8c93\u7fbd",
#             "global_name": "nekoha__suki",
#             "RPG":{
#                 "language":"zh_TW",
#                 "first_online_time":"2024-00-00 00:00:00.00000000",
#                 "color":"0x000000",
#                 "coins":0,
#                 "Race":"MoonRabbit",
#                 "EXP":{
#                     "now":0,
#                     "max":10
#                 },
#                 "Main_profession":{
#                     "class":"Thief",
#                     "level":0
#                 },
#                 "Sub_profession":{
#                     "Merchant":1,
#                     "Pharmacist":1,
#                     "Jeweler":1,
#                     "Floriculturist":1,
#                     "Chef":1,
#                     "Armourer":1,
#                     "Hammersmith":0
#                 },
#                 "attributes":{
#                     "HP":0,
#                     "SP":0,
#                     "MP":0,
#                     "ATK":0,
#                     "MATK":0,
#                     "DEF":0,
#                     "MDEF":0,
#                     "SPD":0,
#                     "AGI":0,
#                     "LUK":0,
#                     "CHR":0,
#                     "SAN":0
#                 },
#                 "item":{
#                     "Weapon":["Claw"],
#                     "Weapon_II":[""],
#                     "Weapon_III":[""],
#                     "Armor":["Leather_armor"],
#                     "Runes":[],
#                     "Flowers":[],
#                     "Gemstones":[],
#                     "Cuisine":[]
#                     },
#                 "handbook":{
#                     "Weapon":["Claw"],
#                     "Weapon_II":[""],
            
#                     "Weapon_III":[""],
#                     "Armor":["Leather_armor"],
#                     "Runes":[],
#                     "Flowers":[],
#                     "Gemstones":[],
#                     "Cuisine":[],
#                     "Hostile":[]
#                 },
#                 "PVP":{
#                     "win":0,
#                     "lose":0,
#                     "tie":0
#                 }
#             }
#         }
#     }
#     user = data['123']
# # user['RPG']['language'] = 'zh_TW'
# # user['RPG']['language'] = 'en_US'
# # user['RPG']['language'] = 'ja_JP'
# with open('cmds/rpg_define/format.json','r',encoding='utf-8') as Format_file:
#     format = json.load(Format_file)
# lang=format[user['RPG']['language']]["additional"]

# with open(f'cmds/rpg_define/{user['RPG']['language']}.lang','r',encoding='utf-8') as Lang_file:
#     for line in Lang_file:
#         line = line.strip()
#         if not line or line.startswith('#'):
#             continue
#         key, value = line.split('=', 1)
#         if value in format[user['RPG']['language']]["lang"]:
#             pass
#             lang[key] = format[user['RPG']['language']]["lang"][value]
#         else:
#             lang[key] = f'"{value}"'



            
# print(lang)
# introduce
# print(format[lang['profession']])
# print(lang)
# A ={
#     "RPG":{}
# }
# languge = {'languge':'zh_TW'}
# A['RPG'].update(languge)
# print(A['RPG'])
# languge = {'languge':'ja_JP'}
# A['RPG'].update(languge)
# print(A['RPG'])


# first_online_time=lang['first_online_time']
# user_first_online_time=user['RPG']['first_online_time']
# language=lang['language']
# user_language=user['RPG']['language']
# Race = lang['Race']
# user_Race = lang[user['RPG']['Race']]
# EXP = lang['EXP']
# user_EXP = {'max':user['RPG']['EXP']['max'],'now':user['RPG']['EXP']['now']}
# main_profession = lang['Main_profession']
# user_main_profession = {f'{lang['Main_profession']}{lang['class']}':lang[user['RPG']['Main_profession']['class']],lang['level']:user['RPG']['Main_profession']['level']}
# sub_professions = lang['Sub_profession']
# user_sub_professions = {lang['Merchant']:user['RPG']['Sub_profession']['Merchant'],lang['Pharmacist']:user['RPG']['Sub_profession']['Pharmacist'],lang['Jeweler']:user['RPG']['Sub_profession']['Jeweler'],lang['Floriculturist']:user['RPG']['Sub_profession']['Floriculturist'],lang['Chef']:user['RPG']['Sub_profession']['Chef'],lang['Armourer']:user['RPG']['Sub_profession']['Armourer'],lang['Hammersmith']:user['RPG']['Sub_profession']['Hammersmith']}
# user_color = user['RPG']['color']
# color = lang['color']
# # Character_Sheet = lang['character_sheet']
# EXP_bar=['/|','/|','/|','/|','/|','.:','.:','.:','.:','.:','.:','.:','.:','.:','.:']
# EXP_bar=f'{'/|'*int(15/user_EXP['max']*(user_EXP['now']))}{'.:'*(15-int(15/user_EXP['max']*(user_EXP['now'])))}'
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////
# print(EXP_bar)
# import random
# if '此處用於找出等級最高的副職業' != 1:
#     top_sub_profession = []
#     maxlave = []
#     for sub_profession_1 in user['RPG']['Sub_profession']:
#         maxlave.append(user['RPG']['Sub_profession'][sub_profession_1])
#         if user['RPG']['Sub_profession'][sub_profession_1] < max(maxlave):
#             maxlave.remove(user['RPG']['Sub_profession'][sub_profession_1])
#         for sub_profession_2 in user['RPG']['Sub_profession']:
#             if user['RPG']['Sub_profession'][sub_profession_1] > user['RPG']['Sub_profession'][sub_profession_2]:
#                 if {sub_profession_1:user['RPG']['Sub_profession'][sub_profession_1]} not in top_sub_profession:
#                     top_sub_profession.append({sub_profession_1:user['RPG']['Sub_profession'][sub_profession_1]})
#                 if {sub_profession_2:user['RPG']['Sub_profession'][sub_profession_2]}  in top_sub_profession:
#                     top_sub_profession.remove({sub_profession_2:user['RPG']['Sub_profession'][sub_profession_2]})
#     if top_sub_profession == []:
#         top_sub_profession.append({'full_equilibrium':user['RPG']['Sub_profession'][sub_profession_1]})
#     else:
#         random.shuffle(top_sub_profession)
#         maxlave = len(maxlave)-1
#     top_sub_profession = top_sub_profession[0]
    # top_sub_profession = {"class":list(top_sub_profession.keys())[0],"level":list(top_sub_profession.values())[0]}



#embed.add_field(
# name='',
# value=f'{'名稱':<3}: **{interaction.user.display_name}**\n
# lang['profession']: {lang[user['RPG']['Main_profession']['class']]:<5}Lv.{user['RPG']['Main_profession']['level']:<3}
# {'/':<2}{top_sub_profession['class']:<4}Lv.{top_sub_profession['level']:<5}\n
# {'種族':<3}: {Race}\n
# {'EXP':<4}: {EXP['now']} / {EXP['max']}\n
# `{str(EXP_bar)[1:-1].replace(',','').replace(' ','').replace("'",'')}`'
# #,inline=False)
# #embed.add_field(
# name='__**-------------------------------------**__',
# value=(f'|!__**H~P**__!| :_`{200:>4}`_\u3000|!__**S!A!N**__!| :_`{0:>4}`_\u3000\n|!__**S~P**__!| :_`{0:>4}`_\u3000|!__**M~P**__!| :_`{0:>4}`_\u3000\n|!__**A!T!K**__!| :_`{0:>4}`_\u3000|!__**MATK**__!| :_`{0:>4}`_\u3000\n|!__**D!E!F**__!| :_`{0:>4}`_\u3000|!__**MDEF**__!| :_`{0:>4}`_\u3000\n|!__**L!U!K**__!| :_`{0:>4}`_\u3000|!__**S!P!D**__!| :_`{0:>4}`_\u3000\n|!__**A!G!\u200BI\u2009**__!| :_`{0:>4}`_\u3000|!__**C!H!R**__!| :_`{0:>4}`_\u3000').replace('~','\u2009\u3000').replace('!','\u200A\u2004').replace(' ','\u2007\u200A')
#,inline=False)
                

# print(user['RPG']['Main_profession']['level'])


# from PIL import Image
# import os,random,shutil,asyncio
# directory = r'imege\rpg\color'
# shutil.rmtree(directory)
# os.makedirs(directory, exist_ok=True)
# width = 192
# height = 108

# async def tset():
#     listdir=os.listdir(directory)
#     for A in range(0x000000,0xffffff+1):
#         A1=(f'0x{(A):06x}.png')
#         if A1 not in listdir:
#             R = (A >> 16) & 0xff
#             G = (A >> 8) & 0xff
#             B = A & 0xff
#             file_path = os.path.join(directory, f'0x{R:02x}{G:02x}{B:02x}.png')
#             if not os.path.exists(file_path):
#                 image = Image.new('RGB', (width, height), (R, G, B))
#                 image.save(file_path, format='PNG')
#                 print(f'0x{R:02x}{G:02x}{B:02x}')
#             else:
#                 print(f'0x{R:02x}{G:02x}{B:02x}(重複)')

# asyncio.run(tset())

# #///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# #///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////








































































































































































































































































































# # #報時器
# # import datetime,asyncio
# # async def main():
# #     counter = 60
# #     while counter >0:
# #         time = datetime.datetime.now().strftime('%H:%M:%S')
# #         counter -= 1
# #         print(time,' || ',counter)
# #         await asyncio.sleep(1)
# # asyncio.run(main())








































































































































































































































































































# import discord
# from discord.ext import commands
# intents = discord.Intents.all()
# intents.typing = False
# intents.presences = False
# import json,asyncio
# with open('setting.json','r',encoding='utf-8') as setting_file:
#     setting = json.load(setting_file)
# bot = commands.Bot(command_prefix =[f'{setting["prefix"]}-','/'],intents = intents)
# prefix = 'a-'
# #機器人登陸通知
# @bot.event
# async def on_ready():
#     print('成功登陸嘍!!')
#     await bot.wait_until_ready()














#     await bot.close()

# async def main():
#     await bot.start(setting['TOKEN'])
# asyncio.run(main())