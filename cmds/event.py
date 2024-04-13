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
        guild = self.bot.get_guild(reaction.guild_id)
        user = guild.get_member(reaction.user_id)
        print(reaction.emoji)
        #第一組
        if str(reaction.message_id) == setting['ROLE_MESSAGE_ID']:
            if str(reaction.emoji) == setting['EMOJI_FREE']:
                role = guild.get_role(int(setting['DEFAULT_ROLE_ID']))
                print(f'#|[{guild}] : User"{user}" add {reaction.emoji}-@{role}')
                await user.add_roles(role,reason=f'已為User: " {user} " 增添了 " @{role} " 的身分^W^!!!')
        #第二組
        if str(reaction.message_id) == setting['ROLE_MESSAGE_ID']:
            if str(reaction.emoji) == setting['EMOJI_GLOWING_STAR']:
                role = guild.get_role(int(setting['LOG_ROLE_ID']))
                print(f'#|[{guild}] : User"{user}" add {reaction.emoji}-@{role}')
                await user.add_roles(role)
        # #第三組
        if str(reaction.message_id) == setting['ROLE_MESSAGE_ID']:
            if str(reaction.emoji) == setting['EMOII_SECRET']:
                role = guild.get_role(int(setting['NSFW_ROLE_ID']))
                print(f'#|[{guild}] : User"{user}" add {reaction.emoji}-@{role}')
                await user.add_roles(role)
#移除身分組
    @commands.Cog.listener()
    async def on_raw_reaction_remove(self,reaction):
        guild = self.bot.get_guild(reaction.guild_id)
        user = guild.get_member(reaction.user_id)
        print(reaction.emoji)
        #第一組
        if str(reaction.message_id) == setting['ROLE_MESSAGE_ID']:
            if str(reaction.emoji) == setting['EMOJI_FREE']:
                role = guild.get_role(int(setting['DEFAULT_ROLE_ID']))
                print(f'#|[{guild}] : User"{user}" remove {reaction.emoji}-@{role}')
                await user.remove_roles(role,reason=f'User: " {user} " 不想要 " @{role} " 的身分了QQ')
        #第二組
        if str(reaction.message_id) == setting['ROLE_MESSAGE_ID']:
            if str(reaction.emoji) == setting['EMOJI_GLOWING_STAR']:
                role = guild.get_role(int(setting['LOG_ROLE_ID']))
                print(f'#|[{guild}] : User"{user}" remove {reaction.emoji}-@{role}')
                await user.remove_roles(role)
        # #第三組
        if str(reaction.message_id) == setting['ROLE_MESSAGE_ID']:
            if str(reaction.emoji) == setting['EMOII_SECRET']:
                role = guild.get_role(int(setting['NSFW_ROLE_ID']))
                print(f'#|[{guild}] : User"{user}" remove {reaction.emoji}-@{role}')
                await user.remove_roles(role)
    @commands.Cog.listener()
    async def on_message(self,ctx):
#前置設定
        with open('setting.json','r',encoding='utf8') as setting_file:
            setting = json.load(setting_file) 
        name = ctx.author.mention
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
        dict_food = dict['food']
        dict_morning = dict['morning']
        dict_afternoon = dict['afternoon']
        dict_evening = dict['evening']
        dict_night = dict['night']
        azunya = dict_azunya + dict_azukira
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
#問候
        if any(word in ctx.content for word in dict_azunya) and ctx.author.bot == False:
        #早上
            if any(word in ctx.content for word in dict_morning):
                if nowtime > '06:00:00' and nowtime < '11:00:00':
                    await ctx.channel.send(f'{name}也早安(≧ω≦)/\n{name}今天抽籤了嗎?')
                else:
                    await ctx.channel.send(f'早...安?')
        #中午~下午
            elif any(word in ctx.content for word in dict_afternoon):
                if nowtime > '11:00:00' and nowtime < '13:00:00':
                    food = random.choice(dict_food)
                    await ctx.channel.send(f'{name}午餐吃什麼??\n順帶一題我剛吃了{food}')
                elif nowtime > '13:00:00' and nowtime < '19:00:00':
                    await ctx.channel.send(f'{name}下午好呀~~')
                else:
                    await ctx.channel.send('午...安?\n等等,我看一下時間')
                    await asyncio.sleep(1)
                    await ctx.channel.send(f'現在好像是{nowtime}ㄟ')  
        #晚上                  
            elif any(word in ctx.content for word in dict_evening):
                if nowtime > '19:00:00' or nowtime < '03:00:00':
                    await ctx.channel.send(f'{name}晚上好呀晚上好')
                else:
                    await ctx.channel.send(f'{name}現在時間{nowtime}\n這時間可能不算晚喔?')
        #睡前
            elif any(word in ctx.content for word in dict_night):
                if nowtime > '19:00:00' and nowtime < '21:00:00':
                    await ctx.channel.send(f'{name}晚安,是說好早睡')
                elif nowtime > '21:00:00' or nowtime < '03:00:00':
                    await ctx.channel.send(f'{name}晚安,祝好夢')
                elif nowtime > '03:00:00' and nowtime < '06:00:00':
                    await ctx.channel.send(f'晚安?\n{name}也太晚睡了吧???')
                else:
                    await ctx.channel.send(f'蛤?晚安?')
                    await asyncio.sleep(1)
                    await ctx.channel.send(f'好吧...晚安...')
        #單純安安
            elif any(word in ctx.content for word in '安安'):
                await ctx.channel.send(f'{name}安安呀 安安 安安')
        #안녕하세요(你好)
            elif any(word in ctx.content for word in '安ニャー') and any(word in ctx.content for word in 'SAY') and any(word in ctx.content for word in '呦'):
                await ctx.channel.send(f'{name}안녕하세요')
#對話{
        #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#抽籤系統/URL
        if channel != log_channel:
            if any(word in ctx.content for word in (azunya)) and any(word in ctx.content for word in (dict_my)) and any(word in ctx.content for word in (dict_omikuji)):
                with open('setting.json','r',encoding='utf8') as setting_file:
                    setting = json.load(setting_file)
                with open('cmds\data\omikuji.json','r',encoding='utf8') as omikuji_file:
                    omikuji = json.load(omikuji_file)
                Current_hours = datetime.datetime.now().strftime('%H')
                Current_minutes = datetime.datetime.now().strftime('%M')
                usercache = omikuji['userdata']
                namecache = omikuji['namedata']
            #如果當前時間等同於' setting['OmikujiTime'] '的設定時間
                if (f'{int(Current_hours)}:{int(Current_minutes)}') == setting['OmikujiTime']:
                    await ctx.channel.send('系統維護中，請稍等1分鐘')
                else:
                #如果抽過了就回傳抽出結果
                    if user in omikuji['userdata']:
                        # pic = discord.File(f'imege\omikuji\{omikuji[f'{int(user)}']}')
                        pic = discord.File(f'{omikuji[f'{int(user)}']}')
                        await ctx.channel.send(f'User : <@{user}>\n你今天已經抽過了啦!',file = pic)
                #沒抽過就抽出結果後更新資料進'omikuji.json'
                    else:
                        random_pic = random.choice(os.listdir('./imege/omikuji'))
                        pic = discord.File(f'imege\omikuji\{random_pic}')
                        await ctx.channel.send('抽出的結果是!!!!\n(搖籤筒聲)')
                        await asyncio.sleep (3)
                        await ctx.channel.send(f'User :<@{user}>\n抽出抽出結果了!!快看快看!!!',file=pic)
                    #資料更新
                        usercache.append (user) 
                        namecache.append({f'{user}':f'{ctx.author}'})
                        omikuji_update = {'namedata':namecache,'userdata':usercache,f'{user}':f'imege\omikuji\{random_pic}'}
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
#訊息日誌
        if channel.id != log_channel.id and guild.id == int(setting['LOG_GUILD_ID']):
            await log_channel.send(f'{nowtime}\n**[ {guild} ]**　|　__{channel}__\n{name}(`ID:`||`{user}`||)：\n{msg} [`訊息連結`](https://discord.com/channels/{guild.id}/{channel.id}/{ctx.id})')










async def setup(bot):
    await bot.add_cog(Event(bot))