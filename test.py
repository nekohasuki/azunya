data={
    "RPG":{
        "language":"zh_TW",
        "first_online_time":"2024-00-00 00:00:00.00000000",
        "color":"0x000000",
        "coins":0,
        "Race":"MoonRabbit",
        "EXP":{
            "now":0,
            "max":10
        },
        "Main_profession":{
            "class":"Thief",
            "level":0
        },
        "Sub_profession":{
            "Merchant":0,
            "Pharmacist":0,
            "Jeweler":0,
            "Floriculturist":1,
            "Chef":0,
            "Armourer":0,
            "Hammersmith":0
        },
        "attributes":{
            "HP":0,
            "SP":0,
            "MP":0,
            "ATK":0,
            "MATK":0,
            "DEF":0,
            "MDEF":0,
            "SPD":0,
            "AGI":0,
            "LUK":0,
            "CHR":0,
            "SAN":0
        },
        "item":{
            "Weapon":["Claw"],
            "Weapon_II":[""],
            "Weapon_III":[""],
            "Armor":["Leather_armor"],
            "Runes":[],
            "Flowers":[],
            "Gemstones":[],
            "Cuisine":[]
            },
        "handbook":{
            "Weapon":["Claw"],
            "Weapon_II":[""],
    
            "Weapon_III":[""],
            "Armor":["Leather_armor"],
            "Runes":[],
            "Flowers":[],
            "Gemstones":[],
            "Cuisine":[],
            "Hostile":[]
        },
        "PVP":{
            "win":0,
            "lose":0,
            "tie":0
        }
    }
}
import json
# print(data['RPG']['language'])
with open(r'cmds\rpg_define\en_US.lang','r','utf-8') as Lang_fill:
    lang = Lang_fill.read()
    # lang = json.load(Lang_fill)
    print((lang))


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