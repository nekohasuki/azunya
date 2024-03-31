import discord
from discord.ext import commands

import json
with open("setting.json","r",encoding="utf8") as setting_file:
    setting = json.load(setting_file)

import random,datetime,asyncio

from core.classes import Cog_extension

Current_Time = datetime.datetime.now().strftime("%H:%M")

class React(Cog_extension):
    #指定圖片/PATH
    @commands.command()
    async def imege(self, ctx):
        pic = discord.File(setting["Imege"])
        await ctx.send(file = pic)
    #隨機圖片/PATH
    @commands.command()
    async def logo(self, ctx):
        random_pic = random.choice(setting["Logo"])
        pic = discord.File(random_pic)
        await ctx.send(file = pic)
    #抽籤/URL
    @commands.command()
    async def omikuji(self,ctx):
        with open("cmds\data\omikuji.json","r",encoding="utf8") as omikuji_file:
            omikuji = json.load(omikuji_file)
            cache = omikuji["userdata"]
            # guild = ctx.guild
            # channel = ctx.channel
            user = ctx.author.id
            #如果抽過了就回傳抽出結果
            if user in omikuji["userdata"]:
                await ctx.send(f"[User :]({omikuji[f"{int(user)}"]}) <@{user}>\n你今天已經抽過了啦!")
            #沒抽過就抽出結果後更新資料進"omikuji.json"
            else:
                random_pic = random.choice(setting["Omikuji"])
                await ctx.send("抽出的結果是!!!!\n(搖籤筒聲)")
                await asyncio.sleep (3)
                await ctx.send(f"[User :]({random_pic}) <@{user}>\n抽出抽出結果了!!快看快看!!!")
                #資料更新
                cache.append (user)
                omikuji_update = {"userdata":cache,f"{user}":random_pic}
                omikuji.update(omikuji_update)
                with open("cmds\data\omikuji.json","w",encoding="utf8") as omikuji_file:
                    json.dump(omikuji,omikuji_file)
    #取得用戶ID
    @commands.command()
    async def myid(self,ctx):
        id = ctx.author.id
        await ctx.send(f'User：<@{id}>的ID是{id}呦!')




# {
#     "userdata":[697842681082281985],
#     "697842681082281985":"https://www.illust-box.jp/db_img/sozai/00019/196972/watermark.jpg"
# }


















async def setup(bot):
    await bot.add_cog(React(bot))