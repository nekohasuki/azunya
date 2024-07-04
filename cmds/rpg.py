import discord
from discord.ext import commands
from discord import app_commands
from discord.ui import Button, View

from core.classes import Cog_extension
prefix = 'rpg-'
Test_mod = True
#      True or False


if Test_mod == True:
    class Button_config(View):
        class name(View):
            #code......
            pass

        class name(View):
            #code......
            pass

        class name(View):
            #code......
            pass

        class name(View):
            #code......
            pass

        class name(View):
            #code......
            pass

        class Character_Sheet(View):
            def __init__(self):
                super().__init__()
                main_profession_button =Button(label='主職業')
                main_profession_button.callback = self.main_profession_button_callback
                self.add_item(main_profession_button)
                sub_profession_button =Button(label='副職業')
                sub_profession_button.callback = self.sub_profession_button_callback
                self.add_item(sub_profession_button)
                attributes_button =Button(label='屬性')
                attributes_button.callback = self.attributes_button_callback
                self.add_item(attributes_button)
            async def main_profession_button_callback(self,interaction:discord.Interaction):
                await interaction.response.send_message(f'主職業')
            async def sub_profession_button_callback(self,interaction:discord.Interaction):
                await interaction.response.send_message(f'副職業')
            async def attributes_button_callback(self,interaction:discord.Interaction):
                await interaction.response.send_message(view=Button_config.Character_Sheet())
    Race = '月兔'
    EXP={"now":0,"max":10}
    main_profession = {"class":"盜賊","level":0}
    sub_profession = {"class":"花匠","level":0}
    class RPG(Cog_extension):
        commandname = (f'{prefix}interface')
        @app_commands.command(name = commandname, description = '叫出介面')
        async def interface(self,interaction:discord.Interaction):
            await interaction.channel.send(f'```{interaction.user.display_name}・{main_profession['class']} Lv.{main_profession['level']}/{sub_profession['class']} Lv.{sub_profession['level']}\n種族 : {Race}　　EXP : {EXP['now']}/{EXP['max']}\n---------------------------\n(attributes is Null)```',view = Button_config.Character_Sheet())
    async def setup(bot):
        await bot.add_cog(RPG(bot))
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
elif Test_mod == False:
    class RPG(Cog_extension):
        pass
    async def setup(bot):
        await bot.add_cog(RPG(bot))