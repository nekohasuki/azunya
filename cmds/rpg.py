import discord
from discord.ext import commands
from discord import app_commands,SelectOption
from discord.ui import Button,Modal,Select,TextInput,View
#Dynamic,Item
open_file='''
with open('setting.json','r',encoding='utf-8') as setting_file:
    setting = json.load(setting_file)
with open('cmds/data/user_data.json' ,'r' ,encoding='utf-8') as userdata_file:
    userdata = json.load(userdata_file)

with open('cmds/rpg_define/format.json','r',encoding='utf-8') as Format_file:
    format = json.load(Format_file)
lang=format[Lang[0]]['additional']
lang.update(format['Shared']['additional'])
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
for line in lang:
    if eval(lang[line]) in format[Lang[0]]['additional']:
        lang[line] = format[Lang[0]]['additional'][eval(lang[line])]

with open(f'cmds/rpg_define/rpg_definitions.json','r',encoding='utf-8') as RPG_definitions_fill:
    rpg_definitions = json.load(RPG_definitions_fill)
'''
dump_userdata='''
with open('cmds/data/user_data.json','w',encoding='utf-8') as userdata_file:
    json.dump(userdata ,userdata_file ,indent=4)
'''
from core.classes import Cog_extension

import asyncio,datetime,json,os,random,re
from PIL import Image

prefix = 'rpg-'
Test_mod = True
#      True or False or None

if Test_mod:
    Lang = ['en_US']
    Color = 0xcfbfff
    Set_Color = [hex(Color)]
    Race = 'Human'
    Set_Race = [Race]
    Main_profession = 'Warrior'
    class Config:
        class Default:
            class Buttons:
                @staticmethod
                def decided():
                    variable = {}
                    exec(open_file,globals(),variable)
                    lang = variable.get('lang')
                    return Button(label = f'{eval(lang.get('decided',lang['error402']))}',style = discord.ButtonStyle.green)
                @staticmethod
                def random():
                    variable = {}
                    exec(open_file,globals(),variable)
                    lang = variable.get('lang')
                    return Button(label = f'{eval(lang.get('random',lang['error402']))}',style = discord.ButtonStyle.blurple)
                @staticmethod
                def back():
                    variable = {}
                    exec(open_file,globals(),variable)
                    lang = variable.get('lang')
                    return Button(label = f'{eval(lang.get('back',lang['error402']))}',style = discord.ButtonStyle.red)
                @staticmethod
                def previous():
                    variable = {}
                    exec(open_file,globals(),variable)
                    lang = variable.get('lang')
                    return Button(label = f'{eval(lang.get('previous',lang['error402']))}')
                @staticmethod
                def next():
                    variable = {}
                    exec(open_file,globals(),variable)
                    lang = variable.get('lang')
                    return Button(label = f'{eval(lang.get('next',lang['error402']))}')
            class Language(View,Select):
                def __init__(self,back = True):
                    super().__init__(timeout = None)
                    variable = {}
                    exec(open_file,globals(),variable)
                    lang = variable.get('lang')
                    if 'row-1' != 0:
                        options = []
                        for language in os.listdir('cmds/rpg_define'):
                            if language.endswith('lang'):
                                with open(f'cmds/rpg_define/{language}','r',encoding = 'utf-8') as Lang_file:
                                    for line in Lang_file:
                                        if line.strip().startswith('language-Type'):
                                            line = line.strip().split('=',1)[1]
                                            options.append(SelectOption(label = line,value = language[:-5]))
                        options = Select(placeholder = f'{eval(lang.get('language','"rerror402"'))}...',options = options)
                        options.callback = self.options_callback
                        self.add_item(options)
                    if 'row-2' != 0:
                        decided = Config.Default.Buttons.decided()
                        decided.row = 1
                        decided.callback = self.decided_callback
                        self.add_item(decided)
                        if back:
                            back = Config.Default.Buttons.back()
                            back.row = 1
                            back.callback = self.back_callback
                            self.add_item(back)
                async def options_callback(self,interaction:discord.Interaction,view = None):
                    user = interaction.user.id
                    if user == 697842681082281985:
                        user = 938100109240074310
                    user = str(user)
                    variable = {}
                    exec(open_file,globals(),variable)
                    userdata = variable.get('userdata')
                    setting = variable.get('setting')
                    if 'RPG' not in userdata[user]:
                        await interaction.response.send_message(f'User:<@{user}>你的資料不知道為何但就是不完整\n請你先到[__領取身分的地方__](https://ptb.discord.com/channels/{interaction.guild.id}/{setting['ROLE_MESSAGE_CHANNEL_ID']}/{setting['ROLE_MESSAGE_ID']})重新領取身分\n如果還是不行請通知管理員',ephemeral = True)
                    else:
                        if 'language' in userdata[user]['RPG']:
                            userdata[user]['RPG']['language'] = interaction.data['values'][0]
                        else:
                            userdata[user]['RPG'].update({'language':interaction.data['values'][0]})
                        exec(dump_userdata)
                    for line in Lang:
                        Lang.remove(line)
                    Lang.append(userdata[user]['RPG']['language'])
                    variable = {}
                    exec(open_file,globals(),variable)
                    lang = variable.get('lang')
                    if view == None:
                        view = Config.Interface.First_online().Language()
                    if view == 'Set_Screen':
                        view = Config.Interface.Set_Screen().Language()
                    await interaction.response.edit_message(content = f'{eval(lang.get('language','"rerror402"'))} :{eval(lang.get('language-Type','"rerror402"'))}',view = view)
                async def decided_callback(self,interaction:discord.Interaction,view = None):
                    user = interaction.user.id
                    if user == 697842681082281985:
                        user = 938100109240074310
                    user = str(user)
                    variable = {}
                    exec(open_file,globals(),variable)
                    userdata = variable.get('userdata')
                    setting = variable.get('setting')
                    lang = variable.get('lang')
                    if 'RPG' not in userdata[user]:
                        await interaction.response.send_message(f'User:<@{user}>你的資料不知道為何但就是不完整\n請你先到[__領取身分的地方__](https://ptb.discord.com/channels/{interaction.guild.id}/{setting['ROLE_MESSAGE_CHANNEL_ID']}/{setting['ROLE_MESSAGE_ID']})重新領取身分\n如果還是不行請通知管理員',ephemeral = True)
                    else:
                        if 'language' in userdata[user]['RPG']:
                            userdata[user]['RPG']['language'] = Lang[0]
                        else:
                            userdata[user]['RPG'].update({'language':Lang[0]})
                        exec(dump_userdata)
                        if view == None:
                            if userdata[user]['RPG']['setting_mod']:
                                Page = 1
                                if 'color' in userdata[user]['RPG']:
                                    user_color = int(userdata[user]['RPG']['color'][2:],16)
                                else:
                                    user_color = Color
                                embed = discord.Embed(description = f'# <:LOGO1:1221378614524641332>__{eval(lang.get('Player_Guidelines',lang['error402']))}__\n{eval(lang.get(f'Player_Guideline_{Page}',lang['error402']))}',colour = user_color,timestamp = datetime.datetime.now())
                                await interaction.response.edit_message(content = None,embed = embed,view = Config.Default.Player_Guidelines(Page))
                            else:
                                await interaction.response.edit_message(delete_after = 0)
                        elif view == 'Set_Screen':
                            await interaction.response.edit_message(content = f'# {eval(lang.get('emoji-setting',lang['error402']))} __|  **{eval(lang.get('set',lang['error402']))}**  |__ {eval(lang.get('emoji-setting',lang['error402']))}',embed = None,view = Config.Interface.Set_Screen().Choice_Screen())
                        
                async def back_callback(self,interaction:discord.Interaction):
                    await interaction.response.edit_message(delete_after = 0)
                    # await interaction.response.send_message('這是永久按鈕你想幹嘛???',ephemeral = True)
            class Player_Guidelines(View):
                def __init__(self,Page = 1):
                    super().__init__(timeout = None)
                    self.page = Page
                    variable = {}
                    exec(open_file,globals(),variable)
                    lang = variable.get('lang')
                    if 'row-1' != 0:
                        previous = Config.Default.Buttons.previous()
                        previous.callback = self.previous_callback
                        self.add_item(previous)
                        page = Button(label = f'{Page}/7',disabled = True)
                        page.callback = self.page_callback
                        self.add_item(page)
                        next = Config.Default.Buttons.next()
                        next.callback = self.next_callback
                        self.add_item(next)
                    if 'row-2' != 0:
                        User_Terms = Button(label = eval(lang.get('User_Terms','"rerror402"')),style = discord.ButtonStyle.blurple,row = 1)
                        User_Terms.callback = self.User_Terms_callback
                        self.add_item(User_Terms)
                    if 'row-3' != 0:
                        if Page == 7:
                            decided = Config.Default.Buttons.decided()
                            decided.row = 2
                            decided.callback = self.decided_callback
                            self.add_item(decided)
                        back = Config.Default.Buttons.back()
                        back.row = 2
                        back.callback = self.back_callback
                        self.add_item(back)
                async def previous_callback(self,interaction:discord.Interaction):
                    Page = self.page - 1
                    if Page < 1:
                        Page = 1
                    user = interaction.user.id
                    if user == 697842681082281985:
                        user = 938100109240074310
                    user = str(user)
                    variable = {}
                    exec(open_file,globals(),variable)
                    userdata = variable.get('userdata')
                    setting = variable.get('setting')
                    lang = variable.get('lang')
                    if 'RPG' not in userdata[user]:
                        await interaction.response.send_message(f'User:<@{user}>你的資料不知道為何但就是不完整\n請你先到[__領取身分的地方__](https://ptb.discord.com/channels/{interaction.guild.id}/{setting['ROLE_MESSAGE_CHANNEL_ID']}/{setting['ROLE_MESSAGE_ID']})重新領取身分\n如果還是不行請通知管理員',ephemeral = True)
                    elif 'color' in userdata[user]['RPG']:
                        user_color = int(userdata[user]['RPG']['color'][2:],16)
                    else:
                        user_color = Color
                    embed = discord.Embed(description = f'# <:LOGO1:1221378614524641332>__{eval(lang.get('Player_Guidelines',lang['error402']))}__\n{eval(lang.get(f'Player_Guideline_{Page}',lang['error402']))}',colour = user_color,timestamp = datetime.datetime.now())
                    await interaction.response.edit_message(content = None,embed = embed,view = Config.Default.Player_Guidelines(Page))
                async def page_callback():
                    pass
                async def next_callback(self,interaction:discord.Interaction):
                    Page = self.page + 1
                    if Page > 7:
                        Page = 7
                    user = interaction.user.id
                    if user == 697842681082281985:
                        user = 938100109240074310
                    user = str(user)
                    variable = {}
                    exec(open_file,globals(),variable)
                    userdata = variable.get('userdata')
                    setting = variable.get('setting')
                    lang = variable.get('lang')
                    if 'RPG' not in userdata[user]:
                        await interaction.response.send_message(f'User:<@{user}>你的資料不知道為何但就是不完整\n請你先到[__領取身分的地方__](https://ptb.discord.com/channels/{interaction.guild.id}/{setting['ROLE_MESSAGE_CHANNEL_ID']}/{setting['ROLE_MESSAGE_ID']})重新領取身分\n如果還是不行請通知管理員',ephemeral = True)
                    elif 'color' in userdata[user]['RPG']:
                        user_color = int(userdata[user]['RPG']['color'][2:],16)
                    else:
                        user_color = Color
                    embed = discord.Embed(description = f'# <:LOGO1:1221378614524641332>__{eval(lang.get('Player_Guidelines',lang['error402']))}__\n{eval(lang.get(f'Player_Guideline_{Page}',lang['error402']))}',colour = user_color,timestamp = datetime.datetime.now())
                    await interaction.response.edit_message(content = None,embed = embed,view = Config.Default.Player_Guidelines(Page))
                async def User_Terms_callback(self,interaction:discord.Interaction):
                    Page = 1
                    user = interaction.user.id
                    if user == 697842681082281985:
                        user = 938100109240074310
                    user = str(user)
                    variable = {}
                    exec(open_file,globals(),variable)
                    userdata = variable.get('userdata')
                    setting = variable.get('setting')
                    lang = variable.get('lang')
                    if 'RPG' not in userdata[user]:
                        await interaction.response.send_message(f'User:<@{user}>你的資料不知道為何但就是不完整\n請你先到[__領取身分的地方__](https://ptb.discord.com/channels/{interaction.guild.id}/{setting['ROLE_MESSAGE_CHANNEL_ID']}/{setting['ROLE_MESSAGE_ID']})重新領取身分\n如果還是不行請通知管理員',ephemeral = True)
                    elif 'color' in userdata[user]['RPG']:
                        user_color = int(userdata[user]['RPG']['color'][2:],16)
                    else:
                        user_color = Color
                    List = []
                    for line in lang:
                        if str(line).startswith(f'User_Terms_{Page}') and not str(line).endswith('0'):
                            List.append(f'{len(List)+1}. {eval(lang.get(line,lang['error402']))}')
                    List = '\n\n'.join(List)
                    embed = discord.Embed(description = f'# <:LOGO1:1221378614524641332>__{eval(lang.get(f'User_Terms',lang['error402']))}__\n**- {eval(lang.get(f'User_Terms_{Page}.0',lang['error402']))} :**\n{List}',colour = user_color,timestamp = datetime.datetime.now())
                    await interaction.response.edit_message(content = None,embed = embed,view = Config.Default.User_Terms(Page))
                async def decided_callback(self,interaction:discord.Interaction):
                    user = interaction.user.id
                    if user == 697842681082281985:
                        user = 938100109240074310
                    user = str(user)
                    variable = {}
                    exec(open_file,globals(),variable)
                    userdata = variable.get('userdata')
                    setting = variable.get('setting')
                    lang = variable.get('lang')
                    if 'RPG' not in userdata[user]:
                        await interaction.response.send_message(f'User:<@{user}>你的資料不知道為何但就是不完整\n請你先到[__領取身分的地方__](https://ptb.discord.com/channels/{interaction.guild.id}/{setting['ROLE_MESSAGE_CHANNEL_ID']}/{setting['ROLE_MESSAGE_ID']})重新領取身分\n如果還是不行請通知管理員',ephemeral = True)
                    else:
                        if 'first_online_time' not in userdata[user]['RPG']:
                            userdata[user]['RPG'].update({'first_online_time':f'{datetime.datetime.now()}'})
                            exec(dump_userdata)
                        if 'color' in userdata[user]['RPG']:
                            user_color = int(userdata[user]['RPG']['color'],16)
                            color = userdata[user]['RPG']['color']
                        else:
                            user_color = Color
                            color = hex(Color)
                        R = int(color[2:-4],16)
                        G = int(color[4:-2],16)
                        B = int(color[-2:],16)
                        directory = 'imege/rpg/color'
                        file_path = os.path.join(directory,f'0x{R}{G}{B}.png')
                        if not os.path.exists(file_path):
                            os.makedirs(directory,exist_ok = True)
                            width = 192
                            height = 108
                            file_path = os.path.join(directory,f'0x{R:02x}{G:02x}{B:02x}.png')
                            if not os.path.exists(file_path):
                                image = Image.new('RGB',(width,height),(R,G,B))
                                image.save(file_path,format = 'PNG')
                                print(f'User:{interaction.user.display_name} adding 0x{R:02x}{G:02x}{B:02x}.png')
                        if userdata[user]['RPG']['setting_mod']:
                            embed = discord.Embed(description = f'# <:LOGO1:1221378614524641332>__{eval(lang.get('random',lang['error402']))}{eval(lang.get('color',lang['error402']))}__',color = user_color,timestamp = datetime.datetime.now())
                            embed.add_field(name = '',value = f'**{eval(lang.get('color',lang['error402']))} :**\n> RGB  `{str(R).zfill(3)},{str(G).zfill(3)},{str(B).zfill(3)}`\n> HEX `#{color[2:]}`',inline = False)
                            embed.set_image(url = f'attachment://{color}.png')
                            file = discord.File(f'imege/rpg/color/{color}.png',filename = f'{color}.png')
                            for set_color in Set_Color:
                                Set_Color.remove(set_color)
                            Set_Color.append(hex(Color))
                            await interaction.response.edit_message(content = None,attachments = [file],embed = embed,view = Config.Interface.First_online().Color())
                        else:
                            await interaction.response.edit_message(content = None,embed = None,view = None)
                async def back_callback(self,interaction:discord.Interaction):
                    user = interaction.user.id
                    if user == 697842681082281985:
                        user = 938100109240074310
                    user = str(user)
                    variable = {}
                    exec(open_file,globals(),variable)
                    userdata = variable.get('userdata')
                    if userdata[user]['RPG']['setting_mod']:
                        await interaction.response.edit_message(content = '',embed = None,view = Config.Interface.First_online().Language())
                    else:
                        await interaction.response.edit_message(content = None,embed = None,view = None)
            class User_Terms(View):
                def __init__(self,Page = 1):
                    super().__init__(timeout = None)
                    self.page = Page
                    if 'row-1' != 0:
                        previous = Config.Default.Buttons.previous()
                        previous.callback = self.previous_callback
                        self.add_item(previous)
                        page = Button(label = f'{Page}/9',disabled = True)
                        page.callback = self.page_callback
                        self.add_item(page)
                        next = Config.Default.Buttons.next()
                        next.callback = self.next_callback
                        self.add_item(next)
                    if 'row-2' != 0:
                        back = Config.Default.Buttons.back()
                        back.row = 1
                        back.callback = self.back_callback
                        self.add_item(back)
                async def previous_callback(self,interaction:discord.Interaction):
                    Page = self.page-1
                    if Page < 1:
                        Page = 1
                    user = interaction.user.id
                    if user == 697842681082281985:
                        user = 938100109240074310
                    user = str(user)
                    variable = {}
                    exec(open_file,globals(),variable)
                    userdata = variable.get('userdata')
                    setting = variable.get('setting')
                    lang = variable.get('lang')
                    if 'RPG' not in userdata[user]:
                        await interaction.response.send_message(f'User:<@{user}>你的資料不知道為何但就是不完整\n請你先到[__領取身分的地方__](https://ptb.discord.com/channels/{interaction.guild.id}/{setting['ROLE_MESSAGE_CHANNEL_ID']}/{setting['ROLE_MESSAGE_ID']})重新領取身分\n如果還是不行請通知管理員',ephemeral = True)
                    elif 'color' in userdata[user]['RPG']:
                        user_color = int(userdata[user]['RPG']['color'][2:],16)
                    else:
                        user_color = Color
                    List = []
                    for line in lang:
                        if str(line).startswith(f'User_Terms_{Page}') and not str(line).endswith('0'):
                            List.append(f'{len(List)+1}. {eval(lang.get(line,lang['error402']))}')
                    List = '\n\n'.join(List)
                    embed = discord.Embed(description = f'# <:LOGO1:1221378614524641332>__{eval(lang.get(f'User_Terms',lang['error402']))}__\n**- {eval(lang.get(f'User_Terms_{Page}.0',lang['error402']))} :**\n{List}',colour = user_color,timestamp = datetime.datetime.now())
                    await interaction.response.edit_message(content = None,embed = embed,view = Config.Default.User_Terms(Page))
                async def page_callback(self,interaction:discord.Interaction):
                    pass
                async def next_callback(self,interaction:discord.Interaction):
                    Page = self.page+1
                    if Page > 9:
                        Page = 9
                    user = interaction.user.id
                    if user == 697842681082281985:
                        user = 938100109240074310
                    user = str(user)
                    variable = {}
                    exec(open_file,globals(),variable)
                    userdata = variable.get('userdata')
                    setting = variable.get('setting')
                    lang = variable.get('lang')
                    if 'RPG' not in userdata[user]:
                        await interaction.response.send_message(f'User:<@{user}>你的資料不知道為何但就是不完整\n請你先到[__領取身分的地方__](https://ptb.discord.com/channels/{interaction.guild.id}/{setting['ROLE_MESSAGE_CHANNEL_ID']}/{setting['ROLE_MESSAGE_ID']})重新領取身分\n如果還是不行請通知管理員',ephemeral = True)
                    elif 'color' in userdata[user]['RPG']:
                        user_color = int(userdata[user]['RPG']['color'][2:],16)
                    else:
                        user_color = Color
                    List = []
                    for line in lang:
                        if str(line).startswith(f'User_Terms_{Page}') and not str(line).endswith('0'):
                            List.append(f'{len(List)+1}. {eval(lang.get(line,lang['error402']))}')
                    List = '\n\n'.join(List)
                    embed = discord.Embed(description = f'# <:LOGO1:1221378614524641332>__{eval(lang.get(f'User_Terms',lang['error402']))}__\n**- {eval(lang.get(f'User_Terms_{Page}.0',lang['error402']))} :**\n{List}',colour = user_color,timestamp = datetime.datetime.now())
                    await interaction.response.edit_message(content = None,embed = embed,view = Config.Default.User_Terms(Page))
                async def back_callback(self,interaction:discord.Interaction):
                    user = interaction.user.id
                    if user == 697842681082281985:
                        user = 938100109240074310
                    user = str(user)
                    variable = {}
                    exec(open_file,globals(),variable)
                    userdata = variable.get('userdata')
                    setting = variable.get('setting')
                    lang = variable.get('lang')
                    if userdata[user]['RPG']['setting_mod']:
                        Page = 1
                        if 'RPG' not in userdata[user]:
                            await interaction.response.send_message(f'User:<@{user}>你的資料不知道為何但就是不完整\n請你先到[__領取身分的地方__](https://ptb.discord.com/channels/{interaction.guild.id}/{setting['ROLE_MESSAGE_CHANNEL_ID']}/{setting['ROLE_MESSAGE_ID']})重新領取身分\n如果還是不行請通知管理員',ephemeral = True)
                        elif 'color' in userdata[user]['RPG']:
                            user_color = int(userdata[user]['RPG']['color'][2:],16)
                        else:
                            user_color = Color
                        embed = discord.Embed(description = f'# <:LOGO1:1221378614524641332>__{eval(lang.get('Player_Guidelines',lang['error402']))}__\n{eval(lang.get(f'Player_Guideline_{Page}',lang['error402']))}',colour = user_color,timestamp = datetime.datetime.now())
                        await interaction.response.edit_message(content = None,embed = embed,view = Config.Default.Player_Guidelines(Page))
                    else:
                        await interaction.response.edit_message(content = None,embed = None,view = None)
            class Color(View):
                def __init__(self,back = True):
                    super().__init__(timeout = None)
                    variable = {}
                    exec(open_file,globals(),variable)
                    lang = variable.get('lang')
                    if 'row-1' != 0:
                        decided = Config.Default.Buttons.decided()
                        decided.callback = self.decided_callback
                        self.add_item(decided)
                        set = Button(label = f'{eval(lang.get('set',lang['error402']))}',style = discord.ButtonStyle.blurple)
                        set.callback = self.set_callback
                        self.add_item(set)
                        random = Config.Default.Buttons.random()
                        random.callback = self.random_callback
                        self.add_item(random)
                        if back:
                            back = Config.Default.Buttons.back()
                            back.callback = self.back_callback
                            self.add_item(back)
                async def decided_callback(self,interaction:discord.Interaction,view = None):
                    user = interaction.user.id
                    if user == 697842681082281985:
                        user = 938100109240074310
                    user = str(user)
                    variable = {}
                    exec(open_file,globals(),variable)
                    userdata = variable.get('userdata')
                    setting = variable.get('setting')
                    lang = variable.get('lang')
                    if 'RPG' not in userdata[user]:
                        await interaction.response.send_message(f'User:<@{user}>你的資料不知道為何但就是不完整\n請你先到[__領取身分的地方__](https://ptb.discord.com/channels/{interaction.guild.id}/{setting['ROLE_MESSAGE_CHANNEL_ID']}/{setting['ROLE_MESSAGE_ID']})重新領取身分\n如果還是不行請通知管理員',ephemeral = True)
                    else:
                        if 'color' not in userdata[user]['RPG']:
                            userdata[user]['RPG'].update({'color':str(Set_Color)[2:-2]})
                            exec(dump_userdata)
                        if view == None:
                            if userdata[user]['RPG']['setting_mod']:
                                for set_race in Set_Race:
                                    Set_Race.remove(set_race)
                                Set_Race.append(Race)
                                await interaction.response.edit_message(content = None,attachments = [],embed = None,view = Config.Interface.First_online().Race())
                            else:
                                await interaction.response.edit_message(delete_after = 0)
                        elif view == 'Set_Screen':
                            await interaction.response.edit_message(content = f'# {eval(lang.get('emoji-setting',lang['error402']))} __|  **{eval(lang.get('set',lang['error402']))}**  |__ {eval(lang.get('emoji-setting',lang['error402']))}',attachments = [],embed = None,view = Config.Interface.Set_Screen().Choice_Screen())
                async def set_callback(self,interaction:discord.Interaction,view = None):
                    if view == None:
                        view = Config.Interface.First_online().Color()
                    if view == 'Set_Screen':
                        view = Config.Interface.Set_Screen().Color()
                    user = interaction.user.id
                    if user == 697842681082281985:
                        user = 938100109240074310
                    user = str(user)
                    variable = {}
                    exec(open_file,globals(),variable)
                    userdata = variable.get('userdata')
                    setting = variable.get('setting')
                    lang = variable.get('lang')
                    class text_input(Modal,title = f'{eval(lang.get('color',lang['error402']))}{eval(lang.get('set',lang['error402']))}'):
                        text_input = TextInput(label = eval(lang.get('color-code','"error402"')),placeholder = "#FFFFFF(HEX) / 255,255,255(RGB)",style = discord.TextStyle.short)
                        async def on_submit(self,interaction:discord.Interaction):
                            if 'RPG' not in userdata[user]:
                                await interaction.response.send_message(f'User:<@{user}>你的資料不知道為何但就是不完整\n請你先到[__領取身分的地方__](https://ptb.discord.com/channels/{interaction.guild.id}/{setting['ROLE_MESSAGE_CHANNEL_ID']}/{setting['ROLE_MESSAGE_ID']})重新領取身分\n如果還是不行請通知管理員',ephemeral = True)
                            else:
                                text = self.text_input.value
                                text = text.replace(' ','').replace('0x','#')
                                color = None
                                if re.match('^[0-9a-fA-F,#]*$',text):
                                    if text.count(',') == 2 and '#' not in text:
                                        R,G,B = text.split(',',2)
                                        if not re.match('^[0-9,]*$',text):
                                            R = int(R,16)
                                            G = int(G,16)
                                            B = int(B,16)
                                        R = int(R) & 0xff
                                        G = int(G) & 0xff
                                        B = int(B) & 0xff
                                        color = f'{(f'{R:0x}').zfill(2)}{(f'{G:0x}').zfill(2)}{(f'{B:0x}').zfill(2)}'
                                    elif text.count('#') == 1 and ',' not in text:
                                        RGB = int(text[1:],16) & 0xffffff
                                        R = (RGB >> 16) & 0xff
                                        G = (RGB >> 8) & 0xff
                                        B = RGB & 0xff
                                        color = f'{(f'{R:0x}').zfill(2)}{(f'{G:0x}').zfill(2)}{(f'{B:0x}').zfill(2)}'
                                    else:
                                        await interaction.response.send_message(f'{eval(lang['error403'])}',ephemeral = True)
                                else:
                                    await interaction.response.send_message(f'{eval(lang['error404'])}',ephemeral = True)
                                if color != None:
                                    directory = 'imege/rpg/color'
                                    os.makedirs(directory,exist_ok = True)
                                    width = 192
                                    height = 108

                                    file_path = os.path.join(directory,f'0x{color}.png')
                                    if not os.path.exists(file_path):
                                        image = Image.new('RGB',(width,height),(R,G,B))
                                        image.save(file_path,format = 'PNG')
                                        print(f'User:{interaction.user.display_name} adding 0x{color}.png')
                                    color = f'0x{color}'
                                    file_path = f'imege/rpg/color/{color}.png'
                                    while not os.path.isfile(file_path):
                                        await asyncio.sleep(0.5)

                                    file = discord.File(file_path,filename = f'{color}.png')
                                    user_color = int(color,16)
                                    if 'color' in userdata[user]['RPG']:
                                        userdata[user]['RPG']['color'] = color
                                    else:
                                        userdata[user]['RPG'].update({'color':color})
                                    exec(dump_userdata)
                                    for set_color in Set_Color:
                                        Set_Color.remove(set_color)
                                    Set_Color.append(color)
                                    embed = discord.Embed(description = f'# <:LOGO1:1221378614524641332>__{eval(lang.get('random',lang['error402']))}{eval(lang.get('color',lang['error402']))}__',color = user_color,timestamp = datetime.datetime.now())
                                    embed.add_field(name = '',value = f'**{eval(lang.get('color',lang['error402']))} :**\n> RGB  `{str(R).zfill(3)},{str(G).zfill(3)},{str(B).zfill(3)}`\n> HEX `#{color[2:]}`',inline = False)
                                    embed.set_image(url = f'attachment://{color}.png')
                                    await interaction.response.edit_message(content = None,attachments = [file],embed = embed,view = view)
                    await interaction.response.send_modal(text_input())
                async def random_callback(self,interaction:discord.Interaction,view = None):
                    user = interaction.user.id
                    if user == 697842681082281985:
                        user = 938100109240074310
                    user = str(user)
                    variable = {}
                    exec(open_file,globals(),variable)
                    userdata = variable.get('userdata')
                    setting = variable.get('setting')
                    lang = variable.get('lang')
                    if 'RPG' not in userdata[user]:
                        await interaction.response.send_message(f'User:<@{user}>你的資料不知道為何但就是不完整\n請你先到[__領取身分的地方__](https://ptb.discord.com/channels/{interaction.guild.id}/{setting['ROLE_MESSAGE_CHANNEL_ID']}/{setting['ROLE_MESSAGE_ID']})重新領取身分\n如果還是不行請通知管理員',ephemeral = True)
                    else:
                        if '這裡是隨機顏色' != 0:
                            directory = 'imege/rpg/color'
                            os.makedirs(directory,exist_ok = True)
                            width = 192
                            height = 108
                            R = random.randint(0x80,0xff)
                            G = random.randint(0x80,0xff)
                            B = random.randint(0x80,0xff)
                            file_path = os.path.join(directory,f'0x{R:02x}{G:02x}{B:02x}.png')
                            if not os.path.exists(file_path):
                                image = Image.new('RGB',(width,height),(R,G,B))
                                image.save(file_path,format = 'PNG')
                                print(f'User:{interaction.user.display_name} adding 0x{R:02x}{G:02x}{B:02x}.png')
                            color = f'0x{R:02x}{G:02x}{B:02x}'
                            file_path = f'imege/rpg/color/{color}.png'
                            while not os.path.isfile(file_path):
                                await asyncio.sleep(0.5)
                        file = discord.File(file_path,filename = f'{color}.png')
                        user_color = int(color,16)
                        if 'color' in userdata[user]['RPG']:
                            userdata[user]['RPG']['color'] = color
                        else:
                            userdata[user]['RPG'].update({'color':color})
                        exec(dump_userdata)
                        for set_color in Set_Color:
                            Set_Color.remove(set_color)
                        Set_Color.append(color)
                        embed = discord.Embed(description = f'# <:LOGO1:1221378614524641332>__{eval(lang.get('random',lang['error402']))}{eval(lang.get('color',lang['error402']))}__',color = user_color,timestamp = datetime.datetime.now())
                        embed.add_field(name = '',value = f'**{eval(lang.get('color',lang['error402']))} :**\n> RGB  `{str(R).zfill(3)},{str(G).zfill(3)},{str(B).zfill(3)}`\n> HEX `#{color[2:]}`',inline = False)
                        embed.set_image(url = f'attachment://{color}.png')
                        if view == None:
                            view = Config.Interface.First_online().Color()
                        if view == 'Set_Screen':
                            view = Config.Interface.Set_Screen().Color()
                        await interaction.response.edit_message(content = None,attachments = [file],embed = embed,view = view)
                async def back_callback(self,interaction:discord.Interaction):
                    Page = 7
                    user = interaction.user.id
                    if user == 697842681082281985:
                        user = 938100109240074310
                    user = str(user)
                    variable = {}
                    exec(open_file,globals(),variable)
                    userdata = variable.get('userdata')
                    setting = variable.get('setting')
                    lang = variable.get('lang')
                    if 'RPG' not in userdata[user]:
                        await interaction.response.send_message(f'User:<@{user}>你的資料不知道為何但就是不完整\n請你先到[__領取身分的地方__](https://ptb.discord.com/channels/{interaction.guild.id}/{setting['ROLE_MESSAGE_CHANNEL_ID']}/{setting['ROLE_MESSAGE_ID']})重新領取身分\n如果還是不行請通知管理員',ephemeral = True)
                    else:
                        if 'color' in userdata[user]['RPG']:
                            user_color = int(userdata[user]['RPG']['color'][2:],16)
                        else:
                            user_color = Color
                        if userdata[user]['RPG']['setting_mod']:
                            embed = discord.Embed(description = f'# <:LOGO1:1221378614524641332>__{eval(lang.get('Player_Guidelines',lang['error402']))}__\n{eval(lang.get(f'Player_Guideline_{Page}',lang['error402']))}',colour = user_color,timestamp = datetime.datetime.now())
                            await interaction.response.edit_message(content = None,attachments = [],embed = embed,view = Config.Default.Player_Guidelines(Page))
                        else:
                            await interaction.response.edit_message(content = None,embed = None,view = None)
            class Race(View,Select):
                def __init__(self):
                    super().__init__(timeout = None)
                    variable = {}
                    exec(open_file,globals(),variable)
                    lang = variable.get('lang')
                    rpg_definitions = variable.get('rpg_definitions')
                    if 'row-1' != 0:
                        options = []
                        for race in rpg_definitions:
                            if race == 'Race':
                                for race in rpg_definitions[race]:
                                    options.append(SelectOption(label = eval(lang.get(race,lang['error402'])),value = race))
                        options = Select(placeholder = f'{eval(lang.get('Race',lang['error402']))}...',options=options)
                        options.callback = self.options_callback
                        self.add_item(options)
                    if 'row-2' != 0:
                        decided = Config.Default.Buttons.decided()
                        decided.row = 1
                        decided.callback = self.decided_callback
                        self.add_item(decided)
                        back = Config.Default.Buttons.back()
                        back.row = 1
                        back.callback = self.back_callback
                        self.add_item(back)
                async def options_callback(self,interaction:discord.Interaction):
                    user = interaction.user.id
                    if user == 697842681082281985:
                        user = 938100109240074310
                    user = str(user)
                    variable = {}
                    exec(open_file,globals(),variable)
                    userdata = variable.get('userdata')
                    setting = variable.get('setting')
                    lang = variable.get('lang')
                    for set_race in Set_Race:
                        Set_Race.remove(set_race)
                    Set_Race.append(interaction.data['values'][0])


                    if 'RPG' not in userdata[user]:
                        await interaction.response.send_message(f'User:<@{user}>你的資料不知道為何但就是不完整\n請你先到[__領取身分的地方__](https://ptb.discord.com/channels/{interaction.guild.id}/{setting['ROLE_MESSAGE_CHANNEL_ID']}/{setting['ROLE_MESSAGE_ID']})重新領取身分\n如果還是不行請通知管理員',ephemeral = True)
                    else:
                        if 'Race' in userdata[user]['RPG']:
                            userdata[user]['RPG']['Race'] = str(Set_Race)[2:-2]
                        else:
                            userdata[user]['RPG'].update({'Race':str(Set_Race)[2:-2]})
                        exec(dump_userdata)
                        if 'color' in userdata[user]['RPG']:
                            user_color = int(userdata[user]['RPG']['color'],16)
                        else:
                            user_color = Color
                    embed = discord.Embed(description = f'# {eval(lang.get(f'emoji-{str(Set_Race)[2:-2]}','"rerror402"'))}\n{eval(lang.get('Race','"rerror402"'))} :{eval(lang.get(str(Set_Race)[2:-2],'"rerror402"'))}',color = user_color,timestamp = datetime.datetime.now())
                    await interaction.response.edit_message(embed = embed,view = Config.Interface.First_online().Race())
                async def decided_callback(self,interaction:discord.Interaction):
                    user = interaction.user.id
                    if user == 697842681082281985:
                        user = 938100109240074310
                    user = str(user)
                    variable = {}
                    exec(open_file,globals(),variable)
                    userdata = variable.get('userdata')
                    setting = variable.get('setting')
                    if 'RPG' not in userdata[user]:
                        await interaction.response.send_message(f'User:<@{user}>你的資料不知道為何但就是不完整\n請你先到[__領取身分的地方__](https://ptb.discord.com/channels/{interaction.guild.id}/{setting['ROLE_MESSAGE_CHANNEL_ID']}/{setting['ROLE_MESSAGE_ID']})重新領取身分\n如果還是不行請通知管理員',ephemeral = True)
                    else:
                        if 'Race' in userdata[user]['RPG']:
                            userdata[user]['RPG']['Race'] = str(Set_Race)[2:-2]
                        else:
                            userdata[user]['RPG'].update({'Race':str(Set_Race)[2:-2]})
                        exec(dump_userdata)
                        if userdata[user]['RPG']['setting_mod']:
                            await interaction.response.edit_message(content = None,attachments = [],embed = None,view = Config.Interface.First_online().Main_profession())
                        else:
                            await interaction.response.edit_message(content = None,embed = None,view = None)
                async def back_callback(self,interaction:discord.Interaction):
                    user = interaction.user.id
                    if user == 697842681082281985:
                        user = 938100109240074310
                    user = str(user)
                    variable = {}
                    exec(open_file,globals(),variable)
                    userdata = variable.get('userdata')
                    setting = variable.get('setting')
                    lang = variable.get('lang')
                    if 'RPG' not in userdata[user]:
                        await interaction.response.send_message(f'User:<@{user}>你的資料不知道為何但就是不完整\n請你先到[__領取身分的地方__](https://ptb.discord.com/channels/{interaction.guild.id}/{setting['ROLE_MESSAGE_CHANNEL_ID']}/{setting['ROLE_MESSAGE_ID']})重新領取身分\n如果還是不行請通知管理員',ephemeral = True)
                    else:
                        if 'color' in userdata[user]['RPG']:
                            user_color = int(userdata[user]['RPG']['color'],16)
                            color = userdata[user]['RPG']['color']
                        else:
                            user_color = Color
                            color = hex(Color)
                        R = int(color[2:-4],16)
                        G = int(color[4:-2],16)
                        B = int(color[-2:],16)
                        directory = 'imege/rpg/color'
                        file_path = os.path.join(directory,f'0x{R}{G}{B}.png')
                        if not os.path.exists(file_path):
                            os.makedirs(directory,exist_ok = True)
                            width = 192
                            height = 108
                            file_path = os.path.join(directory,f'0x{R:02x}{G:02x}{B:02x}.png')
                            if not os.path.exists(file_path):
                                image = Image.new('RGB',(width,height),(R,G,B))
                                image.save(file_path,format = 'PNG')
                                print(f'User:{interaction.user.display_name} adding 0x{R:02x}{G:02x}{B:02x}.png')
                        if userdata[user]['RPG']['setting_mod']:
                            embed = discord.Embed(description = f'# <:LOGO1:1221378614524641332>__{eval(lang.get('random',lang['error402']))}{eval(lang.get('color',lang['error402']))}__',color = user_color,timestamp = datetime.datetime.now())
                            embed.add_field(name = '',value = f'**{eval(lang.get('color',lang['error402']))} :**\n> RGB  `{str(R).zfill(3)},{str(G).zfill(3)},{str(B).zfill(3)}`\n> HEX `#{color[2:]}`',inline = False)
                            embed.set_image(url = f'attachment://{color}.png')
                            file = discord.File(f'imege/rpg/color/{color}.png',filename = f'{color}.png') 
                            for set_color in Set_Color:
                                Set_Color.remove(set_color)
                            Set_Color.append(hex(Color))
                            await interaction.response.edit_message(content = None,attachments = [file],embed = embed,view = Config.Interface.First_online().Color())
                        else:
                            await interaction.response.edit_message(content = None,embed = None,view = None)
            class Main_profession(View,Select):
                def __init__(self):
                    super().__init__(timeout = None)
                    variable = {}
                    exec(open_file,globals(),variable)
                    lang = variable.get('lang')
                    rpg_definitions = variable.get('rpg_definitions')
                    if 'row-1' != 0:
                        options = []
                        for main in rpg_definitions:
                            if main == 'Main_profession':
                                for main in rpg_definitions[main]:
                                    options.append(SelectOption(label = eval(lang.get(main,lang['error402'])),value = main))
                        options = Select(placeholder = f'{eval(lang.get('Main_profession',lang['error402']))}...',options=options)
                        options.callback = self.options_callback
                        self.add_item(options)
                    if 'row-2' != 0:
                        decided = Config.Default.Buttons.decided()
                        decided.row = 1
                        decided.callback = self.decided_callback
                        self.add_item(decided)
                        back = Config.Default.Buttons.back()
                        back.row = 1
                        back.callback = self.back_callback
                        self.add_item(back)
                async def options_callback(self,interaction:discord.Interaction):
                    user = interaction.user.id
                    if user == 697842681082281985:
                        user = 938100109240074310
                    user = str(user)
                    variable = {}
                    exec(open_file,globals(),variable)
                    userdata = variable.get('userdata')
                    setting = variable.get('setting')
                    lang = variable.get('lang')
                    if 'RPG' not in userdata[user]:
                        await interaction.response.send_message(f'User:<@{user}>你的資料不知道為何但就是不完整\n請你先到[__領取身分的地方__](https://ptb.discord.com/channels/{interaction.guild.id}/{setting['ROLE_MESSAGE_CHANNEL_ID']}/{setting['ROLE_MESSAGE_ID']})重新領取身分\n如果還是不行請通知管理員',ephemeral = True)
                    else:
                        Main_profession = interaction.data['values'][0]
                        if 'Main_profession' in userdata[user]['RPG']:
                            userdata[user]['RPG']['Main_profession'] = {"class":Main_profession,"level":0}
                        else:
                            userdata[user]['RPG'].update({'Main_profession':{"class":Main_profession,"level":0}})
                        exec(dump_userdata)
                        await interaction.response.edit_message(content = f'{eval(lang.get('Main_profession','"rerror402"'))} :{eval(lang.get(Main_profession,'"rerror402"'))}',view = Config.Interface.First_online().Main_profession())
                async def decided_callback(self,interaction:discord.Interaction):
                    user = interaction.user.id
                    if user == 697842681082281985:
                        user = 938100109240074310
                    user = str(user)
                    variable = {}
                    exec(open_file,globals(),variable)
                    userdata = variable.get('userdata')
                    setting = variable.get('setting')
                    lang = variable.get('lang')
                    rpg_definitions = variable.get('rpg_definitions')
                    if 'RPG' not in userdata[user]:
                        await interaction.response.send_message(f'User:<@{user}>你的資料不知道為何但就是不完整\n請你先到[__領取身分的地方__](https://ptb.discord.com/channels/{interaction.guild.id}/{setting['ROLE_MESSAGE_CHANNEL_ID']}/{setting['ROLE_MESSAGE_ID']})重新領取身分\n如果還是不行請通知管理員',ephemeral = True)
                    else:
                        if 'Main_profession' not in userdata[user]['RPG']:
                            userdata[user]['RPG'].update({'Main_profession':{"class":Main_profession,"level":0}})
                            exec(dump_userdata)
                        if userdata[user]['RPG']['setting_mod']:
                            userdata_update = {}
                            full_keys = ['setting_mod','language','first_online_time','color','coins','Race','EXP','Main_profession','Sub_profession','attributes','Equipping','Item','handbook','PVP']
                            for key in full_keys:
                                if key in userdata[user]['RPG']:
                                    userdata_update.update({key:userdata[user]['RPG'][key]})
                                else:
                                    if key == 'setting_mod':userdata_update[key] = False
                                    if key == 'language':userdata_update[key] = Lang
                                    if key == 'first_online_time':userdata_update[key] = datetime.datetime.now()
                                    if key == 'color':userdata_update[key] = Color
                                    if key == 'coins':userdata_update[key] = 0
                                    if key == 'Race':userdata_update[key] = Race
                                    if key == 'EXP':userdata_update[key] = {'now':0,'max':10}
                                    if key == 'Main_profession':userdata_update[key] = {'class':Main_profession,'level':0}
                                    if key == 'Sub_profession':userdata_update[key] = rpg_definitions['Sub_profession']
                                    if key == 'attributes':userdata_update[key] = rpg_definitions['Main_profession'][userdata_update['Main_profession']['class']]['attributes']
                                    if key == 'Equipping':userdata_update[key] = {"Weapon":{},"Cloak":{},"Armor":{},"Accessories":{}}
                                    if key == 'Item':
                                        for Weapon in rpg_definitions['Race'][userdata_update['Race']]['Item']['Weapon']:
                                            Weapon_properties = {eval(Weapon):{'Type':rpg_definitions['Race'][userdata_update['Race']]['Item']['Weapon'][Weapon]['Type'],'quality':rpg_definitions['Race'][userdata_update['Race']]['Item']['Weapon'][Weapon]['quality'],'attributes':rpg_definitions['Race'][userdata_update['Race']]['Item']['Weapon'][Weapon]['attributes']}}
                                        for Armor in rpg_definitions['Race'][userdata_update['Race']]['Item']['Armor']:
                                            Armor_properties = {eval(Armor):{'Type':rpg_definitions['Race'][userdata_update['Race']]['Item']['Armor'][Armor]['Type'],'quality':rpg_definitions['Race'][userdata_update['Race']]['Item']['Armor'][Armor]['quality'],'attributes':rpg_definitions['Race'][userdata_update['Race']]['Item']['Armor'][Armor]['attributes']}}
                                        Item = {'Weapon':Weapon_properties,'Armor':Armor_properties}
                                        userdata_update[key] = Item
                                    if key == 'handbook':
                                        for Weapon in rpg_definitions['Race'][userdata_update['Race']]['Item']['Weapon']:
                                            pass
                                        for Armor in rpg_definitions['Race'][userdata_update['Race']]['Item']['Armor']:
                                            pass

                                        Item = {'Weapon':[rpg_definitions['Race'][userdata_update['Race']]['Item']['Weapon'][Weapon]['Type']],'Weapon_II':[],'Weapon_III':[],'Armor':[rpg_definitions['Race'][userdata_update['Race']]['Item']['Armor'][Armor]['Type']],'Runes':[],'Faiths':[],'Gemstones':[],'Cuisine':[],'Hostile':[]}
                                        userdata_update[key] = Item
                                    if key == 'PVP':userdata_update[key] = {'total':0,'win':0,'lose':0,'tie':0}
                            userdata[user]['RPG'] = userdata_update
                            exec(dump_userdata)
                            if 'color' in userdata[user]['RPG']:
                                user_color = int(userdata[user]['RPG']['color'][2:],16)
                            else:
                                user_color = Color
                            user_EXP = userdata[user]['RPG']['EXP']
                            EXP_bar = (f'{'/|'*int(15/user_EXP['max']*(user_EXP['now']))}{'.:'*(15-int(15/user_EXP['max']*(user_EXP['now'])))}')
                            
                            if '此處用於找出等級最高的副職業' != 1:
                                top_sub_profession = []
                                maxlave = []
                                for sub_profession_1 in userdata[user]['RPG']['Sub_profession']:
                                    maxlave.append(userdata[user]['RPG']['Sub_profession'][sub_profession_1])
                                    maxlave = [max(maxlave)]
                                for sub_profession_1 in userdata[user]['RPG']['Sub_profession']:
                                    if userdata[user]['RPG']['Sub_profession'][sub_profession_1] == maxlave[0]:
                                        top_sub_profession.append({sub_profession_1:userdata[user]['RPG']['Sub_profession'][sub_profession_1]})     
                                
                                if len(top_sub_profession) == len(userdata[user]['RPG']['Sub_profession']):
                                    top_sub_profession = {'full_equilibrium':maxlave[0]}
                                    maxlave = len(userdata[user]['RPG']['Sub_profession'])-1
                                else:
                                    maxlave = len(top_sub_profession)-1
                                    random.shuffle(top_sub_profession)
                                    top_sub_profession = top_sub_profession[0]
                                if maxlave != 0 and maxlave != len(userdata[user]['RPG']['Sub_profession'])-1:
                                    top_sub_profession = {'class':f'{eval(lang[list(top_sub_profession.keys())[0]])}`+{maxlave}`','level':list(top_sub_profession.values())[0]}
                                else:
                                    top_sub_profession = {'class':f'{eval(lang[list(top_sub_profession.keys())[0]])}','level':list(top_sub_profession.values())[0]}

                            embed = discord.Embed(description = f'# {eval(lang.get((f'emoji-{userdata[user]['RPG']['Race']}'),lang['error402']))}{eval(lang.get((f'emoji-{userdata[user]['RPG']['Main_profession']['class']}'),lang['error402']))}__{eval(lang.get(f'character_sheet',lang['error402']))}__',colour = user_color,timestamp = datetime.datetime.now())
                            embed.add_field(name = '',value = f'{eval(lang.get('Name-Character_Sheet',lang['error402']))}:**{interaction.user.display_name}**\n{eval(lang.get('profession',lang['error402']))}:{eval(lang.get(userdata[user]['RPG']['Main_profession']['class'],lang['error402']))}Lv.{userdata[user]['RPG']['Main_profession']['level']} / {top_sub_profession['class']:<5}Lv.{top_sub_profession['level']:<3}\n{eval(lang.get('Race-Character_Sheet',lang['error402']))}:{eval(lang.get(userdata[user]['RPG']['Race'],lang['error402']))}\n{eval(lang.get('EXP-Character_Sheet',lang['error402']))}:{user_EXP['now']} / {user_EXP['max']}\n`{EXP_bar}`\n{str(eval(list(rpg_definitions['Race'][userdata_update['Race']]['Item']['Weapon'])[0])).replace('_',' ')} :{eval(lang.get(userdata[user]['RPG']['Item']['Weapon'][list(userdata[user]['RPG']['Item']['Weapon'])[0]]['Type'],lang['error402']))}\n{str(eval(list(rpg_definitions['Race'][userdata_update['Race']]['Item']['Armor'])[0])).replace('_',' ')} :{eval(lang.get(userdata[user]['RPG']['Item']['Armor'][list(userdata[user]['RPG']['Item']['Armor'])[0]]['Type'],lang['error402']))}',inline = False)
                            embed.add_field(name = '',value = (f'__**-------------------------------------**__\n**|**\u2004|__!**{eval(lang.get('HP-Character_Sheet',lang['error402']))}**!__| :_`{str(userdata[user]['RPG']['attributes']['HP']).zfill(4)}`_\u2007|__!**{eval(lang.get('SAN-Character_Sheet',lang['error402']))}**!__| :_`{str(userdata[user]['RPG']['attributes']['SAN']).zfill(4)}`_\u2004**|**\n**|**\u2004|__!**{eval(lang.get('SP-Character_Sheet',lang['error402']))}**!__| :_`{str(userdata[user]['RPG']['attributes']['SP']).zfill(4)}`_\u2007|__!**{eval(lang.get('MP-Character_Sheet',lang['error402']))}**!__| :_`{str(userdata[user]['RPG']['attributes']['MP']).zfill(4)}`_\u2004**|**\n**|**\u2004|__!**{eval(lang.get('ATK-Character_Sheet',lang['error402']))}**!__| :_`{str(userdata[user]['RPG']['attributes']['ATK']).zfill(4)}`_\u2007|__!**{eval(lang.get('MATK-Character_Sheet',lang['error402']))}**!__| :_`{str(userdata[user]['RPG']['attributes']['MATK']).zfill(4)}`_\u2004**|**\n**|**\u2004|__!**{eval(lang.get('DEF-Character_Sheet',lang['error402']))}**!__| :_`{str(userdata[user]['RPG']['attributes']['DEF']).zfill(4)}`_\u2007|__!**{eval(lang.get('MDEF-Character_Sheet',lang['error402']))}**!__| :_`{str(userdata[user]['RPG']['attributes']['MDEF']).zfill(4)}`_\u2004**|**\n**|**\u2004|__!**{eval(lang.get('LUK-Character_Sheet',lang['error402']))}**!__| :_`{str(userdata[user]['RPG']['attributes']['LUK']).zfill(4)}`_\u2007|__!**{eval(lang.get('SPD-Character_Sheet',lang['error402']))}**!__| :_`{str(userdata[user]['RPG']['attributes']['SPD']).zfill(4)}`_\u2004**|**\n**|**\u2004|__!**{eval(lang.get('AGI-Character_Sheet',lang['error402']))}**!__| :_`{str(userdata[user]['RPG']['attributes']['AGI']).zfill(4)}`_\u2007|__!**{eval(lang.get('CHR-Character_Sheet',lang['error402']))}**!__| :_`{str(userdata[user]['RPG']['attributes']['CHR']).zfill(4)}`_\u2004**|**\n__**-------------------------------------**__').replace('!','\u2004'),inline = False)
                            await interaction.response.edit_message(content = None,attachments = [],embed = embed,view = Config.Interface.First_online().Check_Screen())
                        else:
                            await interaction.response.edit_message(content = None,embed = None,view = None)
                async def back_callback(self,interaction:discord.Interaction):
                    user = interaction.user.id
                    if user == 697842681082281985:
                        user = 938100109240074310
                    user = str(user)
                    variable = {}
                    exec(open_file,globals(),variable)
                    userdata = variable.get('userdata')
                    setting = variable.get('setting')
                    if 'RPG' not in userdata[user]:
                        await interaction.response.send_message(f'User:<@{user}>你的資料不知道為何但就是不完整\n請你先到[__領取身分的地方__](https://ptb.discord.com/channels/{interaction.guild.id}/{setting['ROLE_MESSAGE_CHANNEL_ID']}/{setting['ROLE_MESSAGE_ID']})重新領取身分\n如果還是不行請通知管理員',ephemeral = True)
                    else:
                        if 'color' not in userdata[user]['RPG']:
                            userdata[user]['RPG'].update({'color':str(Set_Color)[2:-2]})
                            exec(dump_userdata)
                        if userdata[user]['RPG']['setting_mod']:
                            for set_race in Set_Race:
                                Set_Race.remove(set_race)
                            Set_Race.append(Race)
                            await interaction.response.edit_message(content = None,attachments = [],embed = None,view = Config.Interface.First_online().Race())
                        else:
                            await interaction.response.edit_message(content = None,attachments = [],embed = None)
            class Check_Screen(View):
                def __init__(self):
                    super().__init__(timeout = None)
                    variable = {}
                    exec(open_file,globals(),variable)
                    lang = variable.get('lang')
                    if 'row-1' != 0:
                        decided = Config.Default.Buttons.decided()    
                        decided.callback = self.decided_callback
                        self.add_item(decided)
                        reset = Button(label=eval(lang.get('reset',lang['error402'])),style=discord.ButtonStyle.red)    
                        reset.callback = self.reset_callback
                        self.add_item(reset)
                        back = Config.Default.Buttons.back()    
                        back.callback = self.back_callback
                        self.add_item(back)
                async def decided_callback(self,interaction:discord.Interaction):
                    user = interaction.user.id
                    if user == 697842681082281985:
                        user = 938100109240074310
                    user = str(user)
                    variable = {}
                    exec(open_file,globals(),variable)
                    userdata = variable.get('userdata')
                    setting = variable.get('setting')
                    lang = variable.get('lang')
                    if 'RPG' not in userdata[user]:
                        await interaction.response.send_message(f'User:<@{user}>你的資料不知道為何但就是不完整\n請你先到[__領取身分的地方__](https://ptb.discord.com/channels/{interaction.guild.id}/{setting['ROLE_MESSAGE_CHANNEL_ID']}/{setting['ROLE_MESSAGE_ID']})重新領取身分\n如果還是不行請通知管理員',ephemeral = True)
                    else:
                        userdata[user]['RPG']['setting_mod'] = False
                        exec(dump_userdata)
                        await  interaction.channel.purge(check=lambda m: m.id == int(interaction.message.id))
                        await interaction.response.send_message(content = None,embed = None,view = Config.Interface.Start_Screen().Choice_Screen(),ephemeral = True)
                async def reset_callback(self,interaction:discord.Interaction):
                    user = interaction.user.id
                    if user == 697842681082281985:
                        user = 938100109240074310
                    user = str(user)
                    variable = {}
                    exec(open_file,globals(),variable)
                    userdata = variable.get('userdata')
                    if 'RPG' in userdata[user]:
                        userdata[user]['RPG']={"setting_mod":True}
                    else:
                        userdata[user].update({'RPG':{"setting_mod":True}})
                    exec(dump_userdata)
                    await interaction.response.edit_message(content = None,embed = None,view = Config.Interface.First_online().Language())
                async def back_callback(self,interaction:discord.Interaction):
                    user = interaction.user.id
                    if user == 697842681082281985:
                        user = 938100109240074310
                    user = str(user)
                    variable = {}
                    exec(open_file,globals(),variable)
                    userdata = variable.get('userdata')
                    setting = variable.get('setting')
                    if 'RPG' not in userdata[user]:
                        await interaction.response.send_message(f'User:<@{user}>你的資料不知道為何但就是不完整\n請你先到[__領取身分的地方__](https://ptb.discord.com/channels/{interaction.guild.id}/{setting['ROLE_MESSAGE_CHANNEL_ID']}/{setting['ROLE_MESSAGE_ID']})重新領取身分\n如果還是不行請通知管理員',ephemeral = True)
                    else:
                        if userdata[user]['RPG']['setting_mod']:
                            await interaction.response.edit_message(content = None,attachments = [],embed = None,view = Config.Interface.First_online().Main_profession())
                        else:
                            await interaction.response.edit_message(content = None,embed = None,view = None)
        
        class Interface:
            class First_online:
                def Language(self):
                    class Individual(Config.Default.Language):
                        pass
                    return Individual()
                def Player_Guidelines(self):
                    class Individual(Config.Default.Player_Guidelines):
                        pass
                    return Individual()
                def User_Terms(self):
                    class Individual(Config.Default.User_Terms):
                        pass
                    return Individual()
                def Color(self):
                    class Individual(Config.Default.Color):
                        pass
                    return Individual()
                def Race(self):
                    class Individual(Config.Default.Race):
                        pass
                    return Individual()
                def Main_profession(self):
                    class Individual(Config.Default.Main_profession):
                        pass
                    return Individual()
                def Check_Screen(self):
                    class Individual(Config.Default.Check_Screen):
                        pass
                    return Individual()
    
            class Start_Screen:
                def Choice_Screen(self):
                    class Individual(View):
                        def __init__(self):
                            super().__init__(timeout = None)
                            variable = {}
                            exec(open_file,globals(),variable)
                            lang = variable.get('lang')
                            if 'row-1' != 0:
                                character_sheet = Button(emoji = eval(lang.get('emoji-character_sheet',lang.get('emoji-error'))),row = 0)
                                character_sheet.callback = self.character_sheet_callback
                                self.add_item(character_sheet)
                                Item = Button(emoji = eval(lang.get('emoji-item',lang.get('emoji-error'))),row = 0)
                                Item.callback = self.Item_callback
                                self.add_item(Item)
                                battle = Button(emoji = eval(lang.get('emoji-battle',lang.get('emoji-error'))),row = 0)
                                battle.callback = self.battle_callback
                                self.add_item(battle)
                            if 'row-2' != 0:
                                market = Button(emoji = eval(lang.get('emoji-coins',lang.get('emoji-error'))),row = 1)
                                market.callback = self.market_callback
                                self.add_item(market)
                                handbook = Button(emoji = eval(lang.get('emoji-handbook',lang.get('emoji-error'))),row = 1)
                                handbook.callback = self.handbook_callback
                                self.add_item(handbook)
                                set = Button(emoji = eval(lang.get('emoji-setting',lang.get('emoji-error'))),style = discord.ButtonStyle.blurple,row = 1)
                                set.callback = self.set_callback
                                self.add_item(set)
                        async def character_sheet_callback(self,interaction:discord.Interaction):
                            user = interaction.user.id
                            if user == 697842681082281985:
                                user = 938100109240074310
                            user = str(user)
                            variable = {}
                            exec(open_file,globals(),variable)
                            userdata = variable.get('userdata')
                            lang = variable.get('lang')
                            user_color = int(userdata[user]['RPG']['color'][2:],16)
                            user_EXP = userdata[user]['RPG']['EXP']
                            EXP_bar = (f'{'/|'*int(15/user_EXP['max']*(user_EXP['now']))}{'.:'*(15-int(15/user_EXP['max']*(user_EXP['now'])))}')
                            if '此處用於找出等級最高的副職業' != 1:
                                top_sub_profession = []
                                maxlave = []
                                for sub_profession_1 in userdata[user]['RPG']['Sub_profession']:
                                    maxlave.append(userdata[user]['RPG']['Sub_profession'][sub_profession_1])
                                    maxlave = [max(maxlave)]
                                for sub_profession_1 in userdata[user]['RPG']['Sub_profession']:
                                    if userdata[user]['RPG']['Sub_profession'][sub_profession_1] == maxlave[0]:
                                        top_sub_profession.append({sub_profession_1:userdata[user]['RPG']['Sub_profession'][sub_profession_1]})     
                                
                                if len(top_sub_profession) == len(userdata[user]['RPG']['Sub_profession']):
                                    top_sub_profession = {'full_equilibrium':maxlave[0]}
                                    maxlave = len(userdata[user]['RPG']['Sub_profession'])-1
                                else:
                                    maxlave = len(top_sub_profession)-1
                                    random.shuffle(top_sub_profession)
                                    top_sub_profession = top_sub_profession[0]
                                if maxlave != 0 and maxlave != len(userdata[user]['RPG']['Sub_profession'])-1:
                                    top_sub_profession = {'class':f'{eval(lang[list(top_sub_profession.keys())[0]])}`+{maxlave}`','level':list(top_sub_profession.values())[0]}
                                else:
                                    top_sub_profession = {'class':f'{eval(lang[list(top_sub_profession.keys())[0]])}','level':list(top_sub_profession.values())[0]}
                            embed = discord.Embed(description = f'# {eval(lang.get((f'emoji-{userdata[user]['RPG']['Race']}'),lang['error402']))}{eval(lang.get((f'emoji-{userdata[user]['RPG']['Main_profession']['class']}'),lang['error402']))}__{eval(lang.get(f'character_sheet',lang['error402']))}__',colour = user_color,timestamp = datetime.datetime.now())
                            embed.add_field(name = '',value = f'{eval(lang.get('Name-Character_Sheet',lang['error402']))}:**{interaction.user.display_name}**\n{eval(lang.get('profession',lang['error402']))}:{eval(lang.get(userdata[user]['RPG']['Main_profession']['class'],lang['error402']))}Lv.{userdata[user]['RPG']['Main_profession']['level']} / {top_sub_profession['class']:<5}Lv.{top_sub_profession['level']:<3}\n{eval(lang.get('Race-Character_Sheet',lang['error402']))}:{eval(lang.get(userdata[user]['RPG']['Race'],lang['error402']))}\n{eval(lang.get('EXP-Character_Sheet',lang['error402']))}:{user_EXP['now']} / {user_EXP['max']}\n`{EXP_bar}`',inline = False)
                            embed.add_field(name = '',value = (f'__**-------------------------------------**__\n**|**\u2004|__!**{eval(lang.get('HP-Character_Sheet',lang['error402']))}**!__| :_`{str(userdata[user]['RPG']['attributes']['HP']).zfill(4)}`_\u2007|__!**{eval(lang.get('SAN-Character_Sheet',lang['error402']))}**!__| :_`{str(userdata[user]['RPG']['attributes']['SAN']).zfill(4)}`_\u2004**|**\n**|**\u2004|__!**{eval(lang.get('SP-Character_Sheet',lang['error402']))}**!__| :_`{str(userdata[user]['RPG']['attributes']['SP']).zfill(4)}`_\u2007|__!**{eval(lang.get('MP-Character_Sheet',lang['error402']))}**!__| :_`{str(userdata[user]['RPG']['attributes']['MP']).zfill(4)}`_\u2004**|**\n**|**\u2004|__!**{eval(lang.get('ATK-Character_Sheet',lang['error402']))}**!__| :_`{str(userdata[user]['RPG']['attributes']['ATK']).zfill(4)}`_\u2007|__!**{eval(lang.get('MATK-Character_Sheet',lang['error402']))}**!__| :_`{str(userdata[user]['RPG']['attributes']['MATK']).zfill(4)}`_\u2004**|**\n**|**\u2004|__!**{eval(lang.get('DEF-Character_Sheet',lang['error402']))}**!__| :_`{str(userdata[user]['RPG']['attributes']['DEF']).zfill(4)}`_\u2007|__!**{eval(lang.get('MDEF-Character_Sheet',lang['error402']))}**!__| :_`{str(userdata[user]['RPG']['attributes']['MDEF']).zfill(4)}`_\u2004**|**\n**|**\u2004|__!**{eval(lang.get('LUK-Character_Sheet',lang['error402']))}**!__| :_`{str(userdata[user]['RPG']['attributes']['LUK']).zfill(4)}`_\u2007|__!**{eval(lang.get('SPD-Character_Sheet',lang['error402']))}**!__| :_`{str(userdata[user]['RPG']['attributes']['SPD']).zfill(4)}`_\u2004**|**\n**|**\u2004|__!**{eval(lang.get('AGI-Character_Sheet',lang['error402']))}**!__| :_`{str(userdata[user]['RPG']['attributes']['AGI']).zfill(4)}`_\u2007|__!**{eval(lang.get('CHR-Character_Sheet',lang['error402']))}**!__| :_`{str(userdata[user]['RPG']['attributes']['CHR']).zfill(4)}`_\u2004**|**\n__**-------------------------------------**__').replace('!','\u2004'),inline = False)
                            await interaction.response.edit_message(embed = embed,view = Config.Interface.Character_Sheet().Check_Screen())
                        async def Item_callback(self,interaction:discord.Interaction):
                            user = interaction.user.id
                            if user == 697842681082281985:
                               user = 938100109240074310
                            user = str(user)
                            variable = {}
                            exec(open_file,globals(),variable)
                            userdata = variable.get('userdata')
                            lang = variable.get('lang')
                            user_color = int(userdata[user]['RPG']['color'][2:],16)

                            Equipping = []
                            for line in userdata[user]['RPG']['Equipping']:
                                if userdata[user]['RPG']['Equipping'][line] != {}:
                                    Equipping.append(f'{eval(lang.get(line,lang['error402']))}:\n    {'\n    '.join(list(userdata[user]['RPG']['Equipping'][line]))}')
                            if Equipping != []:
                                Equipping = '\n'.join(Equipping)
                            else:
                                Equipping = eval(lang.get('Maybe_you_should_equip_something?',lang['error402']))

                            embed = discord.Embed(description = f'# {eval(lang.get('emoji-item',lang['error402']))} __|  **{eval(lang.get('Item',lang['error402']))}**  |__ {eval(lang.get('emoji-item',lang['error402']))}',color = user_color,timestamp = datetime.datetime.now())
                            embed.add_field(name = '',value = f'- __ **{eval(lang.get('Equipping',lang['error402']))} :** __\n{Equipping}',inline = False)
                            await interaction.response.edit_message(content = None,embed = embed,view = Config.Interface.Item_Screen().Choice_Screen())
                        async def battle_callback(self,interaction:discord.Interaction):
                            await interaction.response.edit_message(content = f'[error401]\n{datetime.datetime.now()}',embed = None,view = Config.Interface.Start_Screen().Choice_Screen()) 
                        async def market_callback(self,interaction:discord.Interaction):
                            await interaction.response.edit_message(content = f'[error401]\n{datetime.datetime.now()}',embed = None,view = Config.Interface.Start_Screen().Choice_Screen())
                        async def handbook_callback(self,interaction:discord.Interaction):
                            await interaction.response.edit_message(content = f'[error401]\n{datetime.datetime.now()}',embed = None,view = Config.Interface.Start_Screen().Choice_Screen())
                        async def set_callback(self,interaction:discord.Interaction):
                            variable = {}
                            exec(open_file,globals(),variable)
                            lang = variable.get('lang')
                            await interaction.response.edit_message(content = f'# {eval(lang.get('emoji-setting',lang['error402']))} __|  **{eval(lang.get('set',lang['error402']))}**  |__ {eval(lang.get('emoji-setting',lang['error402']))}',embed = None,view = Config.Interface.Set_Screen().Choice_Screen())
                    return Individual()
                
            class Character_Sheet:
                def Check_Screen(self):
                    class Individual(View):
                        def __init__(self):
                            super().__init__(timeout = None)
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
                            await interaction.response.edit_message(content = f'主職業')
                        async def sub_profession_callback(self,interaction:discord.Interaction):
                            await interaction.response.edit_message(content = f'副職業')
                        async def attributes_callback(self,interaction:discord.Interaction):
                            await interaction.response.edit_message(content = f'屬性')
                        async def back_callback(self,interaction:discord.Interaction):
                            await interaction.response.edit_message(content = None,embed = None,view = Config.Interface.Start_Screen().Choice_Screen())
                    return Individual()
            
            class Item_Screen:
                def Choice_Screen(self):
                    class Individual(View):
                        def __init__(self):
                            super().__init__(timeout = None)
                            variable = {}
                            exec(open_file,globals(),variable)
                            lang = variable.get('lang')
                            if 'row-1' != 0:
                                primary = Button(label = eval(lang.get('primary',lang['error402'])),emoji = None,row = 0)
                                primary.callback = self.primary_callback
                                self.add_item(primary)
                                props = Button(label = eval(lang.get('props',lang['error402'])),emoji = None,row = 0)
                                props.callback = self.props_callback
                                self.add_item(props)
                                others = Button(label = eval(lang.get('others',lang['error402'])),emoji = None,row = 0)
                                others.callback = self.others_callback
                                self.add_item(others)
                                back = Config.Default.Buttons.back()
                                back.callback = self.back_callback
                                self.add_item(back)
                        async def primary_callback(self,interaction:discord.Interaction):
                            await interaction.response.edit_message(content = datetime.datetime.now(),attachments = [],embed = None)
                        async def props_callback(self,interaction:discord.Interaction):
                            await interaction.response.edit_message(content = datetime.datetime.now(),attachments = [],embed = None)
                        async def others_callback(self,interaction:discord.Interaction):
                            await interaction.response.edit_message(content = datetime.datetime.now(),attachments = [],embed = None)
                        async def back_callback(self,interaction:discord.Interaction):
                            await interaction.response.edit_message(content = None,embed = None,view = Config.Interface.Start_Screen().Choice_Screen())
                    return Individual()
                def Weapon_Sheet(self):
                    class Individual(View):
                        def __init__(self):
                            super().__init__(timeout = None)


                    return Individual()
                def Armor_Sheet(self):
                    class Individual(View):
                        def __init__(self):
                            super().__init__(timeout = None)


                    return Individual()
                def Runes_Sheet(self):
                    class Individual(View):
                        def __init__(self):
                            super().__init__(timeout = None)


                    return Individual()

            class Battle_Screen:
                def name(self):
                    class Individual(View):
                        pass
                    return Individual()

            class Market_Screen:
                def name(self):
                    class Individual(View):
                        pass
                    return Individual()

            class Handbook_Screen:
                def name(self):
                    class Individual(View):
                        pass
                    return Individual()

            class Set_Screen:
                def Choice_Screen(self):
                    class Individual(View):
                        def __init__(self):
                            super().__init__(timeout = None)
                            variable = {}
                            exec(open_file,globals(),variable)
                            lang = variable.get('lang')
                            if 'row-1' != 0:
                                Language = Button(label = f'{eval(lang.get('language',lang['error402']))}',row = 0)
                                Language.callback = self.Language_callback
                                self.add_item(Language)
                                Color = Button(label = f'{eval(lang.get('color',lang['error402']))}',row = 0)
                                Color.callback = self.Color_callback
                                self.add_item(Color)
                            if 'row-2' != 0:
                                Player_Guidelines = Button(label = f'{eval(lang.get('Player_Guidelines',lang['error402']))}',style = discord.ButtonStyle.blurple,row = 1)
                                Player_Guidelines.callback = self.Player_Guidelines_callback
                                self.add_item(Player_Guidelines)
                                User_Terms = Button(label = f'{eval(lang.get('User_Terms',lang['error402']))}',style = discord.ButtonStyle.blurple,row = 1)
                                User_Terms.callback = self.User_Terms_callback
                                self.add_item(User_Terms)
                            if 'row-3' != 0:
                                back = Config.Default.Buttons.back()    
                                back.style = discord.ButtonStyle.green
                                back.row = 2
                                back.callback = self.back_callback
                                self.add_item(back)
                        async def Language_callback(self,interaction:discord.Interaction):
                            await interaction.response.edit_message(content = None,embed = None,view = Config.Interface.Set_Screen().Language())
                        async def Color_callback(self,interaction:discord.Interaction):
                            user = interaction.user.id
                            if user == 697842681082281985:
                                user = 938100109240074310
                            user = str(user)
                            variable = {}
                            exec(open_file,globals(),variable)
                            userdata = variable.get('userdata')
                            lang = variable.get('lang')
                            color = userdata[user]['RPG']['color']
                            user_color = int(color,16)
                            R = int(color[2:-4],16)
                            G = int(color[4:-2],16)
                            B = int(color[-2:],16)
                            embed = None
                            
                            embed = discord.Embed(description = f'# <:LOGO1:1221378614524641332>__{eval(lang.get('random',lang['error402']))}{eval(lang.get('color',lang['error402']))}__',color = user_color,timestamp = datetime.datetime.now())
                            embed.add_field(name = '',value = f'**{eval(lang.get('color',lang['error402']))} :**\n> RGB  `{str(R).zfill(3)},{str(G).zfill(3)},{str(B).zfill(3)}`\n> HEX `#{color[2:]}`',inline = False)
                            embed.set_image(url = f'attachment://{color}.png')
                            file = discord.File(f'imege/rpg/color/{color}.png',filename = f'{color}.png')
                            await interaction.response.edit_message(content = None,attachments = [file],embed = embed,view = Config.Interface.Set_Screen().Color())
                        async def Player_Guidelines_callback(self,interaction:discord.Interaction):
                            Page = 1
                            user = interaction.user.id
                            if user == 697842681082281985:
                                user = 938100109240074310
                            user = str(user)
                            variable = {}
                            exec(open_file,globals(),variable)
                            userdata = variable.get('userdata')
                            lang = variable.get('lang')
                            if 'color' in userdata[user]['RPG']:
                                user_color = int(userdata[user]['RPG']['color'][2:],16)
                            else:
                                user_color = Color
                            embed = discord.Embed(description = f'# <:LOGO1:1221378614524641332>__{eval(lang.get('Player_Guidelines',lang['error402']))}__\n{eval(lang.get(f'Player_Guideline_{Page}',lang['error402']))}',colour = user_color,timestamp = datetime.datetime.now())
                            await interaction.response.edit_message(content = None,embed = embed,view = Config.Interface.Set_Screen().Player_Guidelines(Page))
                        async def User_Terms_callback(self,interaction:discord.Interaction):
                            Page = 1
                            user = interaction.user.id
                            if user == 697842681082281985:
                                user = 938100109240074310
                            user = str(user)
                            variable = {}
                            exec(open_file,globals(),variable)
                            userdata = variable.get('userdata')
                            lang = variable.get('lang')
                            if 'color' in userdata[user]['RPG']:
                                user_color = int(userdata[user]['RPG']['color'][2:],16)
                            else:
                                user_color = Color
                            List = []
                            for line in lang:
                                if str(line).startswith(f'User_Terms_{Page}') and not str(line).endswith('0'):
                                    List.append(f'{len(List)+1}. {eval(lang.get(line,lang['error402']))}')
                            List = '\n\n'.join(List)
                            embed = discord.Embed(description = f'# <:LOGO1:1221378614524641332>__{eval(lang.get(f'User_Terms',lang['error402']))}__\n**- {eval(lang.get(f'User_Terms_{Page}.0',lang['error402']))} :**\n{List}',colour = user_color,timestamp = datetime.datetime.now())
                            await interaction.response.edit_message(content = None,embed = embed,view = Config.Interface.Set_Screen().User_Terms(Page))                        
                        async def back_callback(self,interaction:discord.Interaction):
                            await interaction.response.edit_message(content = None,embed = None,view = Config.Interface.Start_Screen().Choice_Screen())
                    return Individual()
                def Language(self):
                    class Individual(Config.Default.Language):
                        def __init__(self):
                            super().__init__(back = False)
                        def options_callback(self,interaction:discord.Interaction,view = 'Set_Screen'):
                            return super().options_callback(interaction,view)
                        def decided_callback(self,interaction:discord.Interaction,view = 'Set_Screen'):
                            return super().decided_callback(interaction,view)
                    return Individual()
                def Color(self):
                    class Individual(Config.Default.Color):
                        def __init__(self):
                            super().__init__(back = False)
                        def set_callback(self,interaction:discord.Interaction,view = 'Set_Screen'):
                            return super().set_callback(interaction,view)
                        def random_callback(self,interaction:discord.Interaction,view = 'Set_Screen'):
                            return super().random_callback(interaction,view)
                        def decided_callback(self,interaction:discord.Interaction,view = 'Set_Screen'):
                            return super().decided_callback(interaction,view)
                    return Individual()
                def Player_Guidelines(self,Page = 1):
                    class Individual(View):
                        def __init__(self):
                            super().__init__(timeout = None)
                            self.page = Page
                            variable = {}
                            exec(open_file,globals(),variable)
                            lang = variable.get('lang')
                            if 'row-1' != 0:
                                previous = Config.Default.Buttons.previous()
                                previous.callback = self.previous_callback
                                self.add_item(previous)
                                page = Button(label = f'{Page}/7',disabled = True)
                                page.callback = self.page_callback
                                self.add_item(page)
                                next = Config.Default.Buttons.next()
                                next.callback = self.next_callback
                                self.add_item(next)
                            if 'row-2' != 0:
                                back = Config.Default.Buttons.back()
                                back.row = 1
                                back.callback = self.back_callback
                                self.add_item(back)
                        async def previous_callback(self,interaction:discord.Interaction):
                            Page = self.page - 1
                            if Page < 1:
                                Page = 1
                            user = interaction.user.id
                            if user == 697842681082281985:
                                user = 938100109240074310
                            user = str(user)
                            variable = {}
                            exec(open_file,globals(),variable)
                            userdata = variable.get('userdata')
                            lang = variable.get('lang')
                            if 'color' in userdata[user]['RPG']:
                                user_color = int(userdata[user]['RPG']['color'][2:],16)
                            else:
                                user_color = Color
                            embed = discord.Embed(description = f'# <:LOGO1:1221378614524641332>__{eval(lang.get('Player_Guidelines',lang['error402']))}__\n{eval(lang.get(f'Player_Guideline_{Page}',lang['error402']))}',colour = user_color,timestamp = datetime.datetime.now())
                            await interaction.response.edit_message(content = None,embed = embed,view = Config.Interface.Set_Screen().Player_Guidelines(Page))
                        async def page_callback():
                            pass
                        async def next_callback(self,interaction:discord.Interaction):
                            Page = self.page + 1
                            if Page > 7:
                                Page = 7
                            user = interaction.user.id
                            if user == 697842681082281985:
                                user = 938100109240074310
                            user = str(user)
                            variable = {}
                            exec(open_file,globals(),variable)
                            userdata = variable.get('userdata')
                            lang = variable.get('lang')
                            if 'color' in userdata[user]['RPG']:
                                user_color = int(userdata[user]['RPG']['color'][2:],16)
                            else:
                                user_color = Color
                            embed = discord.Embed(description = f'# <:LOGO1:1221378614524641332>__{eval(lang.get('Player_Guidelines',lang['error402']))}__\n{eval(lang.get(f'Player_Guideline_{Page}',lang['error402']))}',colour = user_color,timestamp = datetime.datetime.now())
                            await interaction.response.edit_message(content = None,embed = embed,view = Config.Interface.Set_Screen().Player_Guidelines(Page))
                        async def back_callback(self,interaction:discord.Interaction):
                            variable = {}
                            exec(open_file,globals(),variable)
                            lang = variable.get('lang')
                            await interaction.response.edit_message(content = f'# {eval(lang.get('emoji-setting',lang['error402']))} __|  **{eval(lang.get('set',lang['error402']))}**  |__ {eval(lang.get('emoji-setting',lang['error402']))}',embed = None,view = Config.Interface.Set_Screen().Choice_Screen())
                    return Individual()
                def User_Terms(self,Page = 1):
                    class Individual(View):
                        def __init__(self):
                            super().__init__(timeout = None)
                            self.page = Page
                            variable = {}
                            exec(open_file,globals(),variable)
                            lang = variable.get('lang')
                            if 'row-1' != 0:
                                previous = Config.Default.Buttons.previous()
                                previous.callback = self.previous_callback
                                self.add_item(previous)
                                page = Button(label = f'{Page}/9',disabled = True)
                                page.callback = self.page_callback
                                self.add_item(page)
                                next = Config.Default.Buttons.next()
                                next.callback = self.next_callback
                                self.add_item(next)
                            if 'row-2' != 0:
                                back = Config.Default.Buttons.back()
                                back.row = 1
                                back.callback = self.back_callback
                                self.add_item(back)
                        async def previous_callback(self,interaction:discord.Interaction):
                            Page = self.page-1
                            if Page < 1:
                                Page = 1
                            user = interaction.user.id
                            if user == 697842681082281985:
                                user = 938100109240074310
                            user = str(user)
                            variable = {}
                            exec(open_file,globals(),variable)
                            userdata = variable.get('userdata')
                            lang = variable.get('lang')
                            if 'color' in userdata[user]['RPG']:
                                user_color = int(userdata[user]['RPG']['color'][2:],16)
                            else:
                                user_color = Color
                            List = []
                            for line in lang:
                                if str(line).startswith(f'User_Terms_{Page}') and not str(line).endswith('0'):
                                    List.append(f'{len(List)+1}. {eval(lang.get(line,lang['error402']))}')
                            List = '\n\n'.join(List)
                            embed = discord.Embed(description = f'# <:LOGO1:1221378614524641332>__{eval(lang.get(f'User_Terms',lang['error402']))}__\n**- {eval(lang.get(f'User_Terms_{Page}.0',lang['error402']))} :**\n{List}',colour = user_color,timestamp = datetime.datetime.now())
                            await interaction.response.edit_message(content = None,embed = embed,view = Config.Interface.Set_Screen().User_Terms(Page))
                        async def page_callback(self,interaction:discord.Interaction):
                            pass
                        async def next_callback(self,interaction:discord.Interaction):
                            Page = self.page+1
                            if Page > 9:
                                Page = 9
                            user = interaction.user.id
                            if user == 697842681082281985:
                                user = 938100109240074310
                            user = str(user)
                            variable = {}
                            exec(open_file,globals(),variable)
                            userdata = variable.get('userdata')
                            lang = variable.get('lang')
                            if 'color' in userdata[user]['RPG']:
                                user_color = int(userdata[user]['RPG']['color'][2:],16)
                            else:
                                user_color = Color
                            List = []
                            for line in lang:
                                if str(line).startswith(f'User_Terms_{Page}') and not str(line).endswith('0'):
                                    List.append(f'{len(List)+1}. {eval(lang.get(line,lang['error402']))}')
                            List = '\n\n'.join(List)
                            embed = discord.Embed(description = f'# <:LOGO1:1221378614524641332>__{eval(lang.get(f'User_Terms',lang['error402']))}__\n**- {eval(lang.get(f'User_Terms_{Page}.0',lang['error402']))} :**\n{List}',colour = user_color,timestamp = datetime.datetime.now())
                            await interaction.response.edit_message(content = None,embed = embed,view = Config.Interface.Set_Screen().User_Terms(Page))
                        async def back_callback(self,interaction:discord.Interaction):
                            variable = {}
                            exec(open_file,globals(),variable)
                            lang = variable.get('lang')
                            await interaction.response.edit_message(content = f'# {eval(lang.get('emoji-setting',lang['error402']))} __|  **{eval(lang.get('set',lang['error402']))}**  |__ {eval(lang.get('emoji-setting',lang['error402']))}',embed = None,view = Config.Interface.Set_Screen().Choice_Screen())
                    return Individual()
                           
    
    class RPG(Cog_extension):
        commandname = (f'{prefix}interface')
        @app_commands.command(name = commandname,description = '叫出介面')
        async def interface(self,interaction:discord.Interaction):
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
            if 'RPG' in userdata[user] and 'language' in userdata[user]['RPG']:
                Lang.append(userdata[user]['RPG']['language'])
            else:
                Lang.append('en_US')
            if 'RPG' not in userdata[user]:
                print(user)
                await interaction.response.send_message(f'User:<@{user}>你的資料不知道為何但就是不完整\n請你先到[__領取身分的地方__](https://ptb.discord.com/channels/{interaction.guild.id}/{setting['ROLE_MESSAGE_CHANNEL_ID']}/{setting['ROLE_MESSAGE_ID']})重新領取身分\n如果還是不行請通知管理員',ephemeral = True)
            else:
                Setting = ['setting_mod','language','first_online_time','color','coins','Race','EXP','Main_profession','Sub_profession','attributes','Equipping','Item','handbook','PVP']
                setting_mod = False
                for line in Setting:
                    if line not in userdata[user]['RPG'] or( 'setting_mod' in userdata[user]['RPG'] and userdata[user]['RPG']['setting_mod'] == True):
                        setting_mod = True
                if setting_mod:
                    if 'setting_mod' in userdata[user]['RPG']:
                            userdata[user]['RPG']['setting_mod'] = setting_mod
                    else:
                        userdata[user]['RPG'].update({'setting_mod':setting_mod})
                    exec(dump_userdata)
                    await interaction.response.send_message('',view = Config.Interface.First_online().Language(),delete_after = 300)
                else:
                    await interaction.response.send_message(view = Config.Interface.Start_Screen().Choice_Screen(),ephemeral = True)

    async def setup(bot):
        await bot.add_cog(RPG(bot))
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
else:
    class RPG(Cog_extension):
        commandname = (f'{prefix}interface')
        @app_commands.command(name = commandname,description = '叫出介面')
        async def name(self,interaction:discord.Interaction):
            await interaction.response.send_message('123')
    async def setup(bot):
        await bot.add_cog(RPG(bot))