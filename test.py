
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








































































































































































































































































































import discord
from discord.ext import commands
intents = discord.Intents.all()
intents.typing = False
intents.presences = False
import json,asyncio
with open('setting.json','r',encoding='utf8') as setting_file:
    setting = json.load(setting_file)
bot = commands.Bot(command_prefix =[f'{setting["prefix"]}-','/'],intents = intents)
prefix = 'a-'
#機器人登陸通知
@bot.event
async def on_ready():
    print('成功登陸嘍!!')
    await bot.wait_until_ready()






    import datetime
    with open('cmds\\data\\user_data.json' , 'r' , encoding='utf8') as UserDataFile:
        userdata = json.load(UserDataFile)
#每月固定日期
    add_ponit_count = int(setting['add_ponit_count'])
    today =  datetime.datetime.now().strftime('%d')
    max_number = []
#<<<<<<<<<注意  VVV
    if today != setting['omikuji_reload_day']:
#比較壞運氣值最大的人

        for user in userdata:
            if 'omikuji' in userdata[user] and userdata[user]['omikuji']['badluck'] != None:
                max_number.append(userdata[user]['omikuji']['badluck'])
        print(max(max_number))

# #給予P點並重置所有人壞運氣值
#         add_ponit_user = []
#         for user in userdata:
#             if 'omikuji' in userdata[user]:
#                 if userdata[user]['omikuji']['badluck'] != None:
#                     add_ponit_user.append(f'**`{userdata[user]['display_name']}`**')
#                     userdata[user]['point'].ucpdate({'now_count':userdata[user]['point']['now_count']+add_ponit_count})
#                     userdata[user]['point'].update({'history_count':userdata[user]['point']['history_count']+add_ponit_count})
#                 userdata[user]['omikuji'].update({'badluck':0})
#         with open('cmds\\data\\user_data.json' , 'w' , encoding='utf8') as UserDataFile:
#             json.dump(userdata , UserDataFile , indent=4)



    # #聊天室留言
    #     channel = bot.get_guild(int(setting['GUILD_ID'])).get_channel(int(setting['MESSAGE_CHANNEL_ID']))
    #     await channel.send(f'**__本月運氣最差的人__**結果出來了!!!')
    #     if add_ponit_user != []:
    #         await asyncio.sleep(6)
    #         await channel.send(f'運氣最差的是 :\n{((str(add_ponit_user).replace("'", '')[1:-1]).replace(',','、'))}')
    #         await asyncio.sleep(8)
    #         await channel.send(f'雖然命運很坎坷，但請不要放棄生活的希望\n說不定前方等著你的是~~ ||更加黑暗|| ~~一片大好前程呢~')
    #         await asyncio.sleep(12)
    #         await channel.send(f'不過運氣不好確實不怎麼開心La，嗯...<:KANGAERU:1147177506294730752>\n這樣!這裡的{add_ponit_count}點P點就收下吧!\n怎麼樣有稍微開心點了嗎?\n未來也要好好ˇ哦打起精神窩=W=')
    #     else:
    #         await asyncio.sleep(3)
    #         await channel.send(f'本月運氣最差的人居然沒有嗎...')
    #         await asyncio.sleep(5)
    #         await channel.send(f'既然是這個結果就說明至少整整一個月都沒有人玩抽籤系統...')
    #         await asyncio.sleep(2)
    #         await channel.send(f'梓守我不信，難道沒有人想抽籤嗎?')
    #         await asyncio.sleep(1)
    #         await channel.send(f'看來這個伺服器不需要我了...')







    await bot.close()
    
async def main():
    await bot.start(setting['TOKEN'])
asyncio.run(main())
