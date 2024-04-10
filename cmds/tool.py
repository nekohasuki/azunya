import discord
from discord.ext import commands
from discord import app_commands
import json
with open("setting.json","r",encoding="utf8") as setting_file:
    setting = json.load(setting_file)

from core.classes import Cog_extension
import asyncio,datetime,math,random
from typing import Optional

class Tool(Cog_extension):
#刪除訊息  
    @app_commands.command(name = "clear", description = "刪除訊息(需要權限)")
    @app_commands.describe(count="輸入數量")
    @app_commands.checks.has_permissions (administrator=True)
    async def clear(self, interaction: discord.Interaction,count: Optional[int] = None):
        user = interaction.user.id
        if count == None:
            await interaction.response.send_message(f"請輸入需要刪除的訊息數量\n參考：\n/clear 1")
        elif count > 200:
             count = 200
        if count == -402:
            await interaction.response.send_message(f"請User：<@{user}>稍等片刻\n正在啟動執行402號刪除程序 ")
            await asyncio.sleep(5)
            await interaction.channel.purge(limit=1)
            deleted = await interaction.channel.purge(limit=2147483648)
            await interaction.channel.send(f'已為USER : <@{user}>刪除{len(deleted)}條訊息')
        else:
            await interaction.response.send_message(f"請User：<@{user}>稍等片刻\n正在刪除{count}項訊息")
            await asyncio.sleep(3)
            await interaction.channel.purge(limit=1)
            deleted = await interaction.channel.purge(limit=count)
            await interaction.channel.send(f'已為USER : <@{user}>刪除{len(deleted)}條訊息')
        async for message in interaction.channel.history(limit=1):
            await asyncio.sleep(60)
            await interaction.channel.purge(check=lambda m: m.id == int(message.id))
#碼表
    @app_commands.command(name = "stopwatch", description = "碼表")
    @app_commands.describe(hours="輸入小時數",minutes="輸入分鐘數",seconds="輸入秒數")
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
            while t > 0:
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
            while t > 0:
                t -=1
                h = math.floor(t/60/60)
                m = math.floor(t/60-h*60)
                s = t-h*60*60-m*60
                await asyncio.sleep(1)
                await message.edit(content=f'剩餘時間 :  **{h}**時**{m}**分**{s}**秒')
        await interaction.channel.purge(check=lambda m: m.id == int(message.id))
        await interaction.channel.send(f'User：{interaction.user.mention}!!!\n之前碼表設定的時間跑完啦啦啦!!!!!')
#查詢用戶ID
    @app_commands.command(name = "myid", description = "查詢Discird的ID")
    async def myid(self,interaction:discord.Integration):
        user = interaction.user
        await interaction.response.send_message(f"User：<@{user.id}>\n你的ID是__{user.id}__呦!")
#test-1
    @app_commands.command(name = "test1", description = "test-1")
    async def test1(self,interaction:discord.Integration):
        await interaction.channel.send(f"{interaction.guild.create_category_channel}\n ** **\n** ** create_category_channel\n ** **\n** **{interaction.guild.id}\n ** **\n** ** id\n ** **\n** **{interaction.guild.members}\n ** **\n** ** members\n ** **\n** **{interaction.guild.member_count}\n ** **\n** ** member_count\n ** **\n** **{interaction.guild.owner_id}\n ** **\n** ** owner_id\n ** **\n** **{interaction.guild.preferred_locale}\n ** **\n** ** preferred_locale\n ** **\n** **{interaction.guild.roles}\n ** **\n** ** roles\n ** **\n** **")
#test-2
    @app_commands.command(name = "test2", description = "test-2")
    async def test2(self,interaction:discord.Integration):
        B =1219645881838600293
        A = interaction.guild.get_role(B)
        await interaction.response.send_message(f"# color:\n   {A.color}\n# created_at:\n    {A.created_at}\n# id:\n   {A.id}\n# members:\n  {A.members}\n# permissions:\n    {A.permissions}")
  
# manage_guild
# value
# manage_messages

# permission
# discord.Member
# get_role("id")

    # color
    # created_at
    # id
    # members
    # permissions

# add_reactions
# administrator
# attach_files
# ban_members
# change_nickname
# connect
# create_expressions
# create_instant_invite
# create_private_threads
# create_public_threads
# deafen_members
# embed_links
# external_emojis
# external_stickers
# kick_members
# manage_channels
# manage_emojis
# manage_emojis_and_stickers
# manage_events
# manage_expressions
# manage_nicknames
# manage_permissions
# manage_roles
# manage_threads
# manage_webhooks
# mention_everyone
# moderate_members
# move_members
# mute_members
# priority_speaker
# read_message_history
# read_messages
# request_to_speak
# send_messages
# send_messages_in_threads
# send_tts_messages
# send_voice_messages
# speak
# stream
# use_application_commands
# use_embedded_activities
# use_external_emojis
# use_external_sounds
# use_external_stickers
# use_soundboard
# use_voice_activation
# view_audit_log
# view_channel
# view_guild_insights

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#以梓喵身分發送訊息
    @commands.command()
    async def say(self,ctx, *,msg):
        print(msg)
        await ctx.channel.purge(limit=1)
        await ctx.send(msg)
#身分領取embed
    @commands.command()
    async def rulemessage(self, ctx):
        embed = discord.Embed(title="**__請按照規則領取身份__**",url="https://discord.com/channels/1219180207534243891/1219815148622057523",description="** **",color=0xaa095f,timestamp=datetime.datetime.now())
        embed.set_author(name="Azumari :",url="https://github.com/nekohasuki/azunya/blob/main/azunya.py")
        embed.add_field(name="**現界[**一**]** - @普通平民老百姓",value="介紹：普通人\n條件：底下:free:按鈕領取\n** **",inline=True)
        embed.add_field(name="**現界[**二**]** - @平民老百姓",value="介紹：有錢\n　　　但還是普通人\n條件：現界一級並至少■■■■\n(條件未開放)",inline=True)
        embed.add_field(name="",value="** **",inline=False)
        embed.add_field(name="**現界[**三**]** - @老百姓",value="介紹：有錢有閒\n　　　但依然還是普通人\n條件：獲得現界二級並至少■■■■\n(條件未開放)",inline=True)
        embed.add_field(name="**現界[**四**]** - @百姓",value="介紹：有錢有閒有權\n　　　即使如此卻依舊還是普通人\n條件：獲得現界三級並至少■■■■\n(條件未開放)",inline=True)
        embed.add_field(name="** **",value="**\n **",inline=False)
        embed.add_field(name="**特殊現界** - @永遠17的",value="介紹：感覺18太老了所以是17www\n　　　(可以聊些有的沒的www)\n條件：請出示成年的證明\n\n** **",inline=False)
        embed.add_field(name="**血族** - @赫",value="介紹：館館&偷摸她雞\n　　　且可繞\"@永遠17的&@百姓\"之條件享受權力\n條件：請先預約並於休息室(#會客室 )等候審核與評估\n\n** **",inline=False)
        embed.add_field(name="**特殊身份(特殊狀況可取):**",value="@歌姬\n@不能說的秘密\n@無身份",inline=False)
        embed.set_image(url=random.choice(setting["ROLE_MESSAGE_IMEGE"]))
        embed.set_thumbnail(url=random.choice(setting["ROLE_MESSAGE_THUMBNAIL"]))
        embed.set_footer(text="Copyright ⑨ 2024 N..S",icon_url="https://slate.dan.onl/slate.png")
        await ctx.send(embed=embed)










async def setup(bot):
    await bot.add_cog(Tool(bot))