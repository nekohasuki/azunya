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
lang=format[Lang[0]]['additional']
with open(f'cmds/rpg_define/{Lang[0]}.lang','r',encoding='utf-8') as Lang_file:
    for line in Lang_file:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        key,value = line.split('=',1)
        if value in format[Lang[0]]["lang"]:
            lang[key] = format[Lang[0]]["lang"][value]
        else:
            lang[key] = f'"{value}"'
'''
dump_userdata='''
with open('cmds/data/user_data.json','w',encoding='utf-8') as userdata_file:
    json.dump(userdata , userdata_file , indent=4)
'''
from core.classes import Cog_extension

import asyncio,datetime,json,os,random
from PIL import Image

prefix = 'rpg-'
Test_mod = True
#      True or False

if Test_mod:
    Lang=['en_US']
    class Default:
        class Buttons:
            @staticmethod
            def decided():
                variable={}
                exec(open_file,globals(),variable)
                lang = variable.get('lang')
                return Button(label=f'{eval(lang.get('decided','"error402"'))}',style=discord.ButtonStyle.green)
            @staticmethod
            def back():
                variable={}
                exec(open_file,globals(),variable)
                lang = variable.get('lang')
                return Button(label=f'{eval(lang.get('back','"error402"'))}',style=discord.ButtonStyle.red)
            @staticmethod
            def previous():
                variable={}
                exec(open_file,globals(),variable)
                lang = variable.get('lang')
                return Button(label=f'{eval(lang.get('previous','"error402"'))}')
            @staticmethod
            def next():
                variable={}
                exec(open_file,globals(),variable)
                lang = variable.get('lang')
                return Button(label=f'{eval(lang.get('next','"error402"'))}')
        class language(View,Select):
            def __init__(self):
                super().__init__()
                variable={}
                exec(open_file,globals(),variable)
                lang = variable.get('lang')
                options=[]
                for language in os.listdir('cmds/rpg_define'):
                    if language.endswith('lang'):
                        with open(f'cmds/rpg_define/{language}','r',encoding='utf-8') as Lang_file:
                            for line in Lang_file:
                                if line.strip().startswith('language-Type'):
                                    line = line.strip().split('=',1)[1]
                                    options.append(SelectOption(label=line,value=language[:-5]))
                options = Select(placeholder=f'{eval(lang.get('language','"rerror402"'))}...',options=options)
                options.callback = self.options_callback
                self.add_item(options)
                decided = Default.Buttons.decided()
                decided.callback = self.decided_callback
                self.add_item(decided)
                back = Default.Buttons.back()
                back.callback = self.back_callback
                self.add_item(back)
            async def options_callback(self,interaction:discord.Interaction):
                user = interaction.user.id
                if user == 697842681082281985:
                    user = 938100109240074310
                user = str(user)
                variable={}
                exec(open_file,globals(),variable)
                userdata = variable.get('userdata')
                setting = variable.get('setting')
                if 'RPG' not in userdata[user]:
                    await interaction.response.send_message(f'User:<@{user}>你的資料不知道為何但就是不完整\n請你先到[__領取身分的地方__](https://ptb.discord.com/channels/{interaction.guild.id}/{setting['ROLE_MESSAGE_CHANNEL_ID']}/{setting['ROLE_MESSAGE_ID']})重新領取身分\n如果還是不行請通知管理員',ephemeral=True)
                else:
                    if 'language' in userdata[user]['RPG']:
                        userdata[user]['RPG']['language'] = interaction.data['values'][0]
                    else:
                        userdata[user]['RPG'].update({'language':interaction.data['values'][0]})
                    exec(dump_userdata)
                for line in Lang:
                    Lang.remove(line)
                Lang.append(userdata[user]['RPG']['language'])
                variable={}
                exec(open_file,globals(),variable)
                lang = variable.get('lang')
                await interaction.response.edit_message(content=f'{eval(lang.get('language','"rerror402"'))} : {eval(lang.get('language-Type','"rerror402"'))}',view=Interface_Config.first_online.language())
            async def decided_callback(self,interaction:discord.Interaction):
                await interaction.response.edit_message(delete_after=0)
            async def back_callback(self,interaction:discord.Interaction):
                # await interaction.response.send_message('這是永久按鈕你想幹嘛???',ephemeral=True)
                await interaction.response.edit_message(delete_after=0)
        class Player_Guidelines(View):
            def __init__(self,Page=1):
                super().__init__(timeout=None)  
                self.page = Page
                variable={}
                exec(open_file,globals(),variable)
                lang = variable.get('lang')

                previous = Default.Buttons.previous()
                previous.callback = self.previous_callback
                self.add_item(previous)
                page = Button(label=f'{Page}/7',disabled=True)
                page.callback = self.page_callback
                self.add_item(page)
                next = Default.Buttons.next()
                next.callback = self.next_callback
                self.add_item(next)

                User_Terms = Button(label=eval(lang.get('User_Terms','"rerror402"')),style=discord.ButtonStyle.blurple,row=1)
                User_Terms.callback = self.User_Terms_callback
                self.add_item(User_Terms)

                decided = Default.Buttons.decided()
                decided.callback = self.decided_callback
                decided.row = 2
                self.add_item(decided)
                back = Default.Buttons.back()
                back.row = 2
                back.callback = self.back_callback
                self.add_item(back)

            async def previous_callback(self,interaction:discord.Interaction):
                Page = self.page - 1
                if Page < 1:
                    Page = 1
                variable={}
                exec(open_file,globals(),variable)
                lang = variable.get('lang')
                embed=None
                await interaction.response.edit_message(content=None,embed=embed,view=Default.Player_Guidelines(Page))
            async def page_callback():
                pass
            async def next_callback(self,interaction:discord.Interaction):
                Page = self.page + 1
                if Page > 7:
                    Page = 7
                variable={}
                exec(open_file,globals(),variable)
                lang = variable.get('lang')
                embed=None
                await interaction.response.edit_message(content=None,embed=embed,view=Default.Player_Guidelines(Page))

            async def User_Terms_callback(self,interaction:discord.Interaction):
                await interaction.response.edit_message(content='',view=Interface_Config.first_online.User_Terms())

            async def decided_callback(self,interaction:discord.Interaction):
                await interaction.response.edit_message(content='',view=Interface_Config.first_online.Player_Guidelines())
            async def back_callback(self,interaction:discord.Interaction):
                user = interaction.user.id
                if user == 697842681082281985:
                    user = 938100109240074310
                user = str(user)
                variable={}
                exec(open_file,globals(),variable)
                userdata = variable.get('userdata')
                # setting = variable.get('setting')
                if userdata[user]['RPG']['setting_mod']:
                    embed=None
                    await interaction.response.edit_message(content='',embed=None,view=Interface_Config.first_online.language())
                else:
                    await interaction.response.edit_message(delete_after=0)

        class User_Terms(View):
            def __init__(self, Page=1):
                super().__init__(timeout=None)
                self.page = Page
                
                previous = Default.Buttons.previous()
                previous.callback = self.previous_callback
                self.add_item(previous)
                page = Button(label=f'{Page}/9', disabled=True)
                page.callback = self.page_callback
                self.add_item(page)
                next = Default.Buttons.next()
                next.callback = self.next_callback
                self.add_item(next)
                
                back = Default.Buttons.back()
                back.row = 1
                back.callback = self.back_callback
                self.add_item(back)

            async def previous_callback(self, interaction: discord.Interaction):
                Page = self.page-1
                if Page < 1:
                    Page = 1
                variable={}
                exec(open_file,globals(),variable)
                lang = variable.get('lang')
                embed=None
                await interaction.response.edit_message(content=None,embed=embed,view=Default.User_Terms(Page))

            async def page_callback(self, interaction: discord.Interaction):
                pass

            async def next_callback(self, interaction: discord.Interaction):
                Page = self.page+1
                if Page > 9:
                    Page = 9
                variable={}
                exec(open_file,globals(),variable)
                lang = variable.get('lang')
                embed=None
                await interaction.response.edit_message(content=None,embed=embed,view=Default.User_Terms(Page))

            async def back_callback(self, interaction: discord.Interaction):
                user = interaction.user.id
                if user == 697842681082281985:
                    user = 938100109240074310
                user = str(user)
                variable={}
                exec(open_file,globals(),variable)
                userdata = variable.get('userdata')
                # setting = variable.get('setting')
                if userdata[user]['RPG']['setting_mod']:
                    embed=None
                    await interaction.response.edit_message(content=None,embed=embed,view=Interface_Config.first_online.Player_Guidelines())
                else:
                    await interaction.response.edit_message(delete_after=0)


    
    class Interface_Config:
        class first_online:
            class language(Default.language):
                async def decided_callback(self,interaction:discord.Interaction):
                    user = interaction.user.id
                    if user == 697842681082281985:
                        user = 938100109240074310
                    user = str(user)
                    variable={}
                    exec(open_file,globals(),variable)
                    userdata = variable.get('userdata')
                    setting = variable.get('setting')
                    if 'RPG' not in userdata[user]:
                        await interaction.response.send_message(f'User:<@{user}>你的資料不知道為何但就是不完整\n請你先到[__領取身分的地方__](https://ptb.discord.com/channels/{interaction.guild.id}/{setting['ROLE_MESSAGE_CHANNEL_ID']}/{setting['ROLE_MESSAGE_ID']})重新領取身分\n如果還是不行請通知管理員',ephemeral=True)
                    else:
                        if 'language' in userdata[user]['RPG']:
                            userdata[user]['RPG']['language'] = Lang[0]
                        else:
                            userdata[user]['RPG'].update({'language':Lang[0]})
                        exec(dump_userdata)
                        if userdata[user]['RPG']['setting_mod']:
                            await interaction.response.edit_message(content='123',view=Interface_Config.first_online.Player_Guidelines())
                        else:
                            await interaction.response.edit_message(content='OK',view=None)
                async def back_callback(self,interaction:discord.Interaction):
                    await interaction.response.edit_message(content='** **',embed=None,view=None)

            class Player_Guidelines(Default.Player_Guidelines):
                async def back_callback(self,interaction:discord.Interaction):
                    await interaction.response.edit_message(content='',embed=None,view=Interface_Config.first_online.language())

            class User_Terms(Default.User_Terms):
                async def back_callback(self, interaction: discord.Interaction):
                    embed=None
                    await interaction.response.edit_message(content=None,embed=embed,view=Interface_Config.first_online.Player_Guidelines())

            
    class RPG(Cog_extension):
        commandname = (f'{prefix}interface')
        @app_commands.command(name = commandname, description = '叫出介面')
        async def name(self,interaction:discord.Interaction):
            user = interaction.user.id
            if user == 697842681082281985:
                user = 938100109240074310
            user = str(user)
            variable = {}
            exec(open_file,globals(),variable)
            userdata = variable.get('userdata')
            setting = variable.get('setting')
            for line in Lang:
                Lang.remove(line)
            if 'language' in userdata[user]['RPG'] and 'RPG'in userdata[user]:
                Lang.append(userdata[user]['RPG']['language'])
            else:
                Lang.append('en_US')
            
            if 'RPG' not in userdata[user]:
                await interaction.response.send_message(f'User:<@{user}>你的資料不知道為何但就是不完整\n請你先到[__領取身分的地方__](https://ptb.discord.com/channels/{interaction.guild.id}/{setting['ROLE_MESSAGE_CHANNEL_ID']}/{setting['ROLE_MESSAGE_ID']})重新領取身分\n如果還是不行請通知管理員',ephemeral=True)
            else:
                Setting = ['language','first_online_time']
                setting_mod = False
                for line in Setting:
                    if line not in userdata[user]['RPG']:
                        setting_mod = True
                if setting_mod:
                    if 'setting_mod' in userdata[user]['RPG']:
                            userdata[user]['RPG']['setting_mod'] = setting_mod
                    else:
                        userdata[user]['RPG'].update({'setting_mod':setting_mod})
                    exec(dump_userdata)
                    # await interaction.response.send_message('',view=Interface_Config.first_online.language())
                    await interaction.response.send_message('',view=Interface_Config.first_online.Player_Guidelines())
                else:
                    await interaction.response.send_message('OK')

    async def setup(bot):
        await bot.add_cog(RPG(bot))
# #||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# elif Test_mod == "A":
# #||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
else:
    User=[]
    Lang=[]
    class Config:
        class first_online:
            class language:
                class choice(View):
                    def __init__(self):
                        super().__init__(timeout=None)
                        language_select = Select(placeholder="language...", options=[
                            SelectOption(label="language (en_US)", value="en_US"),
                            SelectOption(label="語言 (zh_TW)", value="zh_TW"),
                            SelectOption(label="言語 (ja_JP)", value="ja_JP"),
                        ])
                        async def language_select_callback(interaction: discord.Interaction):
                            selected_language = language_select.values[0]
                            variable={}
                            exec(open_file,globals(),variable)
                            userdata=variable.get('userdata')
                            format=variable.get('format')

                            user = interaction.user.id
                            if user == int(697842681082281985):
                                user = 938100109240074310

                            if 'language' not in userdata[str(user)]['RPG']:
                                userdata[str(user)]['RPG'].update({'language':selected_language})
                            else:
                                userdata[str(user)]['RPG']['language']=selected_language
                            exec(dump_userdata)

                            for list in Lang:
                                Lang.remove(list)
                            Lang.append(selected_language)
                            for list in User:
                                User.remove(list)
                            User.append(interaction.user.id)

                            language = userdata[str(user)]['RPG']['language']
                            lang = format[language]["additional"]
                            with open(f'cmds/rpg_define/{language}.lang','r',encoding='utf-8') as Lang_file:
                                for line in Lang_file:
                                    line = line.strip()
                                    if not line or line.startswith('#'):
                                        continue
                                    key, value = line.split('=', 1)
                                    if value in format[language]["lang"]:
                                        pass
                                        lang[key] = format[language]["lang"][value]
                                    else:
                                        lang[key] = f'"{value}"'

                            await interaction.response.edit_message(content=f"{eval(lang['language'])} {eval(lang['choice'])} : {selected_language}",view=Config.first_online.language.rechoice())

                        language_select.callback = language_select_callback
                        self.add_item(language_select)

                        back_button = Button(label='Back',style=discord.ButtonStyle.red)
                        back_button.callback = self.back_button_callback
                        self.add_item(back_button)
                    async def back_button_callback(self,interaction:discord.Interaction):
                        await interaction.response.edit_message(delete_after=0) 

                class rechoice(View):
                    def __init__(self):
                        super().__init__(timeout=None)
                        user = User[0]
                        if user == int(697842681082281985):
                            user = 938100109240074310
                            
                        variable={}
                        exec(open_file,globals(),variable)
                        userdata=variable.get('userdata')
                        format=variable.get('format')
                        language = userdata[str(user)]['RPG']['language']
                        lang=format[language]["additional"]
                        with open(f'cmds/rpg_define/{language}.lang','r',encoding='utf-8') as Lang_file:
                            for line in Lang_file:
                                line = line.strip()
                                if not line or line.startswith('#'):
                                    continue
                                key, value = line.split('=', 1)
                                if value in format[language]["lang"]:
                                    pass
                                    lang[key] = format[language]["lang"][value]
                                else:
                                    lang[key] = f'"{value}"'

                        language_select = Select(placeholder=f'{eval(lang['language'])}...', options=[
                            SelectOption(label="language (en_US)", value="en_US"),
                            SelectOption(label="語言 (zh_TW)", value="zh_TW"),
                            SelectOption(label="言語 (ja_JP)", value="ja_JP"),
                        ])
                        async def language_select_callback(interaction: discord.Interaction):
                            selected_language = language_select.values[0]                            
                            variable={}
                            exec(open_file,globals(),variable)
                            userdata=variable.get('userdata')
                            if 'language' not in userdata[str(user)]['RPG']:
                                userdata[str(user)]['RPG'].update({'language':selected_language})
                            else:
                                userdata[str(user)]['RPG']['language']=selected_language
                            exec(dump_userdata)

                            for list in Lang:
                                Lang.remove(list)
                            Lang.append(selected_language)
                            for list in User:
                                User.remove(list)
                            User.append(interaction.user.id)

                            language = userdata[str(user)]['RPG']['language']
                            lang=format[language]["additional"]
                            with open(f'cmds/rpg_define/{language}.lang','r',encoding='utf-8') as Lang_file:
                                for line in Lang_file:
                                    line = line.strip()
                                    if not line or line.startswith('#'):
                                        continue
                                    key, value = line.split('=', 1)
                                    if value in format[language]["lang"]:
                                        pass
                                        lang[key] = format[language]["lang"][value]
                                    else:
                                        lang[key] = f'"{value}"'

                            await interaction.response.edit_message(content=f"{eval(lang['language'])} {eval(lang['choice'])} : {selected_language}",view=Config.first_online.language.rechoice())
                        
                        language_select.callback = language_select_callback
                        self.add_item(language_select)

                        choice_button = Button(label=eval(lang['choice']),style=discord.ButtonStyle.green)
                        choice_button.callback = self.choice_button_callback
                        self.add_item(choice_button)
                        back_button = Button(label=eval(lang['back']),style=discord.ButtonStyle.red)
                        back_button.callback = self.back_button_callback
                        self.add_item(back_button)
                    async def choice_button_callback(self,interaction:discord.Interaction):
                        user = interaction.user.id
                        if user == int(697842681082281985):
                            user = 938100109240074310
                        variable={}
                        exec(open_file,globals(),variable)
                        userdata=variable.get('userdata')
                        userdata[str(user)]['RPG']['language']=Lang[0]
                        exec(dump_userdata)

                        await interaction.response.edit_message(delete_after=0) 

                    async def back_button_callback(self,interaction:discord.Interaction):
                        await interaction.response.edit_message(delete_after=0)


            class name(View):
                def __init__(self):
                    super().__init__(timeout=None)
                    language_button = Button(label='language_Sheet')
                    language_button.callback = self.language_button_callback
                    self.add_item(language_button)
                async def language_button_callback(self,interaction:discord.Interaction):
                    await interaction.response.edit_message(content='# 種族',view=Config.first_online.Race())
            
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
                    await interaction.response.edit_message(attachments=[],embed=None,view=Config.Start_Screen())

                async def random_color_button_callback(self,interaction:discord.Interaction):
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
                    
                async def back_button_callback(self,interaction:discord.Interaction):
                    await interaction.response.edit_message(attachments=[],embed=None,view=Config.Start_Screen())
            
            class Race():
                pass
            
            class Main_profession():
                pass

        class Start_Screen(View):
            def __init__(self):
                super().__init__(timeout=None)
                Character_Sheet_button = Button(label='Character_Sheet')
                Character_Sheet_button.callback = self.Character_Sheet_button_callback
                self.add_item(Character_Sheet_button)

            async def Character_Sheet_button_callback(self,interaction:discord.Interaction):
                user = interaction.user.id
                if user == int(697842681082281985):
                    user = 938100109240074310
                with open('cmds/data/user_data.json' , 'r' , encoding='utf-8') as userdata_file:
                    userdata = json.load(userdata_file)
                with open('cmds/rpg_define/format.json','r',encoding='utf-8') as Format_file:
                    format = json.load(Format_file)
                display_name=userdata[f'{user}']['display_name']
                RPG = userdata[f'{user}']['RPG']
                lang=format[RPG['language']]["additional"]
                with open(f'cmds/rpg_define/{RPG['language']}.lang','r',encoding='utf-8') as Lang_file:
                    for line in Lang_file:
                        line = line.strip()
                        if not line or line.startswith('#'):
                            continue
                        key, value = line.split('=', 1)
                        if value in format[RPG['language']]['lang']:
                            lang[key] = format[RPG['language']]["lang"][value]
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
                await interaction.response.edit_message(content='',embed=None,view=Config.Start_Screen())



        class test:
            class name(View):
                def __init__(self):
                    super().__init__(timeout=None)
                    random_color_button = Button(label='random_color')
                    random_color_button.callback = self.random_color_button_callback
                    self.add_item(random_color_button)
                async def random_color_button_callback(self,interaction:discord.Interaction):
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
                with open('setting.json','r',encoding='utf-8') as setting_file:
                    setting = json.load(setting_file)
                with open('cmds/data/user_data.json' , 'r' , encoding='utf-8') as userdata_file:
                    userdata = json.load(userdata_file)
                user = interaction.user.id
                if user == int('697842681082281985'):
                    user = 938100109240074310
                if "RPG" not in userdata[str(user)]:
                    await interaction.response.send_message(f'User:<@{user}>你的資料不知道為何但就是不完整\n請你先到[__領取身分的地方__](https://ptb.discord.com/channels/{interaction.guild.id}/{setting['ROLE_MESSAGE_CHANNEL_ID']}/{setting['ROLE_MESSAGE_ID']})重新領取身分\n如果還是不行請通知管理員',ephemeral=True)
                elif userdata[str(user)]['RPG'] == {}:
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