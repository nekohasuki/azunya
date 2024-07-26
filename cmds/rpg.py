import discord
from discord.ext import commands
from discord import app_commands,SelectOption
from discord.ui import Button,View,Select
#Dynamic,Item,Modal,Text_input
open_file='''
with open('setting.json','r',encoding='utf-8') as setting_file:
    setting = json.load(setting_file)
with open('cmds/data/user_data.json' , 'r' , encoding='utf-8') as userdata_file:
    userdata = json.load(userdata_file)
with open('cmds/rpg_define/format.json','r',encoding='utf-8') as Format_file:
    format = json.load(Format_file)
'''

from core.classes import Cog_extension

import asyncio,datetime,json,os,random
from PIL import Image

prefix = 'rpg-'
Test_mod = True
#      True or False

if Test_mod == True:
    class Config:
        class setting:
            class language(Select):
                def __init__(self):
                    options=[]
                    for language in os.listdir('cmds/rpg_define'):
                        if language.endswith('lang'):
                            with open(f'cmds/rpg_define/{language}','r',encoding='utf-8') as Lang_file:
                                for line in Lang_file:
                                    if line.strip().startswith('language-Type'):
                                        lang = line.split('=', 1)[1].strip()
                                        break
                                    else:lang=None
                                if lang != None:
                                    options.append(SelectOption(label=lang,value=language[:-5]))
                    super().__init__(placeholder='選擇語言', options=options)
                async def callback(self, interaction: discord.Interaction):
                    await interaction.response.edit_message(content=f'你選擇了: {self.values[0]}',view=Config.first_online.language.subsequent())


            @staticmethod
            def create_back_button():
                return Button(label='返回', style=discord.ButtonStyle.red)
            @staticmethod
            def create_decide_button():
                return Button(label='決定', style=discord.ButtonStyle.green)
        class first_online:
            class language(View):
                def __init__(self, with_decide=False):
                    super().__init__(timeout=None)
                    self.add_item(Config.setting.language())
                    
                    if with_decide:
                        decide_button = Config.setting.create_decide_button()
                        decide_button.callback = self.decided_callback
                        self.add_item(decide_button)
                    back_button = Config.setting.create_back_button()
                    back_button.callback = self.back_callback
                    self.add_item(back_button)
                async def decided_callback(self, interaction: discord.Interaction):
                    await interaction.response.edit_message(content='決定已確認。', view=None)
                async def back_callback(self, interaction: discord.Interaction):
                    await interaction.response.edit_message(delete_after=0)
                @staticmethod
                def first():
                    return Config.first_online.language(with_decide=False)
                @staticmethod
                def subsequent():
                    return Config.first_online.language(with_decide=True)






        # class first_online:
        #     class language:
        #         class first(View):
        #             def __init__(self):
        #                 super().__init__(timeout=None)
        #                 self.add_item(Config.setting.language())
        #                 back= Button(label='back',style=discord.ButtonStyle.red)
        #                 back.callback = self.back_callback
        #                 self.add_item(back)
        #             async def back_callback(self,interaction:discord.Interaction):
        #                     await interaction.response.edit_message(delete_after=0)
        #         class subsequent(View):
        #             def __init__(self):
        #                 super().__init__(timeout=None)
        #                 self.add_item(Config.first_online.language.first())
        #                 decided = Button(label='decided',style=discord.ButtonStyle.green)
        #                 decided.callback = self.decided_callback
        #                 self.add_item(decided)
        #             async def decided_callback(self,interaction:discord.Interaction):
        #                     await interaction.response.edit_message(delete_after=0)

    class RPG(Cog_extension):
        commandname = f'{prefix}interface'
        @app_commands.command(name=commandname, description='叫出介面')
        async def interface(self, interaction: discord.Interaction):
            await interaction.response.send_message(view=Config.first_online.language.first())
            
    async def setup(bot):
        await bot.add_cog(RPG(bot))
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
elif Test_mod == False:
    User=[]
    Lang=[]
    class Config:
        class first_online:


            class name(View):
                def __init__(self):
                    super().__init__(timeout=None)
                    language = Button(label='language_Sheet')
                    language.callback = self.language_callback
                    self.add_item(language)
                async def language_callback(self,interaction:discord.Interaction):
                    await interaction.response.edit_message(content='# 種族',view=Config.first_online.Race())
            
            class color(View):
                def __init__(self):
                    super().__init__(timeout=None)
                    decided = Button(label='decided',style=discord.ButtonStyle.green)
                    decided.callback = self.decided_callback
                    self.add_item(decided)

                    random_color = Button(label='random_color')
                    random_color.callback = self.random_color_callback
                    self.add_item(random_color)

                    back = Button(label='返回',style=discord.ButtonStyle.red)
                    back.callback = self.back_callback
                    self.add_item(back)
                async def decided_callback(self,interaction:discord.Interaction):
                    await interaction.response.edit_message(attachments=[],embed=None,view=Config.Start_Screen())

                async def random_color_callback(self,interaction:discord.Interaction):
                    start = datetime.datetime.now().strftime('(int("%H")*3600)+(int("%M")*60)+int("%S")+float(int(str("%f")[:3])/1000)')
                    directory = r'imege\rpg\color'
                    os.makedirs(directory,exist_ok=True)
                    width = 192
                    height = 108
                    R = random.randint(0x80,0xff)
                    G = random.randint(0x80,0xff)
                    B = random.randint(0x80,0xff)
                    file_path = os.path.join(directory,f'0x{R:02x}{G:02x}{B:02x}.png')

                    if not os.path.exists(file_path):
                        image = Image.new('RGB',(width,height),(R,G,B))
                        image.save(file_path,format='PNG')
                        print(f'User:{interaction.user.display_name} adding 0x{R:02x}{G:02x}{B:02x}.png')
                    user_color = f'0x{R:02x}{G:02x}{B:02x}'
                    file_path = f'imege/rpg/color/{user_color}.png'
                    # while not os.path.isfile(file_path):
                    #     await asyncio.sleep(1)

                    end = datetime.datetime.now().strftime('(int("%H")*3600)+(int("%M")*60)+int("%S")+float(int(str("%f")[:3])/1000)')
                    h,r = divmod(int(eval(end)-eval(start)),3600)
                    m,s = divmod(r,60)
                    ms = str(int((eval(end)-eval(start)-int(eval(end)-eval(start)))*1000)).zfill(3)
                    delay = []
                    if (h or m) != 0:
                        delay.append(f'{str(h).zfill(2)}:{str(m).zfill(2)}\n')
                    delay.append(f'{s}.{ms}/s')
                    delay = ''.join(delay)

                    file = discord.File(file_path,filename=f'{user_color}.png')
                    embed = discord.Embed(description=f'# <:LOGO1:1221378614524641332>__{'random_color'}__',colour=int(user_color,16),timestamp=datetime.datetime.now())
                    embed.add_field(name='',value=f'**耗時 :**\n> `{delay}`\n\n**顏色 :**\n> RGB  `{str(R).zfill(3)} , {str(G).zfill(3)} , {str(B).zfill(3)}`\n> HEX `#{str(user_color)[2:]}`',inline=False)
                    embed.set_image(url=f'attachment://{user_color}.png')
                    await interaction.response.edit_message(attachments=[file],embed=embed,view=Config.first_online.color())
                    
                async def back_callback(self,interaction:discord.Interaction):
                    await interaction.response.edit_message(attachments=[],embed=None,view=Config.Start_Screen())
            
            class Race():
                pass
            
            class Main_profession():
                pass

        class Start_Screen(View):
            def __init__(self):
                super().__init__(timeout=None)
                Character_Sheet = Button(label='Character_Sheet')
                Character_Sheet.callback = self.Character_Sheet_callback
                self.add_item(Character_Sheet)

                test = Button(label='test',row=4)
                test.callback = self.test_callback
                self.add_item(test)
            async def Character_Sheet_callback(self,interaction:discord.Interaction):
                user = interaction.user.id
                if user == int(697842681082281985):
                    user = 938100109240074310
                variable={}
                exec(open_file,globals(),variable)
                userdata=variable.get('userdata')
                format=variable.get('format')
                display_name=userdata[f'{user}']['display_name']
                RPG = userdata[f'{user}']['RPG']
                lang=format[user['RPG']['language']]['additional']
                with open(f'cmds/rpg_define/{user['RPG']['language']}.lang','r',encoding='utf-8') as Lang_file:
                    for line in Lang_file:
                        line = line.strip()
                        if not line or line.startswith('#'):
                            continue
                        key, value = line.split('=', 1)
                        if value in format[user['RPG']['language']][lang]:
                            pass
                            lang[key] = format[user['RPG']['language']][lang][value]
                        else:
                            lang[key] = f'"{value}"'










                if '此處用於找出等級最高的副職業' != 1:
                    top_sub_profession = []
                    maxlave = []
                    for sub_profession_1 in RPG['Sub_profession']:
                        maxlave.append(RPG['Sub_profession'][sub_profession_1])
                        for sub_profession_2 in RPG['Sub_profession']:
                            if min(maxlave) != max(maxlave):
                                maxlave.remove(min(maxlave))
                            if RPG['Sub_profession'][sub_profession_1] > RPG['Sub_profession'][sub_profession_2]:
                                if {sub_profession_1:RPG['Sub_profession'][sub_profession_1]} not in top_sub_profession:
                                    top_sub_profession.append({sub_profession_1:RPG['Sub_profession'][sub_profession_1]})
                                if {sub_profession_2:RPG['Sub_profession'][sub_profession_2]}  in top_sub_profession:
                                    top_sub_profession.remove({sub_profession_2:RPG['Sub_profession'][sub_profession_2]})
                    if top_sub_profession == []:
                        top_sub_profession.append({'full_equilibrium':RPG['Sub_profession'][sub_profession_1]})
                    else:
                        random.shuffle(top_sub_profession)
                        maxlave = len(maxlave)-1
                    top_sub_profession = top_sub_profession[0]
                    if maxlave != 0:
                        top_sub_profession = {'class':f'{eval(lang[list(top_sub_profession.keys())[0]])}`+{maxlave}`','level':list(top_sub_profession.values())[0]}
                    else:
                        top_sub_profession = {'class':f'{eval(lang[list(top_sub_profession.keys())[0]])}','level':list(top_sub_profession.values())[0]}
                user_EXP = {'max':RPG['EXP']['max'],'now':RPG['EXP']['now']}
                EXP_bar=(f'{'/|'*int(15/user_EXP['max']*(user_EXP['now']))}{'.:'*(15-int(15/user_EXP['max']*(user_EXP['now'])))}')
                user_main_profession = {'class':lang[RPG['Main_profession']['class']],'level':RPG['Main_profession']['level']}
            
                embed = discord.Embed(description=f'# <:LOGO1:1221378614524641332>__{eval(lang['character_sheet'])}__',colour=int(RPG['color'],16),timestamp=datetime.datetime.now())
                embed.add_field(name='',value=f'{eval(lang['name'])}: **{display_name}**\n{eval(lang['profession'])}: {eval(user_main_profession['class']):<5}Lv.{user_main_profession['level']:<3}{'/':<2}{top_sub_profession['class']:<5}Lv.{top_sub_profession['level']:<3}\n{eval(lang['Race'])}: {eval(lang[RPG['Race']])}\n{eval(lang['EXP'])}: {user_EXP['now']} / {user_EXP['max']}\n`{EXP_bar}`',inline=False)
                embed.add_field(name='__**-------------------------------------**__',value=(f'**|**|!__**H~P**__!| :_`{200:>4}`_\u3000|!__**S!A!N**__!| :_`{0:>4}`_\u3000\n**|**|!__**S~P**__!| :_`{0:>4}`_\u3000|!__**M~P**__!| :_`{0:>4}`_\u3000\n**|**|!__**A!T!K**__!| :_`{0:>4}`_\u3000|!__**MATK**__!| :_`{0:>4}`_\u3000\n**|**|!__**D!E!F**__!| :_`{0:>4}`_\u3000|!__**MDEF**__!| :_`{0:>4}`_\u3000\n**|**|!__**L!U!K**__!| :_`{0:>4}`_\u3000|!__**S!P!D**__!| :_`{0:>4}`_\u3000\n**|**|!__**A!G!\u200BI\u2009**__!| :_`{0:>4}`_\u3000|!__**C!H!R**__!| :_`{0:>4}`_\u3000').replace('~','\u2009\u3000').replace('!','\u200A\u2004').replace(' ','\u2007\u200A'),inline=False)
                await interaction.response.edit_message(embed=embed,view=Config.Character_Sheet())
             
            async def test_callback(self,interaction:discord.Interaction):
                print('pass')
                # await interaction.response.edit_message(content=(f'```{first_online_time}\n{datetime.datetime.now()}```\n{language}'))

        class Character_Sheet(View):
            def __init__(self):
                super().__init__(timeout=None)
                main_profession =Button(label='主職業')
                main_profession.callback = self.main_profession_callback
                self.add_item(main_profession)
                sub_profession =Button(label='副職業')
                sub_profession.callback = self.sub_profession_callback
                self.add_item(sub_profession)
                attributes =Button(label='屬性')
                attributes.callback = self.attributes_callback
                self.add_item(attributes)
                back = Button(label='返回',style=discord.ButtonStyle.red)
                back.callback = self.back_callback
                self.add_item(back)
            async def main_profession_callback(self,interaction:discord.Interaction):
                await interaction.response.edit_message(content=f'主職業')
            async def sub_profession_callback(self,interaction:discord.Interaction):
                await interaction.response.edit_message(content=f'副職業')
            async def attributes_callback(self,interaction:discord.Interaction):
                await interaction.response.edit_message(content=f'屬性')
            async def back_callback(self,interaction:discord.Interaction):
                await interaction.response.edit_message(content='',embed=None,view=Config.Start_Screen())

        class name(View):
            def __init__(self):
                super().__init__(timeout=None)
                back = Button(label='返回',style=discord.ButtonStyle.red)
                back.callback = self.back_callback
                self.add_item(back)
            async def back_callback(self,interaction:discord.Interaction):
                await interaction.response.edit_message('',view=Config.Start_Screen())

            def __init__(self):
                super().__init__(timeout=None)
                back = Button(label='返回',style=discord.ButtonStyle.red)
                back.callback = self.back_callback
                self.add_item(back)
            async def back_callback(self,interaction:discord.Interaction):
                await interaction.response.edit_message('',view=Config.Start_Screen())



        class test:
            class A(View):
                class Route_A(View):
                    def __init__(self):
                        super().__init__(timeout=None)
                        A1 = Button(label='A1')
                        A1.callback = self.A1_callback
                        self.add_item(A1)
                        A2 = Button(label='A2')
                        A2.callback = self.A2_callback
                        self.add_item(A2)
                        back = Button(label='返回',style=discord.ButtonStyle.red)
                        back.callback = self.back_callback
                        self.add_item(back)
                    async def A1_callback(self,interaction:discord.Interaction):
                        if interaction.user == interaction.message.interaction.user:
                            embed = discord.Embed(title='結果',description=f'雖然 {interaction.user.mention} 選擇了 A1，但還是會回到 B，因為這就是命運石之門的選擇。',color=discord.Color.purple(),timestamp=datetime.datetime.now())
                            await interaction.response.edit_message(embed=embed,view=Config.test.A())
                        else:
                            await interaction.response.send_message(f'這不是你的選項。',ephemeral=True)
                    async def A2_callback(self,interaction:discord.Interaction):
                        if interaction.user == interaction.message.interaction.user:
                            embed = discord.Embed(title='結果',description=f'雖然 {interaction.user.mention} 選擇了 A2，但還是會回到 B，因為這就是命運石之門的選擇。',color=discord.Color.purple(),timestamp=datetime.datetime.now())
                            await interaction.response.edit_message(embed=embed,view=Config.test.A())
                        else:
                            await interaction.response.send_message(f'這不是你的選項。',ephemeral=True)
                    async def back_callback(self,interaction:discord.Interaction):
                        if interaction.user == interaction.message.interaction.user:
                            embed = discord.Embed(title='請選擇',description=f'您好{interaction.user.mention}，請選擇 A 或 B',color=discord.Color.purple(),timestamp=datetime.datetime.now())
                            await interaction.response.edit_message(embed=embed,view=Config.test.A())
                        else:
                            await interaction.response.send_message(f'這不是你的選項。',ephemeral=True)
                def __init__(self):
                    super().__init__(timeout=None)
                    A = Button(label='A')
                    A.callback = self.A_callback
                    self.add_item(A)
                    B = Button(label='B')
                    B.callback = self.B_callback
                    self.add_item(B)
                async def A_callback(self,interaction:discord.Interaction):
                    if interaction.user == interaction.message.interaction.user:
                        embed = discord.Embed(title='請選擇',description=f'{interaction.user.mention}，請選擇 1 或 2',color=discord.Color.purple(),timestamp=datetime.datetime.now())
                        await interaction.response.edit_message(embed=embed,view=Config.test.A.Route_A())
                    else:
                        await interaction.response.send_message(f'這不是你的選項。',ephemeral=True)
                async def B_callback(self,interaction:discord.Interaction):
                    if interaction.user == interaction.message.interaction.user:
                        embed = discord.Embed(title='結果',description=f'選了B的你\n命運終究是沒辦法跳出的。',color=discord.Color.purple(),timestamp=datetime.datetime.now())
                        await interaction.response.edit_message(embed=embed,view=Config.test.A())
                    else:
                        await interaction.response.send_message(f'這不是你的選項。',ephemeral=True)
            class B(View):
                class Route_A(View):
                    def __init__(self):
                        super().__init__(timeout=None)
                        A1 = Button(label='A1')
                        A1.callback = self.A1_callback
                        self.add_item(A1)
                        A2 = Button(label='A2')
                        A2.callback = self.A2_callback
                        self.add_item(A2)
                        back = Button(label='返回',style=discord.ButtonStyle.red)
                        back.callback = self.back_callback
                        self.add_item(back)
                    async def A1_callback(self,interaction:discord.Interaction):
                        embed = discord.Embed(title='結果',description=f'雖然 {interaction.user.mention} 選擇了 A1，但還是會回到 B，因為這就是命運石之門的選擇。',color=discord.Color.purple(),timestamp=datetime.datetime.now())
                        await interaction.response.edit_message(embed=embed,view=Config.test.B())
                    async def A2_callback(self,interaction:discord.Interaction):
                        embed = discord.Embed(title='結果',description=f'雖然 {interaction.user.mention} 選擇了 A2，但還是會回到 B，因為這就是命運石之門的選擇。',color=discord.Color.purple(),timestamp=datetime.datetime.now())
                        await interaction.response.edit_message(embed=embed,view=Config.test.B())
                    async def back_callback(self,interaction:discord.Interaction):
                        embed = discord.Embed(title='請選擇',description=f'您好{interaction.user.mention}，請選擇 A 或 B',color=discord.Color.purple(),timestamp=datetime.datetime.now())
                        await interaction.response.edit_message(embed=embed,view=Config.test.B())
                def __init__(self):
                    super().__init__(timeout=None)
                    A = Button(label='A')
                    A.callback = self.A_callback
                    self.add_item(A)
                    B = Button(label='B')
                    B.callback = self.B_callback
                    self.add_item(B)
                async def A_callback(self,interaction:discord.Interaction):
                    embed = discord.Embed(title='請選擇',description=f'{interaction.user.mention}，請選擇 1 或 2',color=discord.Color.purple(),timestamp=datetime.datetime.now())
                    await interaction.response.edit_message(embed=embed,view=Config.test.B.Route_A())
                async def B_callback(self,interaction:discord.Interaction):
                    embed = discord.Embed(title='結果',description=f'選了B的你\n命運終究是沒辦法跳出的。',color=discord.Color.purple(),timestamp=datetime.datetime.now())
                    await interaction.response.edit_message(embed=embed,view=Config.test.B())
            class name(View):
                def __init__(self):
                    super().__init__(timeout=None)
                    random_color = Button(label='random_color')
                    random_color.callback = self.random_color_callback
                    self.add_item(random_color)
                async def random_color_callback(self,interaction:discord.Interaction):
                    directory = r'imege\rpg\color'
                    os.makedirs(directory,exist_ok=True)
                    width = 192
                    height = 108
                    R = (int(user_color,16) >> 16) & 0xff
                    G = (int(user_color,16) >> 8) & 0xff
                    B = int(user_color,16) & 0xff
                    file_path = os.path.join(directory,f'{str(user_color)}.png')
                    
                    if not os.path.exists(file_path):
                        image = Image.new('RGB',(width,height),(R,G,B))
                        image.save(file_path,format='PNG')
                    file_path = f'imege/rpg/color/{user_color}.png'
                    file = discord.File(file_path,filename=f'{user_color}.png')
                    embed = discord.Embed(description=f'# <:LOGO1:1221378614524641332>__{'random_color'}__',colour=int(user_color,16),timestamp=datetime.datetime.now())
                    embed.add_field(name='',value=f'**顏色 :**\n> RGB  `{str(R).zfill(3)},{str(G).zfill(3)},{str(B).zfill(3)}`\n> HEX `#{user_color}`',inline=False)
                    embed.set_image(url=f'attachment://{user_color}.png')
                    await interaction.response.edit_message(attachments=[file],embed=embed,view=Config.first_online.color())
    class RPG(Cog_extension):
        commandname = (f'{prefix}interface')
        @app_commands.command(name = commandname,description = '叫出介面')
        async def interface(self,interaction:discord.Interaction):
            test = 'No'
            #A or B or No
            if test =='No':
                variable={}
                exec(open_file,globals(),variable)
                userdata=variable.get('userdata')
                setting=variable.get('setting')
                user = interaction.user.id
                if user == int('697842681082281985'):
                    user = 938100109240074310
                if "RPG" not in userdata[str(user)]:
                    await interaction.response.send_message(f'User:<@{user}>你的資料不知道為何但就是不完整\n請你先到[__領取身分的地方__](https://ptb.discord.com/channels/{interaction.guild.id}/{setting['ROLE_MESSAGE_CHANNEL_ID']}/{setting['ROLE_MESSAGE_ID']})重新領取身分\n如果還是不行請通知管理員',ephemeral=True)
                elif userdata[str(user)]['RPG'] != {'1'}:
                    for list in User:
                        User.remove(list)
                    User.append(interaction.user.id)
                    await interaction.response.send_message(view=Config.first_online.language.choice())
                else:
                    await interaction.response.send_message(view=Config.Start_Screen())
           
           
           
           
            else:
                embed = discord.Embed(title='請選擇',description=f'您好{interaction.user.mention}，請選擇 A 或 B',color=discord.Color.purple(),timestamp=datetime.datetime.now())
                if test == 'A':
                    await interaction.response.send_message(embed=embed,view=Config.test.A())
                if test == 'B':
                    await interaction.response.send_message(embed=embed,view=Config.test.B())
            
    async def setup(bot):
        await bot.add_cog(RPG(bot))

