from discord import app_commands,SelectOption
import json,os,random
# with open(f'cmds/rpg_define/rpg_definitions.json','r',encoding='utf-8') as RPG_definitions_fill: 
#     rpg_definitions = json.load(RPG_definitions_fill)
# with open(f'cmds/rpg_define/rpg_definitions.json','w',encoding='utf-8') as RPG_definitions_fill: 
#     json.dump(rpg_definitions,RPG_definitions_fill,indent=4)
open_file='''
with open('setting.json','r',encoding='utf-8') as setting_file:
    setting = json.load(setting_file)
with open('cmds/data/user_data.json' ,'r' ,encoding='utf-8') as userdata_file:
    userdata = json.load(userdata_file)
with open('cmds/rpg_define/format.json','r',encoding='utf-8') as Format_file:
    format = json.load(Format_file)
lang=format[Lang[0]]['additional']
lang.update(format['Shared']['additional'])
with open(f'cmds/rpg_define/{Lang[0]}.lang','r',encoding='utf-8') as Lang_file:
    for line in Lang_file:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        key,value = line.split('=',1)
        if value in format[Lang[0]]["lang"]:
            lang[key] = format[Lang[0]]["lang"][value]
        else:
            lang[key] = f'"{value}"'
for line in lang:
    if eval(lang[line]) in format[Lang[0]]['additional']:
        lang[line] = format[Lang[0]]['additional'][eval(lang[line])]

with open(f'cmds/rpg_define/rpg_definitions.json','r',encoding='utf-8') as RPG_definitions_fill:
    rpg_definitions = json.load(RPG_definitions_fill)
'''

Lang = ['zh_TW']
user = str(938100109240074310)

variable = {}
exec(open_file,globals(),variable)
userdata = variable.get('userdata')
setting = variable.get('setting')
lang = variable.get('lang')
rpg_definitions = variable.get('rpg_definitions')






point_list = []
for line in userdata:
    if line == str(697842681082281985):
        pass
    elif 'RPG' in userdata[line] and 'setting_mod' in userdata[line]['RPG'] and not userdata[line]['RPG']['setting_mod']:
        if 'point' in userdata[line] and userdata[line]['point']['now_count'] != 0:
            point_list.append(userdata[line]['point']['now_count'])
if point_list == []:
    point_list.append(1)


point_total = sum(point_list)
point_max = max(point_list)
point_min = min(point_list)
point_len = len(point_list)
if point_max <= 0:
    point_len = 1


print(point_list)
Exchange_rate = (point_total/point_max-point_total) / ((point_len**2*point_total)/point_max/(point_len+1)) *-1+1

print(rpg_definitions['Exchange_rate'])





# if '屬性':
#     Aa = 100
#     Bb = 1
#     A = int((Aa+Bb)/1.5)
#     B = int(abs(Aa-Bb)+(A/3))
#     if A > B:
#         a = A
#         A = B
#         B = a

#     print(A,B)
#     print(int(random.uniform(A-0.5,B)+.5))
# if '品階':
#     A = 10
#     B = 1

#     c=((((A+B)/2+B)/2+B)/2)
#     C=c+c-(c-1)
#     if A < C:
#         a=A
#         A=C
#         C=a

#     print(C,A,'\n\n')

#     print(int(random.uniform(C+0.5,A)+0.5))

# #--------------------------------------------------------------------------------------------------------
# if '這裡是自動處理*.ling的代碼':
#     Lang='ja_JP.lang'
#     Lang='en_US.lang'
#     lang=[]
#     with open(f'cmds/rpg_define/zh_TW.lang','r',encoding='utf-8') as Lang_file:
#         for zh_line in Lang_file:
#             zh_line = zh_line.strip()
#             if not zh_line or zh_line.startswith('#'):
#                 zh_key = zh_line
#             else:
#                 zh_key, zh_value = zh_line.split('=', 1)
#             lang.append(zh_key)
    
#             with open(f'cmds/rpg_define/{Lang}','r',encoding='utf-8') as Lang_file:
#                 for line in Lang_file:
#                     line = line.strip()
#                     value=None
#                     if not line or line.startswith('#'):
#                         continue
#                     key, value = line.split('=', 1)
#                     if value == '':
#                         value = '"error401"'
#                     if key in lang:
#                         lang.remove(key)
#                         if f'key' not in lang:
#                             lang.append(f'{key}={value}')
#     lang='\n'.join(lang)
#     print(lang)
#     #日文要檢查空白符號,因未知原因會自動卡一個空格
# #--------------------------------------------------------------------------------------------------------








































































































































































































































































































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