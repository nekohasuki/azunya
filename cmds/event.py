import discord
from discord.ext import commands
import json
with open("setting.json","r",encoding="utf8") as setting_file:
    setting = json.load(setting_file)
with open("dict.json","r",encoding="utf8") as dict_file:
    dict = json.load(dict_file)

from core.classes import Cog_extension
from core.error import Errors
import asyncio,datetime,os,random

now = datetime.datetime.now()
time = now.strftime("%H:%M")

class Event(Cog_extension):
    #"指令"錯誤報錯
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
        embed = discord.Embed(title="吉訊",url="https://www.jcolor.com.tw/jcolorfiles/release/product/pdt-868/pdt-8689539/medium.jpg",description="GOOD NEWS",colour=0xad0000,timestamp=now)
        embed.add_field(name="#最新消息：",value=f"User：\"__**{member}**__\"於今天的{time}\n奇蹟般的降臨了這個伺服器\n\n讓我們熱烈的歡迎!!!!!!!\n將祝福賜予User：__**{member}**__\n\n\n** **",inline=False)
        embed.add_field(name="#Latest News：",value=f"User：\"__**{member}**__\" in today's {time}\nMiraculously arrived at this server\n\nLet us give you a warm welcome!!!!!!!\nGive blessings to User: __**{member}**__",inline=False)
        channel = self.bot.get_channel(int(setting["WELCOME_CHANNEL_ID"]))
        guild = channel.guild
        await channel.send(f"歡!迎!{member.mention}!!",embed=embed)
        print(f'User:{member} 加入了[{guild}]伺服器!')
    #成員退出通知
    @commands.Cog.listener()
    async def on_member_remove(self,member):
        embed = discord.Embed(title="悲報",url="https://img.soundofhope.org/2024-03/1709580096451.jpg",description="SAD NEWS",colour=0x787878,timestamp=now)
        embed.add_field(name="#最新消息：",value=f"User：\"__**{member}**__\"於今天的{time}\n突然地離開了這個伺服器\n\n對此我們感到非常的難受\n願這伺服器，再無苦痛\n\n\n** **",inline=False)
        embed.add_field(name="#Latest News：",value=f"User：\"__**{member}**__\" in today's {time}\nLeft this server suddenly\n\nWe feel very uncomfortable about this\nI wish this server would have no more pain",inline=False)
        channel = self.bot.get_channel(int(setting["WELCOME_CHANNEL_ID"]))
        guild = channel.guild
        await channel.send(f"再見{member.mention}QAO",embed=embed)
        print(f'User:{member} 離開了[{guild}]伺服器!')
    #添加身分組
    @commands.Cog.listener()
    async def on_raw_reaction_add(self,reaction):
        guild = self.bot.get_guild(reaction.guild_id)
        user = guild.get_member(reaction.user_id)
        #第一組
        if str(reaction.message_id) == "1221830423592570910":
            if str(reaction.emoji) == setting["EMOJI_FREE"]:
                role = guild.get_role(int(setting["ROLE_ID"]))
                print(f"#|[{guild}] : User'{user}' add {reaction.emoji}-@{role}")
                await user.add_roles(role,reason=f"已為User: ' {user} ' 增添了 ' @{role} ' 的身分^W^!!!")
        # #第二組
        # if str(reaction.message_id) == "1222165371705098250":
        #     if str(reaction.emoji) == "✨":
        #         role = guild.get_role(1219645880831971408)
        #         print(reaction.emoji)
        #         print(f"{user} add role")
        #         await user.add_roles(role)
        # #第三組
        # if str(reaction.message_id) == "1222165371705098250":
        #     if str(reaction.emoji) == "<:LOGO1:1221378614524641332>":
        #         role = guild.get_role(1219645862502731876)
        #         print(reaction.emoji)
        #         print(f"{user} add role")
        #         await user.add_roles(role)
    #移除身分組
    @commands.Cog.listener()
    async def on_raw_reaction_remove(self,reaction):
        guild = self.bot.get_guild(reaction.guild_id)
        user = guild.get_member(reaction.user_id)
        #第一組
        if str(reaction.message_id) == "1221830423592570910":
            print(reaction.emoji)
            if str(reaction.emoji) == setting["EMOJI_FREE"]:
                role = guild.get_role(int(setting["ROLE_ID"]))
                print(f"#|[{guild}] : User'{user}' remove {reaction.emoji}-@{role}")
                await user.remove_roles(role,reason=f"User: ' {user} ' 不想要 ' @{role} ' 的身分了QQ")
        # #第二組
        # if str(reaction.message_id) == "1222165371705098250":
        #     if str(reaction.emoji) == "✨":
        #         role = guild.get_role(1219645880831971408)
        #         print(reaction.emoji)
        #         print(f"{user} remove role")
        #         await user.remove_roles(role)
        # #第三組
        # if str(reaction.message_id) == "1222165371705098250":
        #     if str(reaction.emoji) == "<:LOGO1:1221378614524641332>":
        #         role = guild.get_role(1219645862502731876)
        #         print(reaction.emoji)
        #         print(f"{user} remove role")
        #         await user.remove_roles(role) 
    #偵測到任一訊息時...
    @commands.Cog.listener()
    async def on_message(self,msg):
        print(msg)
        with open("setting.json","r",encoding="utf8") as setting_file:
            setting = json.load(setting_file)
        dict_my = dict["user_self-proclaimed"]
        dict_azunya = dict["azunya"]
        dict_omikuji = dict["omikuji"]
        #==:等於/!=:不等於
        #in:等於/not in:不等於
        #endswith:結束詞/startswith:開始詞
        #列表:<key= ["apple","banana"]>
        #and:以及/or:

        #……以及訊息不為自身(機器人)發出
        #<and msg.author != self.bot.user:>
        #……以及訊息中如果有包含關鍵字(key)
        #<and any(word in msg.content for word in key)>
        #……以及訊息等於關鍵字(key)
        #<and msg.content == key>

    #抽籤系統/URL
        if any(word in msg.content for word in (dict_azunya)) and any(word in msg.content for word in (dict_my)) and any(word in msg.content for word in (dict_omikuji)):
            with open("setting.json","r",encoding="utf8") as setting_file:
                setting = json.load(setting_file)
            with open("cmds\data\omikuji.json","r",encoding="utf8") as omikuji_file:
                omikuji = json.load(omikuji_file)
            Current_hours = datetime.datetime.now().strftime("%H")
            Current_minutes = datetime.datetime.now().strftime("%M")
            usercache = omikuji["userdata"]
            namecache = omikuji["namedata"]
            # guild = ctx.guild
            # channel = ctx.channel
            user = msg.author.id
            name = msg.author
            #如果當前時間等同於" setting["OmikujiTime"] "的設定時間
            if (f"{int(Current_hours)}:{int(Current_minutes)}") == setting["OmikujiTime"]:
                await msg.channel.send("系統維護中，請稍等1分鐘")
            else:
                #如果抽過了就回傳抽出結果
                if user in omikuji["userdata"]:
                    # pic = discord.File(f"imege\omikuji\{omikuji[f"{int(user)}"]}")
                    pic = discord.File(f"{omikuji[f"{int(user)}"]}")
                    await msg.channel.send(f"User : <@{user}>\n你今天已經抽過了啦!",file = pic)
                #沒抽過就抽出結果後更新資料進"omikuji.json"
                else:
                    random_pic = random.choice(os.listdir("./imege/omikuji"))
                    pic = discord.File(f"imege\omikuji\{random_pic}")
                    await msg.channel.send("抽出的結果是!!!!\n(搖籤筒聲)")
                    await asyncio.sleep (3)
                    await msg.channel.send(f"User :<@{user}>\n抽出抽出結果了!!快看快看!!!",file=pic)
                    #資料更新
                    usercache.append (user) 
                    namecache.append({f"{user}":f"{name}"})
                    omikuji_update = {"namedata":namecache,"userdata":usercache,f"{user}":f"imege\omikuji\{random_pic}"}
                    omikuji.update(omikuji_update)
                    with open("cmds\data\omikuji.json","w",encoding="utf8") as omikuji_file:
                        json.dump(omikuji,omikuji_file,indent=4)
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    #對話文本
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////










async def setup(bot):
    await bot.add_cog(Event(bot))