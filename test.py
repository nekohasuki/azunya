


# import json,datetime
# userdata = {"user_a" : {"count":1},"user_b" : {"count":-1},"user_c" : {"count":-1}}
# userlist = []
# for user in userdata:
#     if "count" in userdata[user] and userdata[user]['count'] != None:
#         userlist.append(userdata[user]['count'])
# for user in userdata:
#     if "count" in userdata[user] and userdata[user]['count'] == (min(userlist)):
#         print(user)


# #///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# #比較數字最小壞運氣值+1
# for user_a in userdata:
#     for user_b in userdata:
#         if 'omikuji' in userdata[user_a] and 'omikuji' in userdata[user_b] and user_a != user_b:
#             user.update({user_a:userdata[user_a],user_b:userdata[user_b]})
#             if user[user_a]['omikuji']['today'] != None and user[user_b]['omikuji']['today'] != None and user[user_a]['omikuji']['today'] != user[user_b]['omikuji']['today']:
#                 if user[user_a]['omikuji']['today'] > user[user_b]['omikuji']['today']:
#                     user[user_a]['omikuji'].update({'today':None})
#                 else:
#                     user[user_b]['omikuji'].update({'today':None})
# bad_luck_user = []
# for user_a in user:
#     if user[user_a]['omikuji']['today'] != None:
#         bad_luck_user.append(f'**`{userdata[user_a]['display_name']}`**')
#         userdata[user_a].update({'omikuji':{'badluck':user[user_a]['omikuji']['badluck']+1,'today':None}})
#     with open('cmds\\data\\user_data.json' , 'w' , encoding='utf8') as UserDataFile:
#         json.dump(userdata , UserDataFile , indent=4)
# #聊天室留言
# channel = self.bot.get_guild(int(setting['GUILD_ID'])).get_channel(int(setting['MESSAGE_CHANNEL_ID']))
# if bad_luck_user != []:
#     await channel.send(f'今天運氣最差的是 :\n{((str(bad_luck_user).replace("'", '')[1:-1]).replace(',','、'))}')
# else:
#     await channel.send(f'今天運氣最差的是!!')
#     await asyncio.sleep(.5)
#     await channel.send(f'???')
#     await asyncio.sleep(2)
#     await channel.send(f'難道今天沒有人抽籤嗎?QQ')
#     await asyncio.sleep(1)
#     await channel.send(f'梓守我不被需要了嗎Q^O')


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
# with open('setting.json','r',encoding='utf8') as setting_file:
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
