import discord
from discord.ext import commands
from core.classes import Cog_extension

import json
with open("setting.json","r",encoding="utf8") as setting_file:
    setting = json.load(setting_file)
import datetime ,random

class Main(Cog_extension):
        
    @commands.command()
    async def ping(self, ctx):      #延遲
        await ctx.send(f"{round(self.bot.latency)}/s\n"  f"{round(((self.bot.latency)-round(self.bot.latency))*1000)}/ms"),
    
    @commands.command()
        #, timestamp=datetime.datetime.now()
    async def p(self, ctx):
        embed=discord.Embed(title="**__請按照規則領取身份__**", url="https://discord.com/channels/1219180207534243891/1219815148622057523", description="** **", color=0xaa095f, timestamp=datetime.datetime.now())
        embed.set_author(name="Azumari : ", url="https://github.com/nekohasuki/azunya/blob/main/azunya.py")
        embed.set_thumbnail(url= random.choice(setting["ROLE_MESSAGE_Thumbnail"]))
        embed.add_field(name="**現界[**一**]** - @普通平民老百姓", value="介紹：普通人\n\n條件：底下:free:按鈕領取\n\n** **", inline=True)
        embed.add_field(name="**現界[**二**]** - @平民老百姓", value="介紹：有錢\n　　　但還是普通人\n條件：現界一級並至少■■■■\n(條件未開放)\n\n** **", inline=True)
        embed.add_field(name="", value=" ", inline=False)
        embed.add_field(name="**現界[**三**]** - @老百姓", value="介紹：有錢有閒\n　　　但依然還是普通人\n條件：獲得現界二級並至少■■■■\n(條件未開放)\n\n** **", inline=True)
        embed.add_field(name="**現界[**四**]** - @百姓", value="介紹：有錢有閒有權\n　　　即使如此卻依舊還是普通人\n條件：獲得現界三級並至少■■■■\n(條件未開放)\n\n** **", inline=True)
        embed.add_field(name="", value=" ", inline=False)
        embed.add_field(name="**特殊現界** - @永遠17的", value="介紹：感覺18太老了所以是17www\n　　　(可以聊些有的沒的www)\n條件：請出示成年的證明\n\n** **", inline=False)
        embed.add_field(name="**血族** - @赫", value='介紹：館館&偷摸她雞\n　　　(可繞"@永遠17的&@百姓"之條件享受權力)\n條件：請先預約並於休息室(#會客室 )等候審核與評估\n\n** **', inline=False)
        embed.add_field(name="**特殊身份(特殊狀況可取):**", value="\n@歌姬\n@不能說的秘密\n@無身份", inline=False)
        embed.add_field(name="", value=" ", inline=False)
        embed.add_field(name="", value=" ", inline=False)
        embed.add_field(name="", value=" ", inline=False)
        embed.set_image(url= random.choice(setting["ROLE_MESSAGE_IMEGE"]))
        embed.set_footer(text= "Copyright ⑨ 2024 N..S ")
        await ctx.send(embed=embed)































async def setup(bot):
    await bot.add_cog(Main(bot))