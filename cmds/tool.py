import discord
from discord.ext import commands
from discord import app_commands
import json
with open('setting.json','r',encoding='utf8') as setting_file:
    setting = json.load(setting_file)

from core.classes import Cog_extension
import asyncio,datetime,math,random
from typing import Optional

prefix = 't-'
class Tool(Cog_extension):
#刪除訊息
    commandname = (f'{prefix}clear')
    @app_commands.command(name = commandname,description = '刪除訊息(需要權限)')
    @app_commands.describe(count='輸入數量')
    @app_commands.checks.has_permissions (administrator=True)
    async def clear(self, interaction: discord.Interaction,count: Optional[int] = None):
        user = interaction.user.id
        if count == None:
            await interaction.response.send_message(f'請輸入需要刪除的訊息數量\n參考：\n```/clear 1```')
        elif count >200:
             count = 200
        if count == -402:
            await interaction.response.send_message(f'請User：<@{user}>稍等片刻\n正在啟動執行402號刪除程序 ')
            await asyncio.sleep(5)
            await interaction.channel.purge(limit=1)
            deleted = await interaction.channel.purge(limit=2147483648)
            await interaction.channel.send(f'已為USER : <@{user}>刪除{len(deleted)}條訊息')
        else:
            await interaction.response.send_message(f'請User：<@{user}>稍等片刻\n正在刪除{count}項訊息')
            await asyncio.sleep(3)
            await interaction.channel.purge(limit=1)
            deleted = await interaction.channel.purge(limit=count)
            await interaction.channel.send(f'已為USER : <@{user}>刪除{len(deleted)}條訊息')
        async for message in interaction.channel.history(limit=1):
            await asyncio.sleep(60)
            await interaction.channel.purge(check=lambda m: m.id == int(message.id))
#碼表
    commandname = (f'{prefix}stopwatch')
    @app_commands.command(name = commandname, description = '碼表')
    @app_commands.describe(hours='輸入小時數',minutes='輸入分鐘數',seconds='輸入秒數')
    async def stopwatch(self,interaction: discord.Interaction,hours: Optional[int] = None,minutes: Optional[int] = None,seconds: Optional[int] = None):
        if hours == None:
            hours=0
        if minutes == None:
            minutes=0
        if seconds == None:
            seconds=0
        t = (hours*60*60)+(minutes*60)+(seconds)
        if t >= 604800:
            t = 604800
        d = math.floor(t/60/60/24)
        h = math.floor(t/60/60-d*24)
        m = math.floor(t/60-h*60-d*60*24)
        s = t-d*60*60*24-h*60*60-m*60
        if d >= 1 :
            await interaction.response.send_message(f'好的User : {interaction.user.mention} !\n已將時間設定為**{int(d)}**天**{h}**時**{m}**分**{s}**秒\n開始到計時')
            message = await interaction.channel.send(f'剩餘時間 : **{int(d)}**天 **{h}**時**{m}**分**{s}**秒')
            while t >0:
                t -=1
                d = math.floor(t/60/60/24)
                h = math.floor(t/60/60-d*24)
                m = math.floor(t/60-h*60-d*60*24)
                s = t-d*60*60*24-h*60*60-m*60
                await asyncio.sleep(1)
                await message.edit(content=f'剩餘時間 : **{int(d)}**天 **{h}**時**{m}**分**{s}**秒')
        else:
            await interaction.response.send_message(f'好的User : {interaction.user.mention} !\n已將時間設定為**{h}**時**{m}**分**{s}**秒\n開始到計時')
            message = await interaction.channel.send(f'剩餘時間 :  **{h}**時**{m}**分**{s}**秒')
            while t >0:
                t -=1
                h = math.floor(t/60/60)
                m = math.floor(t/60-h*60)
                s = t-h*60*60-m*60
                await asyncio.sleep(1)
                await message.edit(content=f'剩餘時間 :  **{h}**時**{m}**分**{s}**秒')
        await interaction.channel.purge(check=lambda m: m.id == int(message.id))
        await interaction.channel.send(f'User：{interaction.user.mention}!!!\n之前碼表設定的時間跑完啦啦啦!!!!!')
#test-1
    commandname = (f'{prefix}test1')
    @app_commands.command(name = commandname, description = 'test-1')
    async def test1(self,interaction:discord.Integration):
        await interaction.channel.send(f'{interaction.guild.create_category_channel}\n ** **\n** ** create_category_channel\n ** **\n** **{interaction.guild.id}\n ** **\n** ** id\n ** **\n** **{interaction.guild.members}\n ** **\n** ** members\n ** **\n** **{interaction.guild.member_count}\n ** **\n** ** member_count\n ** **\n** **{interaction.guild.owner_id}\n ** **\n** ** owner_id\n ** **\n** **{interaction.guild.preferred_locale}\n ** **\n** ** preferred_locale\n ** **\n** **{interaction.guild.roles}\n ** **\n** ** roles\n ** **\n** **')
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#以梓喵身分發送訊息
    @commands.command()
    async def say(self,ctx, *,msg):
        print(msg)
        await ctx.channel.purge(limit=1)
        await ctx.send(msg)
#身分領取embed
    @commands.command()
    async def rulemessage(self, ctx):
        guild = ctx.guild
        msg = self.bot.get_channel(int(setting['ROLE_MESSAGE_CHANNEL_ID'])).get_partial_message(setting['ROLE_MESSAGE_ID'])
        #普通平民老百姓
        role_01 = guild.get_role(965668031114129438).mention
        #平民老百姓
        role_02 = guild.get_role(958806085274316870).mention
        #老百姓
        role_03 = guild.get_role(958829885504237598).mention
        #百姓
        role_04 = guild.get_role(959015027787042856).mention
        #永遠17的
        role_05 = guild.get_role(958812521907765308).mention
        #LOG
        role_06 = guild.get_role(1228288640627642379).mention
        #赫
        role_07 = guild.get_role(958826888950874192).mention
        #歌姬
        role_08 = guild.get_role(1079982786926100571).mention
        #不能說的秘密
        role_09 = guild.get_role(1080316995448352868).mention
        #無身份
        role_10 = guild.get_role(958827709272821770).mention
        embed = discord.Embed(title='**__請按照規則領取身份__**',url='https://discord.com/channels/1219180207534243891/1219815148622057523',description='** **',color=0xaa095f,timestamp=datetime.datetime.now())
        embed.set_author(name='Azumari :',url='https://github.com/nekohasuki/azunya/blob/main/azunya.py')
        embed.add_field(name=f'**現界[**一**]**',value=f'身分：{role_01}\n介紹：普通人\n條件：底下:free:按鈕領取\n** **',inline=True)
        embed.add_field(name=f'**現界[**二**]**',value=f'身分：{role_02}\n介紹：有錢\n　　　但還是普通人\n條件：現界一級並至少■■■■\n(條件未開放)',inline=True)
        embed.add_field(name=f'',value='** **',inline=False)
        embed.add_field(name=f'**現界[**三**]**',value=f'身分：{role_03}\n介紹：有錢有閒\n　　　但依然還是普通人\n條件：獲得現界二級並至少■■■■\n(條件未開放)',inline=True)
        embed.add_field(name=f'**現界[**四**]**',value=f'身分：{role_04}\n介紹：有錢有閒有權\n　　　即使如此卻依舊還是普通人\n條件：獲得現界三級並至少■■■■\n(條件未開放)',inline=True)
        embed.add_field(name=f'** **',value='**\n **',inline=False)
        embed.add_field(name=f'**特殊現界**',value=f'身分：{role_05}\n介紹：感覺18太老了所以是17www\n　　　(可以聊些有的沒的www)\n條件：底下:secret:按鈕領取\n\n** **',inline=False)
        embed.add_field(name=f'**訊息紀錄**',value=f'身分：{role_06}\n介紹：用於查看[__訊息紀錄__](https://discord.com/channels/958801205776248833/1227498587890516009)\n條件：底下:glowing_star:按鈕領取\n** **',inline=False)
        embed.add_field(name=f'**血族**',value=f'身分：{role_07}\n介紹：館館偷摸她雞\n　　　且可繞\'{role_05}&{role_04} \'之條件享受權力\n條件：請先預約並於[__休息室__](https://discord.com/channels/958801205776248833/958809630778195979)等候審核與評估\n\n** **',inline=False)
        embed.add_field(name=f'**特殊身份\n(特殊狀況可取)**',value=f'{role_08}\n{role_09}\n{role_10}',inline=False)
        embed.set_image(url=random.choice(setting['ROLE_MESSAGE_IMEGE']))
        embed.set_thumbnail(url=random.choice(setting['ROLE_MESSAGE_THUMBNAIL']))
        embed.set_footer(text='Copyright ⑨ 2024 N..S',icon_url='https://slate.dan.onl/slate.png')
        await msg.edit(embed = embed)
    @commands.command()
    async def embededit(self,ctx):
        import datetime
        now = datetime.datetime(2024,3,27,1,10)
        time = "01:10"
        member = ""
        channelid = ""
        msgid = ""
        msg = self.bot.get_channel(channelid).get_partial_message(msgid)
        embed = discord.Embed()
        await msg.edit(embed=embed)










async def setup(bot):
    await bot.add_cog(Tool(bot))