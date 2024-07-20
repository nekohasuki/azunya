import discord
from discord.ext import commands
from discord import app_commands
from discord.ui import Button, View

from core.classes import Cog_extension

import asyncio,datetime,json,os,random
from PIL import Image

prefix = 'rpg-'
Test_mod = True
#      True or False


# /////////////////////////////////////////////////////////////////////////////////////////////////////////////
if '此處用於測試時代替真實玩家資料':
    data={
        "123": {
            "name": "nekoha__suki",
            "display_name": "\u8c93\u7fbd\uff08\u516c\u4e8b\u5e33\uff09",
            "global_name": "nekoha__suki",
            "RPG":{
                "language":"zh_TW",
                "first_online_time":"2024-00-00 00:00:00.00000000",
                "color":"0x000000",
                "coins":0,
                "Race":"MoonRabbit",
                "EXP":{
                    "now":0,
                    "max":10
                },
                "Main_profession":{
                    "class":"Thief",
                    "level":0
                },
                "Sub_profession":{
                    "Merchant":0,
                    "Pharmacist":0,
                    "Jeweler":0,
                    "Floriculturist":1,
                    "Chef":0,
                    "Armourer":0,
                    "Hammersmith":0
                },
                "attributes":{
                    "HP":0,
                    "SP":0,
                    "MP":0,
                    "ATK":0,
                    "MATK":0,
                    "DEF":0,
                    "MDEF":0,
                    "SPD":0,
                    "AGI":0,
                    "LUK":0,
                    "CHR":0,
                    "SAN":0
                },
                "item":{
                    "Weapon":["Claw"],
                    "Weapon_II":[""],
                    "Weapon_III":[""],
                    "Armor":["Leather_armor"],
                    "Runes":[],
                    "Flowers":[],
                    "Gemstones":[],
                    "Cuisine":[]
                    },
                "handbook":{
                    "Weapon":["Claw"],
                    "Weapon_II":[""],
            
                    "Weapon_III":[""],
                    "Armor":["Leather_armor"],
                    "Runes":[],
                    "Flowers":[],
                    "Gemstones":[],
                    "Cuisine":[],
                    "Hostile":[]
                },
                "PVP":{
                    "win":0,
                    "lose":0,
                    "tie":0
                }
            }
        }
    }
    user = data['123']

first_online_time=user['RPG']['first_online_time']
language=user['RPG']['language']
Race = user['RPG']['Race']
EXP=user['RPG']['EXP']
main_profession = user['RPG']['Main_profession']
sub_professions = user['RPG']['Sub_profession']
user_color = user['RPG']['color']

EXP_bar=['/|','/|','/|','/|','/|','.:','.:','.:','.:','.:','.:','.:','.:','.:','.:']
Character_Sheet = '角色卡'
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////


if Test_mod == True:
    class Button_config:
        class first_online():
            class language():
                pass
            class name():
                pass
            class color(View):
                def __init__(self):
                    super().__init__(timeout=None)
                    decided_button = Button(label='decided',style=discord.ButtonStyle.green)
                    decided_button.callback = self.decided_button_callback
                    self.add_item(decided_button)

                    random_color_button = Button(label='random_color')
                    random_color_button.callback = self.random_color_button_callback
                    self.add_item(random_color_button)

                    back_button = Button(label='返回',style=discord.ButtonStyle.red)
                    back_button.callback = self.back_button_callback
                    self.add_item(back_button)
                async def decided_button_callback(self,interaction:discord.Interaction):
                    await interaction.response.edit_message(attachments=[],embed=None,view=Button_config.Start_Screen())

                async def random_color_button_callback(self,interaction:discord.Interaction):
                    start = datetime.datetime.now().strftime('(int("%H")*3600)+(int("%M")*60)+int("%S")+float(int(str("%f")[:3])/1000)')
                    directory = r'imege\rpg\color'
                    os.makedirs(directory, exist_ok=True)
                    width = 192
                    height = 108
                    R = random.randint(0x80,0xff)
                    G = random.randint(0x80,0xff)
                    B = random.randint(0x80,0xff)
                    file_path = os.path.join(directory, f'0x{R:02x}{G:02x}{B:02x}.png')

                    if not os.path.exists(file_path):
                        image = Image.new('RGB', (width, height), (R, G, B))
                        image.save(file_path, format='PNG')
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

                    file = discord.File(file_path, filename=f'{user_color}.png')
                    embed = discord.Embed(description=f'# <:LOGO1:1221378614524641332>__{'random_color'}__',colour=int(user_color,16),timestamp=datetime.datetime.now())
                    embed.add_field(name='',value=f'**耗時 :**\n> `{delay}`\n\n**顏色 :**\n> RGB  `{str(R).zfill(3)} , {str(G).zfill(3)} , {str(B).zfill(3)}`\n> HEX `#{str(user_color)[2:]}`',inline=False)
                    embed.set_image(url=f'attachment://{user_color}.png')
                    await interaction.response.edit_message(attachments=[file],embed=embed,view=Button_config.first_online.color())
                    
                async def back_button_callback(self,interaction:discord.Interaction):
                    await interaction.response.edit_message(attachments=[],embed=None,view=Button_config.Start_Screen())
            
            class Race():
                pass
            class Main_profession():
                pass

        class Start_Screen(View):
            def __init__(self):
                super().__init__(timeout=None)
                Character_Sheet_button = Button(label=Character_Sheet)
                Character_Sheet_button.callback = self.Character_Sheet_button_callback
                self.add_item(Character_Sheet_button)

                test_button = Button(label='test',row=4)
                test_button.callback = self.test_button_callback
                self.add_item(test_button)
            async def Character_Sheet_button_callback(self,interaction:discord.Interaction):
                if '此處用於找出等級最高的副職業' != 1:
                    top_sub_profession = []
                    for sub_profession in sub_professions:
                        for sub_profession_2 in sub_professions:
                            if sub_professions[sub_profession] > sub_professions[sub_profession_2]:
                                if {f'{sub_profession}':sub_professions[sub_profession]} not in top_sub_profession:
                                    top_sub_profession.append({f'{sub_profession}':sub_professions[sub_profession]})
                                if {f'{sub_profession_2}':sub_professions[sub_profession]} in top_sub_profession:
                                    top_sub_profession.remove({f'{sub_profession_2}':sub_professions[sub_profession]})
                    if top_sub_profession ==[]:
                        top_sub_profession.append({f'全均衡':sub_professions[sub_profession]})
                    else:
                        random.shuffle(top_sub_profession)
                    top_sub_profession = top_sub_profession[0]
                    top_sub_profession = {"class":list(top_sub_profession.keys())[0],"level":top_sub_profession[list(top_sub_profession.keys())[0]]}
                embed = discord.Embed(description=f'# <:LOGO1:1221378614524641332>__{Character_Sheet}__',colour=int(user_color,16),timestamp=datetime.datetime.now())
                embed.add_field(name='',value=f'{'名稱':<3}: **{interaction.user.display_name}**\n{'職業':<3}: {main_profession['class']:<5}Lv.{main_profession['level']:<3}{'/':<2}{top_sub_profession['class']:<4}Lv.{top_sub_profession['level']:<5}\n{'種族':<3}: {Race}\n{'EXP':<4}: {EXP['now']} / {EXP['max']}\n`{str(EXP_bar)[1:-1].replace(',','').replace(' ','').replace("'",'')}`',inline=False)
                embed.add_field(name='__**-------------------------------------**__',value=(f'|!__**H~P**__!| :_`{200:>4}`_\u3000|!__**S!A!N**__!| :_`{0:>4}`_\u3000\n|!__**S~P**__!| :_`{0:>4}`_\u3000|!__**M~P**__!| :_`{0:>4}`_\u3000\n|!__**A!T!K**__!| :_`{0:>4}`_\u3000|!__**MATK**__!| :_`{0:>4}`_\u3000\n|!__**D!E!F**__!| :_`{0:>4}`_\u3000|!__**MDEF**__!| :_`{0:>4}`_\u3000\n|!__**L!U!K**__!| :_`{0:>4}`_\u3000|!__**S!P!D**__!| :_`{0:>4}`_\u3000\n|!__**A!G!\u200BI\u2009**__!| :_`{0:>4}`_\u3000|!__**C!H!R**__!| :_`{0:>4}`_\u3000').replace('~','\u2009\u3000').replace('!','\u200A\u2004').replace(' ','\u2007\u200A'),inline=False)
                await interaction.response.edit_message(embed=embed,view=Button_config.Character_Sheet())
             
            async def test_button_callback(self,interaction:discord.Interaction):
                await interaction.response.edit_message(content=(f'```{first_online_time}\n{datetime.datetime.now()}```\n{language}'))
        

              
        class Character_Sheet(View):
            def __init__(self):
                super().__init__(timeout=None)
                main_profession_button =Button(label='主職業')
                main_profession_button.callback = self.main_profession_button_callback
                self.add_item(main_profession_button)
                sub_profession_button =Button(label='副職業')
                sub_profession_button.callback = self.sub_profession_button_callback
                self.add_item(sub_profession_button)
                attributes_button =Button(label='屬性')
                attributes_button.callback = self.attributes_button_callback
                self.add_item(attributes_button)
                back_button = Button(label='返回',style=discord.ButtonStyle.red)
                back_button.callback = self.back_button_callback
                self.add_item(back_button)
            async def main_profession_button_callback(self,interaction:discord.Interaction):
                await interaction.response.edit_message(content=f'主職業')
            async def sub_profession_button_callback(self,interaction:discord.Interaction):
                await interaction.response.edit_message(content=f'副職業')
            async def attributes_button_callback(self,interaction:discord.Interaction):
                await interaction.response.edit_message(content=f'屬性')
            async def back_button_callback(self,interaction:discord.Interaction):
                await interaction.response.edit_message(content='',embed=None,view=Button_config.Start_Screen())

        class name(View):
            def __init__(self):
                super().__init__(timeout=None)
                back_button = Button(label='返回',style=discord.ButtonStyle.red)
                back_button.callback = self.back_button_callback
                self.add_item(back_button)
            async def back_button_callback(self,interaction:discord.Interaction):
                await interaction.response.edit_message('',view=Button_config.Start_Screen())

            def __init__(self):
                super().__init__(timeout=None)
                back_button = Button(label='返回',style=discord.ButtonStyle.red)
                back_button.callback = self.back_button_callback
                self.add_item(back_button)
            async def back_button_callback(self,interaction:discord.Interaction):
                await interaction.response.edit_message('',view=Button_config.Start_Screen())

        class test:
            class A(View):
                class Route_A(View):
                    def __init__(self):
                        super().__init__(timeout=None)
                        A1_button = Button(label='A1')
                        A1_button.callback = self.A1_button_callback
                        self.add_item(A1_button)
                        A2_button = Button(label='A2')
                        A2_button.callback = self.A2_button_callback
                        self.add_item(A2_button)
                        back_button = Button(label='返回',style=discord.ButtonStyle.red)
                        back_button.callback = self.back_button_callback
                        self.add_item(back_button)
                    async def A1_button_callback(self,interaction:discord.Interaction):
                        if interaction.user == interaction.message.interaction.user:
                            embed = discord.Embed(title='結果',description=f'雖然 {interaction.user.mention} 選擇了 A1，但還是會回到 B，因為這就是命運石之門的選擇。',color=discord.Color.purple(),timestamp=datetime.datetime.now())
                            await interaction.response.edit_message(embed=embed,view=Button_config.test.A())
                        else:
                            await interaction.response.send_message(f'這不是你的選項。',ephemeral=True)
                    async def A2_button_callback(self,interaction:discord.Interaction):
                        if interaction.user == interaction.message.interaction.user:
                            embed = discord.Embed(title='結果',description=f'雖然 {interaction.user.mention} 選擇了 A2，但還是會回到 B，因為這就是命運石之門的選擇。',color=discord.Color.purple(),timestamp=datetime.datetime.now())
                            await interaction.response.edit_message(embed=embed,view=Button_config.test.A())
                        else:
                            await interaction.response.send_message(f'這不是你的選項。',ephemeral=True)
                    async def back_button_callback(self,interaction:discord.Interaction):
                        if interaction.user == interaction.message.interaction.user:
                            embed = discord.Embed(title='請選擇',description=f'您好{interaction.user.mention}，請選擇 A 或 B',color=discord.Color.purple(),timestamp=datetime.datetime.now())
                            await interaction.response.edit_message(embed=embed,view=Button_config.test.A())
                        else:
                            await interaction.response.send_message(f'這不是你的選項。',ephemeral=True)
                def __init__(self):
                    super().__init__(timeout=None)
                    A_button = Button(label='A')
                    A_button.callback = self.A_button_callback
                    self.add_item(A_button)
                    B_button = Button(label='B')
                    B_button.callback = self.B_button_callback
                    self.add_item(B_button)
                async def A_button_callback(self,interaction:discord.Interaction):
                    if interaction.user == interaction.message.interaction.user:
                        embed = discord.Embed(title='請選擇',description=f'{interaction.user.mention}，請選擇 1 或 2',color=discord.Color.purple(),timestamp=datetime.datetime.now())
                        await interaction.response.edit_message(embed=embed,view=Button_config.test.A.Route_A())
                    else:
                        await interaction.response.send_message(f'這不是你的選項。',ephemeral=True)
                async def B_button_callback(self,interaction:discord.Interaction):
                    if interaction.user == interaction.message.interaction.user:
                        embed = discord.Embed(title='結果',description=f'選了B的你\n命運終究是沒辦法跳出的。',color=discord.Color.purple(),timestamp=datetime.datetime.now())
                        await interaction.response.edit_message(embed=embed,view=Button_config.test.A())
                    else:
                        await interaction.response.send_message(f'這不是你的選項。',ephemeral=True)
            class B(View):
                class Route_A(View):
                    def __init__(self):
                        super().__init__(timeout=None)
                        A1_button = Button(label='A1')
                        A1_button.callback = self.A1_button_callback
                        self.add_item(A1_button)
                        A2_button = Button(label='A2')
                        A2_button.callback = self.A2_button_callback
                        self.add_item(A2_button)
                        back_button = Button(label='返回',style=discord.ButtonStyle.red)
                        back_button.callback = self.back_button_callback
                        self.add_item(back_button)
                    async def A1_button_callback(self,interaction:discord.Interaction):
                        embed = discord.Embed(title='結果',description=f'雖然 {interaction.user.mention} 選擇了 A1，但還是會回到 B，因為這就是命運石之門的選擇。',color=discord.Color.purple(),timestamp=datetime.datetime.now())
                        await interaction.response.edit_message(embed=embed,view=Button_config.test.B())
                    async def A2_button_callback(self,interaction:discord.Interaction):
                        embed = discord.Embed(title='結果',description=f'雖然 {interaction.user.mention} 選擇了 A2，但還是會回到 B，因為這就是命運石之門的選擇。',color=discord.Color.purple(),timestamp=datetime.datetime.now())
                        await interaction.response.edit_message(embed=embed,view=Button_config.test.B())
                    async def back_button_callback(self,interaction:discord.Interaction):
                        embed = discord.Embed(title='請選擇',description=f'您好{interaction.user.mention}，請選擇 A 或 B',color=discord.Color.purple(),timestamp=datetime.datetime.now())
                        await interaction.response.edit_message(embed=embed,view=Button_config.test.B())
                def __init__(self):
                    super().__init__(timeout=None)
                    A_button = Button(label='A')
                    A_button.callback = self.A_button_callback
                    self.add_item(A_button)
                    B_button = Button(label='B')
                    B_button.callback = self.B_button_callback
                    self.add_item(B_button)
                async def A_button_callback(self,interaction:discord.Interaction):
                    embed = discord.Embed(title='請選擇',description=f'{interaction.user.mention}，請選擇 1 或 2',color=discord.Color.purple(),timestamp=datetime.datetime.now())
                    await interaction.response.edit_message(embed=embed,view=Button_config.test.B.Route_A())
                async def B_button_callback(self,interaction:discord.Interaction):
                    embed = discord.Embed(title='結果',description=f'選了B的你\n命運終究是沒辦法跳出的。',color=discord.Color.purple(),timestamp=datetime.datetime.now())
                    await interaction.response.edit_message(embed=embed,view=Button_config.test.B())
            class name(View):
                def __init__(self):
                    super().__init__(timeout=None)
                    random_color_button = Button(label='random_color')
                    random_color_button.callback = self.random_color_button_callback
                    self.add_item(random_color_button)
                async def random_color_button_callback(self,interaction:discord.Interaction):
                    directory = r'imege\rpg\color'
                    os.makedirs(directory, exist_ok=True)
                    width = 192
                    height = 108
                    R = (int(user_color,16) >> 16) & 0xff
                    G = (int(user_color,16) >> 8) & 0xff
                    B = int(user_color,16) & 0xff
                    file_path = os.path.join(directory, f'{str(user_color)}.png')
                    
                    if not os.path.exists(file_path):
                        image = Image.new('RGB', (width, height), (R, G, B))
                        image.save(file_path, format='PNG')
                    file_path = f'imege/rpg/color/{user_color}.png'
                    file = discord.File(file_path, filename=f'{user_color}.png')
                    embed = discord.Embed(description=f'# <:LOGO1:1221378614524641332>__{'random_color'}__',colour=int(user_color,16),timestamp=datetime.datetime.now())
                    embed.add_field(name='',value=f'**顏色 :**\n> RGB  `{str(R).zfill(3)} , {str(G).zfill(3)} , {str(B).zfill(3)}`\n> HEX `#{user_color}`',inline=False)
                    embed.set_image(url=f'attachment://{user_color}.png')
                    await interaction.response.edit_message(attachments=[file],embed=embed,view=Button_config.first_online.color())
    class RPG(Cog_extension):
        commandname = (f'{prefix}interface')
        @app_commands.command(name = commandname, description = '叫出介面')
        async def interface(self,interaction:discord.Interaction):
            test = 'No'
            #A or B or No
            if test =='No':
                with open('cmds\\data\\user_data.json' , 'r' , encoding='utf-8') as userdata_file:
                    userdata = json.load(userdata_file)
                author_id = interaction.user.id
                if author_id == int('697842681082281985'):
                    author_id = 938100109240074310
                if 'RPG' not in userdata[str(author_id)]:
                    await interaction.response.send_message(content='# 歡迎遊玩',view=Button_config.Start_Screen())
                else:
                    await interaction.response.send_message(view=Button_config.Start_Screen())
           
           
           
           
           
           
           
           
            else:
                embed = discord.Embed(title='請選擇',description=f'您好{interaction.user.mention}，請選擇 A 或 B',color=discord.Color.purple(),timestamp=datetime.datetime.now())
                if test == 'A':
                    await interaction.response.send_message(embed=embed,view=Button_config.test.A())
                if test == 'B':
                    await interaction.response.send_message(embed=embed,view=Button_config.test.B())
            
    async def setup(bot):
        await bot.add_cog(RPG(bot))
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
elif Test_mod == False:
    class RPG(Cog_extension):
        pass
    async def setup(bot):
        await bot.add_cog(RPG(bot))