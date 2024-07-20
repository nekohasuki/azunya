import discord
from discord.ext import commands
import json
with open('setting.json','r',encoding='utf-8') as setting_file:
    setting = json.load(setting_file)
with open('dict.json','r',encoding='utf-8') as dict_file:
    dict = json.load(dict_file)

from core.classes import Cog_extension
from core.error import Errors
import asyncio,datetime,os,random

now = datetime.datetime.now()
time = now.strftime('%H:%M')

class Event(Cog_extension):
#'指令'錯誤報錯
    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):
        error_command = '{0}_error'.format(ctx.command)
        if hasattr(Errors,error_command):      # 檢查是否有 Custom Error Handler
            error_cmd = getattr(Errors,error_command)
            await error_cmd(self,ctx,error)
            return
        else:       # 使用 Default Error Handler
            await Errors.default_error(self,ctx,error)
#成員加入通知
    @commands.Cog.listener()
    async def on_member_join(self,member):
        now = datetime.datetime.now()
        embed = discord.Embed(title='吉訊',url='https://www.jcolor.com.tw/jcolorfiles/release/product/pdt-868/pdt-8689539/medium.jpg',description='GOOD NEWS',colour=0xad0000,timestamp=now)
        embed.add_field(name='#最新消息：',value=f'User：\"__**{member.mention}**__\"於今天的{time}\n奇蹟般的降臨了這個伺服器\n\n讓我們熱烈的歡迎!!!!!!!\n將祝福賜予User：__**{member.mention}**__\n\n\n** **',inline=False)
        embed.add_field(name='#Latest News：',value=f'User：\"__**{member.mention}**__\" in {"today's"} {time}\nMiraculously arrived at this server\n\nLet us give you a warm welcome!!!!!!!\nGive blessings to User: __**{member.mention}**__',inline=False)
        channel = self.bot.get_channel(int(setting['WELCOME_CHANNEL_ID']))
        guild = channel.guild
        await channel.send(f'歡!迎!{member.mention}!!',embed=embed)
        print(f'User:{member.mention} 加入了[{guild}]伺服器!')
#成員退出通知
    @commands.Cog.listener()
    async def on_member_remove(self,member):
        now = datetime.datetime.now()
        embed = discord.Embed(title='悲報',url='https://img.soundofhope.org/2024-03/1709580096451.jpg',description='SAD NEWS',colour=0x787878,timestamp=now)
        embed.add_field(name='#最新消息：',value=f'User：\"__**{member.mention}**__\"於今天的{time}\n突然地離開了這個伺服器\n\n對此我們感到非常的難受\n願這伺服器，再無苦痛\n\n\n** **',inline=False)
        embed.add_field(name='#Latest News：',value=f'User：\"__**{member.mention}**__\" in {"today's"} {time}\nLeft this server suddenly\n\nWe feel very uncomfortable about this\nI wish this server would have no more pain',inline=False)
        channel = self.bot.get_channel(int(setting['WELCOME_CHANNEL_ID']))
        guild = channel.guild
        await channel.send(f'再見{member.mention}QAO',embed=embed)
        print(f'User:{member.mention} 離開了[{guild}]伺服器!')
#添加身分組
    @commands.Cog.listener()
    async def on_raw_reaction_add(self,reaction):
        nowtime = datetime.datetime.now().strftime('%H:%M')
        guild = self.bot.get_guild(reaction.guild_id)
        user = guild.get_member(reaction.user_id)
        if user.bot == False:
            print(reaction.emoji)
            #第一組
            if str(reaction.message_id) == setting['ROLE_MESSAGE_ID']:
                if str(reaction.emoji) == setting['EMOJI_FREE']:
                    role = guild.get_role(int(setting['DEFAULT_ROLE_ID']))
                    print(f'{nowtime} | [{guild}] : User"{user}" add {reaction.emoji}-@{role}')
                    await user.add_roles(role,reason=f'已為User: " {user} " 增添了 " @{role} " 的身分^W^!!!')
            #第二組
            if str(reaction.message_id) == setting['ROLE_MESSAGE_ID']:
                if str(reaction.emoji) == setting['EMOJI_GLOWING_STAR']:
                    role = guild.get_role(int(setting['LOG_ROLE_ID']))
                    print(f'{nowtime} | [{guild}] : User"{user}"add {reaction.emoji}-@{role}')
                    await user.add_roles(role)
            #第三組
            if str(reaction.message_id) == setting['ROLE_MESSAGE_ID']:
                if str(reaction.emoji) == setting['EMOII_SECRET']:
                    role = guild.get_role(int(setting['NSFW_ROLE_ID']))
                    print(f'{nowtime} | [{guild}] : User"{user}"add {reaction.emoji}-@{role}')
                    await user.add_roles(role)
            #第四組
            if str(reaction.message_id) == setting['ROLE_MESSAGE_ID']:
                if str(reaction.emoji) == setting['EMOII_REGIONAL_INDICATOR_P']:
                    with open('cmds\\data\\user_data.json' , 'r' , encoding='utf-8') as userdata_file:
                        userdata = json.load(userdata_file)
                    counter = 0
                    for data in userdata:
                        if user.id == int(data):
                            counter += 1
                            userdata_update = userdata[f'{user.id}']
                            userdata_update['point']['state'] = True
                            userdata_update['name'] = user.name
                            userdata_update['display_name'] = user.display_name
                            userdata_update['global_name'] = user.global_name
                            userdata_update['top_role'] = f'<@&{user.top_role.id}>'
                            userdata[f'{user.id}'].update(userdata_update)
                            with open('cmds\\data\\user_data.json','w',encoding='utf-8') as userdata_file:
                                json.dump(userdata , userdata_file , indent=4)
                    if counter == 0:
                        if user.bot == False:
                            code=[]
                            if userdata == {}:
                                code.append('000')
                            else:
                                for data in userdata:
                                    if userdata[data]['code'] != "#NO":
                                        code.append(userdata[data]['code'])
                            userdata_update = {f'{user.id}':{'name':f'{user.name}','display_name':f'{user.display_name}','global_name':f'{user.global_name}','code':str(int(max(code))+1).zfill(3),'top_role':f'<@&{user.top_role.id}>','name_card':True,'point':{'state':True,'now_count':0,'history_count':0,'consumption':0,'give':0,'deprivation':0},'trade_count': 0,'VIP_tickets': 0,'VIP_chip': 0,"omikuji": {"badluck": 0,"today": None},"RPG":{},"recent_messages":{"url":"","time":""}}}
                        else:
                            userdata_update = {f'{user.id}':{'name':f'{user.name}','display_name':f'{user.display_name}','global_name':f'{user.global_name}','code':f'#NO','top_role':f'<@&{user.top_role.id}>','name_card':True,'point':{'state':True,'now_count':0,'history_count':0,'consumption':0,'give':0,'deprivation':0},'trade_count': 0,'VIP_tickets': 0,'VIP_chip': 0,"omikuji": {"badluck": 0,"today": None},"RPG":{},"recent_messages":{"url":"","time":""}}}
                        userdata.update(userdata_update)
                        with open('cmds\\data\\user_data.json','w',encoding='utf-8') as userdata_file:
                            json.dump(userdata , userdata_file , indent=4)
                    role = guild.get_role(int(setting['P_ROLE_ID']))
                    print(f'{nowtime} | [{guild}] : User"{user}"add {reaction.emoji}-@{role}')
                    await user.add_roles(role)
#移除身分組
    @commands.Cog.listener()
    async def on_raw_reaction_remove(self,reaction):
        nowtime = datetime.datetime.now().strftime('%H:%M')
        guild = self.bot.get_guild(reaction.guild_id)
        user = guild.get_member(reaction.user_id)
        if user.bot == False:
            print(reaction.emoji)
            #第一組
            if str(reaction.message_id) == setting['ROLE_MESSAGE_ID']:
                if str(reaction.emoji) == setting['EMOJI_FREE']:
                    role = guild.get_role(int(setting['DEFAULT_ROLE_ID']))
                    print(f'{nowtime} | [{guild}] : User"{user}"remove {reaction.emoji}-@{role}')
                    await user.remove_roles(role,reason=f'User: " {user} " 不想要 " @{role} " 的身分了QQ')
            #第二組
            if str(reaction.message_id) == setting['ROLE_MESSAGE_ID']:
                if str(reaction.emoji) == setting['EMOJI_GLOWING_STAR']:
                    role = guild.get_role(int(setting['LOG_ROLE_ID']))
                    print(f'{nowtime} | [{guild}] : User"{user}"remove {reaction.emoji}-@{role}')
                    await user.remove_roles(role)
            #第三組
            if str(reaction.message_id) == setting['ROLE_MESSAGE_ID']:
                if str(reaction.emoji) == setting['EMOII_SECRET']:
                    role = guild.get_role(int(setting['NSFW_ROLE_ID']))
                    print(f'{nowtime} | [{guild}] : User"{user}"remove {reaction.emoji}-@{role}')
                    await user.remove_roles(role)
            #第四組
            if str(reaction.message_id) == setting['ROLE_MESSAGE_ID']:
                if str(reaction.emoji) == setting['EMOII_REGIONAL_INDICATOR_P']:
                    with open('cmds\\data\\user_data.json' , 'r' , encoding='utf-8') as userdata_file:
                        userdata = json.load(userdata_file)
                    counter = 0
                    for data in userdata:
                        if user.id == int(data):
                            counter += 1
                            userdata_update = userdata[f'{user.id}']
                            userdata_update['point']['state'] = False
                            userdata_update['name'] = user.name
                            userdata_update['display_name'] = user.display_name
                            userdata_update['global_name'] = user.global_name
                            userdata_update['top_role'] = f'<@&{user.top_role.id}>'
                            userdata[f'{user.id}'].update(userdata_update)
                            with open('cmds\\data\\user_data.json','w',encoding='utf-8') as userdata_file:
                                json.dump(userdata , userdata_file , indent=4)
                    if counter == 0:
                        if user.bot == False:
                            code=[]
                            if userdata == {}:
                                code.append('000')
                            else:
                                for data in userdata:
                                    if userdata[data]['code'] != "#NO":
                                        code.append(userdata[data]['code'])
                            userdata_update = {f'{user.id}':{'name':f'{user.name}','display_name':f'{user.display_name}','global_name':f'{user.global_name}','code':str(int(max(code))+1).zfill(3),'top_role':f'<@&{user.top_role.id}>','name_card':True,'point':{'state':True,'now_count':0,'history_count':0,'consumption':0,'give':0,'deprivation':0},'trade_count': 0,'VIP_tickets': 0,'VIP_chip': 0,"omikuji": {"badluck": 0,"today": None},"RPG":{},"recent_messages":{"url":"","time":""}}}
                        else:
                            userdata_update = {f'{user.id}':{'name':f'{user.name}','display_name':f'{user.display_name}','global_name':f'{user.global_name}','code':f'#NO','top_role':f'<@&{user.top_role.id}>','name_card':True,'point':{'state':True,'now_count':0,'history_count':0,'consumption':0,'give':0,'deprivation':0},'trade_count': 0,'VIP_tickets': 0,'VIP_chip': 0,"omikuji": {"badluck": 0,"today": None},"RPG":{},"recent_messages":{"url":"","time":""}}}
                        userdata.update(userdata_update)
                        with open('cmds\\data\\user_data.json','w',encoding='utf-8') as userdata_file:
                            json.dump(userdata , userdata_file , indent=4)

                    role = guild.get_role(int(setting['P_ROLE_ID']))
                    print(f'{nowtime} | [{guild}] : User"{user}"remove {reaction.emoji}-@{role}')
                    await user.remove_roles(role)

    @commands.Cog.listener()
    async def on_message(self,ctx):
#前置設定
        with open('setting.json','r',encoding='utf-8') as setting_file:
            setting = json.load(setting_file)
        with open('dict.json','r',encoding='utf-8') as dict_file:
            dict = json.load(dict_file)
        with open('cmds\\data\\user_data.json' , 'r' , encoding='utf-8') as userdata_file:
            userdata = json.load(userdata_file)
        guild = ctx.guild
        channel = ctx.channel
        name = ctx.author.mention
        user = ctx.author.id
        global_name = guild.get_member(user).global_name
        display_name = guild.get_member(user).display_name
        nowtime = datetime.datetime.now().strftime('%H:%M:%S')
        msg = ctx.content
        log_channel = self.bot.get_channel(int(setting['MESSAGE_LOG_CHANNEL_ID']))
        nowtime = datetime.datetime.now().strftime('%H:%M:%S')
    #字典
        dict_my = dict['user_self-proclaimed']
        dict_azunya = dict['azunya']
        dict_azukira = dict['azukira']
        dict_omikuji = dict['omikuji']
        dict_dessert = dict['dessert']
        dict_morning = dict['morning']
        dict_afternoon = dict['afternoon']
        dict_evening = dict['evening']
        dict_night = dict['night']
        dict_go_to_Work = dict['go_to_Work']
        dict_get_off_work = dict['get_off_work']
        dict_Friday = dict['Friday'] 
        azunya = dict_azunya + dict_azukira
        dessert = random.choice(dict_dessert)
        #==:等於/!=:不等於
        #in:等於/not in:不等於
        #endswith:結束詞/startswith:開始詞
        #列表:<key= ['apple','banana']>
        #and:以及/or:

        #……以及訊息不為自身(機器人)發出
        #<and ctx.author != self.bot.user:>
        #……以及訊息中如果有包含關鍵字(key)
        #<and any(word in ctx.content for word in key)>
        #……以及訊息等於關鍵字(key)
        #<and ctx.content == key>
#訊息日誌
        if channel.id != log_channel.id and guild.id == int(setting['GUILD_ID']):
            if ctx.author.bot == False:
                await log_channel.send(f'{nowtime}\n**[ {guild} ]**　|　__{channel}__\n{name}(`ID:`||`{user}`||)：\n{msg} [`訊息連結`](https://discord.com/channels/{guild.id}/{channel.id}/{ctx.id})')
#問候
        if ctx.author.bot == False:
            await asyncio.sleep(0.1)
            random_1_5 = ['1','','','','']
            morning = [
                f'{name}也早安(≧ω≦]/\n{name}今天抽籤了嗎?',
                f'(火焰燃燒聲)(鍋具碰撞聲)\n哎呀~{name}起床啦~\n梓喵我正在幫自己做早餐呢\n{name}你也要吃嗎?是{dessert}呦~!',
                f'{name}早安呀早安呀~',
                f'{name}早~~\n梓守我打算吃{dessert}當早餐\n{name}也是嗎?',
                f'(已讀)'
            ]
            morning_Else = [
                f'早...安?',
                f'(望向時鐘)\n嗯?(歪頭)',
                f'{name}那裏的時區是早上嗎?'
            ]
            afternoon_A = [
                f'{name}午餐吃什麼?\n順帶一題梓守我剛吃了{dessert}',
                f'中午了~主機暖烘烘的好舒服~\n(suya~)',
                f'再一下下就是下午茶時間了,不知道有沒有人帶{dessert}來',
                f'(貌似睡得很安穩)',
                f'(揉眼)\n午安呀{name}\n梓守我剛剛夢到了自己在吃{dessert}\n(咕嚕咕嚕)\n討厭!肚子餓了啦!'
            ]
            afternoon_B = [
                f'{name}下午好呀~~',
                f'下午茶時間是用來休息的\n可以聊天也可以吃吃零食\n那個...{name}...\n其實...梓守我呀有一個夢想\n算了!果然還是不要講好了',
                f'(想事情中)\n\n嗯?阿!\n{name}是什麼時候過來的呀~\n在想什麼?\n喔喔!其實也沒什麼啦?只是在想明天的下午茶要吃什麼而已~',
                f'下午茶?\n說到下午茶當然是紅茶跟奶油蛋糕嘍~',
                f'(聊天喧鬧聲)\n啊!{name}你來了阿\n隨便找張椅子座就可以了\n我們正在喝下午茶呢!'
            ]
            afternoon_Else = [
                f'午...安?\n等等,我看一下時間\n現在好像是**{nowtime[:-3]}**ㄟ',
                f'Hey Google,現在的時間\nG：現在時間{nowtime}\n阿~原來是{nowtime[:-3]}呀!\n我還以為呢~',
                f'好吧?畢竟每個人對中午下午的定義都不一樣'
            ]
            evening = [
                f'{name}晚上好呀晚上好',
                f'{name}背我...(吃力)\n梓守我剛吃太飽了現在肘不動...',
                f'不知道今天晚上看不看的到星星\n{name}有看過星星嗎?',
                f'{name}吃晚餐了嗎?\n梓喵我今天晚餐吃{dessert}，可是這家做的{dessert}好難吃QAQ',
                f'晚上好阿{user}(哈欠聲)\n不知道怎麼了明明時間還很早的\n但是梓喵我卻好想睡\n振作點可不能睡著了(拍臉)'
            ]
            evening_Else = [
                f'{name}現在時間**{nowtime[:-3]}**\n這時間可能不算晚上喔?',
                f'聽說南北極即便到了晚上天空也可能是亮的\n但{name}你應該不是住南北極吧?',
                f'怎麼了{name}還在沉浸於昨天晚上嗎?'
            ]
            night_A = [
                f'{name}晚安,是說好早睡',
                f'{name}這麼早睡今天肯定很累吧?{name}今天一天辛苦了',
                f'怎麼這麼早睡?!!\n{name}身體不舒服嗎??',
                f'ㄟ?!!這就晚安了嗎?!!(失落)',
                f'喔喔~好早喔現在才**{nowtime[:-3]}**而已\n{name}你明天是要早起嗎?\n辛苦了~'
            ]
            night_B = [
                f'{name}晚安,祝好夢',
                f'晚安呀晚安晚安',
                f'{name}有好好睡覺呢~,好乖好乖'
            ]
            night_C = [
                f'晚安?\n{name}也太晚睡了吧???',
                f'看來{name}昨天晚上過得很充實喔',
                f'現在都已經**{nowtime[:-3]}**要不樣乾脆不睡了?',
                f'現在睡下去早上起得來嗎?(疑惑)',
                f'{name}~(皺眉)\n偶爾的話就算了,如果太這麼晚睡的話身體會壞掉喔!!'
            ]
            night_Else = [
                f'蛤?晚安?\n好吧...晚安...',
                f'晚安~\n嗯?現在是晚上嗎?',
                f'阿?晚安??\n難道{name}上夜班或夜校的嗎??'
            ]

        #早上
            if any(word in ctx.content for word in dict_morning):
                choice = random.choice(random_1_5)
                if choice == '1':
                    print(f'{nowtime[:-3]} | 梓喵回應了User : "{global_name}"的早安')
                    if nowtime > '06:00:00' and nowtime < '11:00:00':
                        await ctx.channel.send(random.choice(morning))
                    else:
                        await ctx.channel.send(random.choice(morning_Else))
                else:
                    print(f'{nowtime[:-3]} | User : "{global_name}" 觸發了早安')
        #中午~下午
            if any(word in ctx.content for word in dict_afternoon):
                choice = random.choice(random_1_5)
                if choice == '1':
                    print(f'{nowtime[:-3]} | 梓喵回應了User : "{global_name}"的午安')
                    if nowtime > '11:00:00' and nowtime < '13:00:00':
                        await ctx.channel.send(random.choice(afternoon_A))
                    elif nowtime > '13:00:00' and nowtime < '19:00:00':
                        await ctx.channel.send(random.choice(afternoon_B))
                    else:
                        await ctx.channel.send(random.choice(afternoon_Else))
                else:
                    print(f'{nowtime[:-3]} | User : "{global_name}" 觸發了午安')
        #晚上                  
            if any(word in ctx.content for word in dict_evening):
                choice = random.choice(random_1_5)
                if choice == '1':
                    print(f'{nowtime[:-3]} | 梓喵回應了User : "{global_name}"的晚上好')
                    if nowtime > '19:00:00' or nowtime < '03:00:00':
                        await ctx.channel.send(random.choice(evening))
                    else:
                        await ctx.channel.send(random.choice(evening_Else))
                else:
                    print(f'{nowtime[:-3]} | User : "{global_name}" 觸發了晚上好')
        #睡前
            if any(word in ctx.content for word in dict_night):
                choice = random.choice(random_1_5)
                if choice == '1':
                    print(f'{nowtime[:-3]} | 梓喵回應了User : "{global_name}"的晚安')
                    if nowtime > '19:00:00' and nowtime < '21:00:00':
                        await ctx.channel.send(random.choice(night_A))
                    elif nowtime > '21:00:00' or nowtime < '03:00:00':
                        await ctx.channel.send(random.choice(night_B))
                    elif nowtime > '03:00:00' and nowtime < '06:00:00':
                        await ctx.channel.send(random.choice(night_C))
                    else:
                        await ctx.channel.send(random.choice(night_Else))
                else:
                    print(f'{nowtime[:-3]} | User : "{global_name}" 觸發了晚安')
        #單純安安
            key = ['安安']
            if any(word in ctx.content for word in key):
                choice = random.choice(random_1_5)
                if choice == '1':
                    print(f'{nowtime[:-3]} | 梓喵回應了User : "{global_name}"的安安')
                    await ctx.channel.send(f'{name}安安呀 安安 安安')
                else:
                    print(f'{nowtime[:-3]} | User : "{global_name}" 觸發了安安')
        #안녕하세요(你好)
            if any(word in ctx.content for word in '安ニャー') and any(word in ctx.content for word in 'SAY') and any(word in ctx.content for word in '呦'):
                await ctx.channel.send(f'{name}안녕하세요')
#對話
        if ctx.author.bot == False:
            await asyncio.sleep(0.1)
            Friday_4 = [
                        '加油!在一天就放假了!!'
                    ]
            Friday_5 = [
                        '太棒了!明天放假耶!!'
                    ]
            # go_to_Work = []
            # get_off_work = []
        #上班上學
            if any(word in ctx.content for word in dict_go_to_Work):
                print(f'{nowtime[:-3]} | User : "{global_name}" 觸發了上班上學')
        #下班放學
            if any(word in ctx.content for word in dict_get_off_work):
                print(f'{nowtime[:-3]} | User : "{global_name}" 觸發了下班放學')
        # #週五
        #     if any(word in ctx.content for word in dict_Friday):
        #         print(f'{nowtime[:-3]} | User : "{global_name}" 觸發了週五')
        #         weekday = datetime.datetime.now().weekday()+1
        #         if weekday == 5:
        #             await ctx.channel.send(random.choice(Friday_5))
        #         elif weekday == 4:
        #             await ctx.channel.send(random.choice(Friday_4))
        
        # #暫時
        #     if any(word in ctx.content for word in (['嗨梓喵'])):
        #         await ctx.channel.send('你又想做什麼...')
        #     if any(word in ctx.content for word in (['幫你自己寫個RPG的遊戲'])):
        #         await ctx.channel.send('??????')
        #         await asyncio.sleep(1)
        #         await ctx.channel.send('我的開發者腦袋終於壞掉了嗎??')
        #     if any(word in ctx.content for word in (['所以不行嗎?'])):
        #         await ctx.channel.send('廢話，我又不是AI')
        #     if any(word in ctx.content for word in (['那你怎麼回我的'])):
        #         await ctx.channel.send('這不是你設定的指定文句觸發回復嗎?')




















#抽籤系統/URL
        if channel != log_channel:
            if any(word in ctx.content for word in (dict_azunya)) and any(word in ctx.content for word in (dict_my)) and any(word in ctx.content for word in (dict_omikuji)) and any(word not in ctx.content for word in (['/say'])):
            # if any(word in ctx.content for word in (azunya)) and any(word in ctx.content for word in (dict_my)) and any(word in ctx.content for word in (dict_omikuji)) and any(word not in ctx.content for word in (['/say'])):
                if user == (697842681082281985):
                    user = (938100109240074310)
                with open('setting.json','r',encoding='utf-8') as setting_file:
                    setting = json.load(setting_file)
                Current_hours = datetime.datetime.now().strftime('%H')
                Current_minutes = datetime.datetime.now().strftime('%M')
            #如果當前時間等同於' setting['omikuji_reload_time'] '的設定時間
                if (f'{int(Current_hours)}:{int(Current_minutes)}') == setting['omikuji_reload_time']:
                    await ctx.channel.send('系統維護中，請稍等1分鐘')
                else:
                #防覆寫
                    await asyncio.sleep(random.uniform(random.uniform(0,0.1),1))
                    while os.path.exists('cmds\data\omikuji.lock') == True:
                        await asyncio.sleep(1)
                    open('cmds\data\omikuji.lock', 'w').close()
                    with open('cmds\data\omikuji.json','r',encoding='utf-8') as omikuji_file:
                        omikuji = json.load(omikuji_file)
                #抓資料
                    counter = 0
                    for userid in omikuji:
                        if counter == 1:
                            break
                        if str(user) == str(userid):
                            counter += 1
                        else:
                            pass
                #如果抽過了就告訴用戶抽出結果
                    if counter == 1:
                        pic = discord.File(omikuji[f'{user}']['pic'])
                        await ctx.channel.send(f'User : <@{ctx.author.id}>\n你今天已經抽過了啦!\n今日運勢：{omikuji[f'{user}']['pic'][13:-4]}',file = pic)
                #沒抽過就抽出結果後告訴用戶抽出結果
                    elif counter == 0:
                        random_pic = random.choice(os.listdir('./imege/omikuji'))
                        pic = discord.File(f'imege\omikuji\{random_pic}')
                        await ctx.channel.send(f'為User :<@{user}>抽出的結果是!!!!\n(搖籤筒聲)')
                        await asyncio.sleep (3)
                        await ctx.channel.send(f'抽出抽出結果了!!快看快看!!!\n今日運勢：{random_pic[:-4]}',file=pic)                       
                    #omikuji資料更新
                        omikuji_update = {f'{user}':{'name':f'{display_name}','pic':f'imege\omikuji\{random_pic}'}}
                        omikuji.update(omikuji_update)
                        with open('cmds\data\omikuji.json','w+',encoding='utf-8') as omikuji_file:
                            json.dump(omikuji,omikuji_file,indent=4)
                    #如果用戶有在'user_data.json'裡就存進去,否則聊天室回復訊息
                        counter = 0
                        for userid in userdata:
                            if counter == 1:
                                break
                            if str(user) == str(userid):
                                counter += 1
                            else:
                                pass
                        if counter  == 1:
                            user_pic = random_pic[:-4]
                            if '¤' in user_pic:
                                if 'omikuji' in userdata[f'{user}']:
                                    userdata[f'{user}']['omikuji'].update({'badluck':userdata[f'{user}']['omikuji']['badluck'],'today':0})
                                elif 'omikuji' not in userdata[f'{user}']:
                                    userdata[f'{user}'].update({'omikuji':{'badluck':0,'today':0,}})
                            if '★' in user_pic:
                                counter = 0
                                while '★' in user_pic:
                                    counter += 1
                                    user_pic=user_pic[1:]
                                if 'x' in user_pic:
                                    today = int(user_pic[1:])-1+counter
                                else:
                                    today = counter
                                if 'omikuji' in userdata[f'{user}']:
                                        userdata[f'{user}']['omikuji'].update({'badluck':userdata[f'{user}']['omikuji']['badluck'],'today':today})
                                elif 'omikuji' not in userdata[f'{user}']:
                                    userdata[f'{user}'].update({'omikuji':{'badluck':0,'today':today}})
                            if '☆' in user_pic:
                                counter = 0
                                while '☆' in user_pic:
                                    counter += 1
                                    user_pic=user_pic[1:]
                                if 'x' in user_pic:
                                    today = (int(user_pic[1:])-1+counter)*-1
                                else:
                                    today = counter*-1
                                if 'omikuji' in userdata[f'{user}']:
                                        userdata[f'{user}']['omikuji'].update({'badluck':userdata[f'{user}']['omikuji']['badluck'],'today':today})
                                elif 'omikuji' not in userdata[f'{user}']:
                                    userdata[f'{user}'].update({'omikuji':{'badluck':0,'today':today}})
                            with open('cmds\\data\\user_data.json' , 'w' , encoding='utf-8') as userdata_file:
                                json.dump(userdata , userdata_file , indent=4)
                        else:
                            await ctx.channel.send(f'是說 User :<@{user}>\n你好像沒有註冊P卡喔\n沒有註冊的話是不能參與比賽的\n現在去註冊的話今天00:00一過再抽籤就可以比賽嘍^W^')
                    os.remove('cmds\data\omikuji.lock')
    # #不要用那個稱呼
    #         if any(word in ctx.content for word in dict_azukira) and ctx.author.bot == False:
    #             if user == (703238602586456114):
    #                 await asyncio.sleep(1)
    #                 await ctx.channel.send(f'嘴巴閉閉\n不會講話就不要講\n你是知道我有名字的')
    #             elif user == (849505185364967475):
    #                 await asyncio.sleep(1)
    #                 await ctx.channel.send(f'不要用那個稱呼叫我!!!**あきら1966**\n我有名字的**あきら1966**\n叫__梓守__!,或者也可以叫我__梓喵__')
    #                 await asyncio.sleep(2)
    #                 await ctx.channel.send(f'聽懂了沒有**あきら1966**')
    #             elif user == (697842681082281985) or user == (938100109240074310):
    #                 await asyncio.sleep(1)
    #                 await ctx.channel.send(f'不對吧,你叫錯就太誇張了吧QAQ')
    #             else:
    #                 await asyncio.sleep(1)
    #                 await ctx.channel.send(f'還有，{name}不要用那個稱呼叫我!!!\n我叫__梓守__!,或者也可以叫我__梓喵__')










async def setup(bot):
    await bot.add_cog(Event(bot))