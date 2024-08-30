import discord
from discord.ext import commands
from discord import app_commands
from discord.ui import Button, View

from core.classes import Cog_extension

import asyncio,datetime
prefix = 'rpg-'
Test_mod = True
#      True or False


# /////////////////////////////////////////////////////////////////////////////////////////////////////////////
Race = '月兔'
EXP={'now':0,'max':10}
EXP_bar=['/|','/|','/|','/|','/|','.:','.:','.:','.:','.:','.:','.:','.:','.:','.:']
main_profession = {'class':'盜賊','level':0}
sub_profession = {'class':'花匠','level':0}
Character_Sheet = '角色卡'
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////


if Test_mod == True:
    class Button_config:
        class Start_Screen(View):
            def __init__(self):
                super().__init__(timeout=None)
                Character_Sheet_button = Button(label=Character_Sheet)
                Character_Sheet_button.callback = self.Character_Sheet_button_callback
                self.add_item(Character_Sheet_button)
            async def Character_Sheet_button_callback(self,interaction:discord.Interaction):
                embed = discord.Embed(description=f'# <:LOGO1:1221378614524641332>__{Character_Sheet}__',colour=0x00b0f4,timestamp=datetime.datetime.now())
                embed.add_field(name='',value=f'{'名稱':<3}: **{interaction.user.display_name}**\n{'職業':<3}: {main_profession['class']:<5}Lv.{main_profession['level']:<3}{'/':<2}{sub_profession['class']:<4}Lv.{sub_profession['level']:<5}\n{'種族':<3}: {Race}\n{'EXP':<4}: {EXP['now']} / {EXP['max']}\n`{str(EXP_bar)[1:-1].replace(',','').replace(' ','').replace("'",'')}`',inline=False)
                embed.add_field(name='__**-------------------------------------**__',value=(f'|!__**H~P**__!| :_`{200:>4}`_\u3000|!__**S!A!N**__!| :_`{0:>4}`_\u3000\n|!__**S~P**__!| :_`{0:>4}`_\u3000|!__**M~P**__!| :_`{0:>4}`_\u3000\n|!__**A!T!K**__!| :_`{0:>4}`_\u3000|!__**MATK**__!| :_`{0:>4}`_\u3000\n|!__**D!E!F**__!| :_`{0:>4}`_\u3000|!__**MDEF**__!| :_`{0:>4}`_\u3000\n|!__**L!U!K**__!| :_`{0:>4}`_\u3000|!__**S!P!D**__!| :_`{0:>4}`_\u3000\n|!__**A!G!\u200BI\u2009**__!| :_`{0:>4}`_\u3000|!__**C!H!R**__!| :_`{0:>4}`_\u3000').replace('~','\u2009\u3000').replace('!','\u200A\u2004').replace(' ','\u2007\u200A'),inline=False)
                await interaction.response.edit_message(embed=embed,view=Button_config.Character_Sheet())

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

        class name(View):
            def __init__(self):
                super().__init__(timeout=None)
                back_button = Button(label='返回',style=discord.ButtonStyle.red)
                back_button.callback = self.back_button_callback
                self.add_item(back_button)
            async def back_button_callback(self,interaction:discord.Interaction):
                await interaction.response.edit_message('',view=Button_config.Start_Screen())

        class name(View):
            def __init__(self):
                super().__init__(timeout=None)
                back_button = Button(label='返回',style=discord.ButtonStyle.red)
                back_button.callback = self.back_button_callback
                self.add_item(back_button)
            async def back_button_callback(self,interaction:discord.Interaction):
                await interaction.response.edit_message('',view=Button_config.Start_Screen())

        class name(View):
            def __init__(self):
                super().__init__(timeout=None)
                back_button = Button(label='返回',style=discord.ButtonStyle.red)
                back_button.callback = self.back_button_callback
                self.add_item(back_button)
            async def back_button_callback(self,interaction:discord.Interaction):
                await interaction.response.edit_message('',view=Button_config.Start_Screen())

        class name(View):
            def __init__(self):
                super().__init__(timeout=None)
                back_button = Button(label='返回',style=discord.ButtonStyle.red)
                back_button.callback = self.back_button_callback
                self.add_item(back_button)
            async def back_button_callback(self,interaction:discord.Interaction):
                await interaction.response.edit_message('',view=Button_config.Start_Screen())

        class name(View):
            def __init__(self):
                super().__init__(timeout=None)
                back_button = Button(label='返回',style=discord.ButtonStyle.red)
                back_button.callback = self.back_button_callback
                self.add_item(back_button)
            async def back_button_callback(self,interaction:discord.Interaction):
                await interaction.response.edit_message('',view=Button_config.Start_Screen())

        class name(View):
            def __init__(self):
                super().__init__(timeout=None)
                back_button = Button(label='返回',style=discord.ButtonStyle.red)
                back_button.callback = self.back_button_callback
                self.add_item(back_button)
            async def back_button_callback(self,interaction:discord.Interaction):
                await interaction.response.edit_message('',view=Button_config.Start_Screen())

        class name(View):
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

    class RPG(Cog_extension):
        commandname = (f'{prefix}interface')
        @app_commands.command(name = commandname, description = '叫出介面')
        async def interface(self,interaction:discord.Interaction):
            test = 'No'
            #A or B or No
            if test =='No':
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