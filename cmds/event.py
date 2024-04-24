import discord
from discord.ext import commands
import json
with open('setting.json','r',encoding='utf8') as setting_file:
    setting = json.load(setting_file)
with open('dict.json','r',encoding='utf8') as dict_file:
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
                    role = guild.get_role(int(setting['P_ROLE_ID']))
                    print(f'{nowtime} | [{guild}] : User"{user}"remove {reaction.emoji}-@{role}')
                    await user.remove_roles(role)
    @commands.Cog.listener()
    async def on_message(self,ctx):
#前置設定
        with open('setting.json','r',encoding='utf8') as setting_file:
            setting = json.load(setting_file)
        with open('dict.json','r',encoding='utf8') as dict_file:
            dict = json.load(dict_file)
        name = ctx.author.mention
        global_name = ctx.author.global_name
        user = ctx.author.id
        guild = ctx.guild
        channel = ctx.channel
        nowtime = datetime.datetime.now().strftime('%H:%M:%S')
        msg = ctx.content
        log_channel = self.bot.get_channel(int(setting['LOG_CHANNEL_ID']))
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
        if channel.id != log_channel.id and guild.id == int(setting['LOG_GUILD_ID']):
            if ctx.author.bot == False:
                await log_channel.send(f'{nowtime}\n**[ {guild} ]**　|　__{channel}__\n{name}(`ID:`||`{user}`||)：\n{msg} [`訊息連結`](https://discord.com/channels/{guild.id}/{channel.id}/{ctx.id})')
#問候
        if ctx.author.bot == False:
            await asyncio.sleep(0.1)
            random_1_10 = ["1","","","","","","","","",""]
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
                choice = random.choice(random_1_10)
                if choice == "1":
                    print(f'{nowtime[:-3]} | 梓喵回應了User : "{global_name}"的早安')
                    if nowtime > '06:00:00' and nowtime < '11:00:00':
                        await ctx.channel.send(random.choice(morning))
                    else:
                        await ctx.channel.send(random.choice(morning_Else))
                else:
                    print(f'{nowtime[:-3]} | User : "{global_name}" 觸發了早安')
        #中午~下午
            if any(word in ctx.content for word in dict_afternoon):
                choice = random.choice(random_1_10)
                if choice == "1":
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
                choice = random.choice(random_1_10)
                if choice == "1":
                    print(f'{nowtime[:-3]} | 梓喵回應了User : "{global_name}"的晚上好')
                    if nowtime > '19:00:00' or nowtime < '03:00:00':
                        await ctx.channel.send(random.choice(evening))
                    else:
                        await ctx.channel.send(random.choice(evening_Else))
                else:
                    print(f'{nowtime[:-3]} | User : "{global_name}" 觸發了晚上好')
        #睡前
            if any(word in ctx.content for word in dict_night):
                choice = random.choice(random_1_10)
                if choice == "1":
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
                choice = random.choice(random_1_10)
                if choice == "1":
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
        #週五
            if any(word in ctx.content for word in dict_Friday):
                print(f'{nowtime[:-3]} | User : "{global_name}" 觸發了週五')
                weekday = datetime.datetime.now().weekday()+1
                if weekday == 5:
                    await ctx.channel.send(random.choice(Friday_5))
                elif weekday == 4:
                    await ctx.channel.send(random.choice(Friday_4))
#抽籤系統/URL
        if channel != log_channel:
            if any(word in ctx.content for word in (azunya)) and any(word in ctx.content for word in (dict_my)) and any(word in ctx.content for word in (dict_omikuji)):
                if user == (697842681082281985):
                    user = (938100109240074310)
                with open('setting.json','r',encoding='utf8') as setting_file:
                    setting = json.load(setting_file)
                with open('cmds\data\omikuji.json','r',encoding='utf8') as omikuji_file:
                    omikuji = json.load(omikuji_file)
                Current_hours = datetime.datetime.now().strftime('%H')
                Current_minutes = datetime.datetime.now().strftime('%M')
            #如果當前時間等同於' setting['OmikujiTime'] '的設定時間
                if (f'{int(Current_hours)}:{int(Current_minutes)}') == setting['OmikujiTime']:
                    await ctx.channel.send('系統維護中，請稍等1分鐘')
                else:
                    counter = 0
                    for userid in omikuji:
                        if counter == 1:
                            break
                        if str(user) == str(userid):
                            counter += 1
                        else:
                            pass
                    if counter == 1:
                        pic = discord.File(omikuji[f"{user}"]["pic"])
                        await ctx.channel.send(f'User : <@{ctx.author.id}>\n你今天已經抽過了啦!\n今日運勢：{omikuji[f"{user}"]["pic"][13:-4]}',file = pic)
                #沒抽過就抽出結果後更新資料進'omikuji.json'
                    elif counter == 0:
                        random_pic = random.choice(os.listdir('./imege/omikuji'))
                        pic = discord.File(f'imege\omikuji\{random_pic}')
                        await ctx.channel.send('抽出的結果是!!!!\n(搖籤筒聲)')
                        await asyncio.sleep (3)
                        await ctx.channel.send(f'User :<@{user}>\n抽出抽出結果了!!快看快看!!!\n今日運勢：{random_pic[:-4]}',file=pic)
                    #資料更新
                        omikuji_update = {f'{user}':{"name":"","pic":""}}
                        omikuji_update[f'{user}']["name"] = f'{ctx.author}'
                        omikuji_update[f'{user}']["pic"] = f'imege\omikuji\{random_pic}'
                        omikuji.update(omikuji_update)
                        with open('cmds\data\omikuji.json','w',encoding='utf8') as omikuji_file:
                            json.dump(omikuji,omikuji_file,indent=4)
    #不要用那個稱呼
            if any(word in ctx.content for word in dict_azukira) and ctx.author.bot == False:
                if user == (703238602586456114):
                    await asyncio.sleep(1)
                    await ctx.channel.send(f'嘴巴閉閉\n不會講話就不要講\n你是知道我有名字的')
                elif user == (849505185364967475):
                    await asyncio.sleep(1)
                    await ctx.channel.send(f'不要用那個稱呼叫我!!!**あきら1966**\n我有名字的**あきら1966**\n叫__梓守__!,或者也可以叫我__梓喵__')
                    await asyncio.sleep(2)
                    await ctx.channel.send(f'聽懂了沒有**あきら1966**')
                elif user == (697842681082281985) or user == (938100109240074310):
                    await asyncio.sleep(1)
                    await ctx.channel.send(f'不對吧,你叫錯就太誇張了吧QAQ')
                else:
                    await asyncio.sleep(1)
                    await ctx.channel.send(f'還有，{name}不要用那個稱呼叫我!!!\n我叫__梓守__!,或者也可以叫我__梓喵__')










async def setup(bot):
    await bot.add_cog(Event(bot))