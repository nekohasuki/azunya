import discord
from discord.ext import commands
from discord import app_commands
import json
import random,numpy

prefix = 'r-'

test = False
#      True or False
if test == False:
    from core.classes import Cog_extension
    class RPG(Cog_extension):
        pass
    async def setup(bot):
        await bot.add_cog(RPG(bot))
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
elif test == True:
    if '這裡是' != '職業基礎屬性':
    #'戰士'
        Warrior_hp =15
        Warrior_atk=10
        Warrior_def=6
        Warrior_spd=2
        Warrior_luk=2
    #'弓箭手'
        Archer_hp =6
        Archer_atk=8
        Archer_def=6
        Archer_spd=10
        Archer_luk=5
    #'盜賊'
        # Rogue_hp =10
        # Rogue_atk=7
        # Rogue_def=5
        # Rogue_spd=8
        # Rogue_luk=(0)#?
    #'盾兵'
        Shielder_hp =6
        Shielder_atk=8
        Shielder_def=6
        Shielder_spd=10
        Shielder_luk=5
    class RPG():
        with open('cmds\\data\\user_data.json' , 'r' , encoding='utf8') as userdata_file:
            userdata = json.load(userdata_file)
        A_user = '938100109240074310'
        B_user = '697842681082281985'
        if 'RPG' in userdata[A_user] and 'RPG' in userdata[B_user]:
            if userdata[A_user]['RPG']['Race'] == None:
                print('您尚未建置檔案')
            elif userdata[B_user]['RPG']['Race'] == None:
                print('對方尚未建置檔案')
            else:
            #抓取角色能力數值
                msg = []
                A_user_name = userdata[A_user]['display_name']
                A_user_Race = userdata[A_user]['RPG']['Race']
                A_user_Character = userdata[A_user]['RPG']['Character']
                A_user_Hp  = userdata[A_user]['RPG']['Hp']
                A_user_Atk = userdata[A_user]['RPG']['Atk']
                A_user_Def = userdata[A_user]['RPG']['Def']
                A_user_Spd = userdata[A_user]['RPG']['Spd']
                A_user_Luk = userdata[A_user]['RPG']['Luk']

                B_user_name = userdata[B_user]['display_name']
                B_user_Race = userdata[B_user]['RPG']['Race']
                B_user_Character = userdata[B_user]['RPG']['Character']
                B_user_Hp  = userdata[B_user]['RPG']['Hp']
                B_user_Atk = userdata[B_user]['RPG']['Atk']
                B_user_Def = userdata[B_user]['RPG']['Def']
                B_user_Spd = userdata[B_user]['RPG']['Spd']
                B_user_Luk = userdata[B_user]['RPG']['Luk']
                if '這裡是' != '種族運算':
                    pass
                if '這裡是' != '職業運算':
                    if A_user_Character == 'Archer':
                        A_hp =Archer_hp + (A_user_Hp)
                        A_atk=Archer_atk + (A_user_Atk)
                        A_def=Archer_def + (A_user_Def)
                        A_spd=Archer_spd + (A_user_Spd)
                        A_luk=Archer_luk + (A_user_Luk)
                    elif A_user_Character == 'Shielder':
                        A_hp =Shielder_hp + (A_user_Hp)
                        A_atk=Shielder_atk + (A_user_Atk)
                        A_def=Shielder_def + (A_user_Def)
                        A_spd=Shielder_spd + (A_user_Spd)
                        A_luk=Shielder_luk + (A_user_Luk)
                    elif A_user_Character == 'Warrior':
                        A_hp =Warrior_hp + (A_user_Hp)
                        A_atk=Warrior_atk + (A_user_Atk)
                        A_def=Warrior_def + (A_user_Def)
                        A_spd=Warrior_spd + (A_user_Spd)
                        A_luk=Warrior_luk + (A_user_Luk)
                    if B_user_Character == 'Archer':
                        B_hp =Archer_hp + (B_user_Hp)
                        B_atk=Archer_atk + (B_user_Atk)
                        B_def=Archer_def + (B_user_Def)
                        B_spd=Archer_spd + (B_user_Spd)
                        B_luk=Archer_luk + (B_user_Luk)
                    elif B_user_Character == 'Shielder':
                        B_hp =Shielder_hp + (B_user_Hp)
                        B_atk=Shielder_atk + (B_user_Atk)
                        B_def=Shielder_def + (B_user_Def)
                        B_spd=Shielder_spd + (B_user_Spd)
                        B_luk=Shielder_luk + (B_user_Luk)
                    elif B_user_Character == 'Warrior':
                        B_hp =Warrior_hp + (B_user_Hp)
                        B_atk=Warrior_atk + (B_user_Atk)
                        B_def=Warrior_def + (B_user_Def)
                        B_spd=Warrior_spd + (B_user_Spd)
                        B_luk=Warrior_luk + (B_user_Luk)
                if '這裡是' != '裝備運算':
                    pass
                if '這裡是' != '戰鬥模擬':
                    A=A_spd
                    B=B_spd
                    A_spd=(10/(A+B)*A)
                    B_spd=(10/(A+B)*B)
                    if A_spd <0.5 or B_spd <0.5:
                        A_spd=A_spd+.5
                        B_spd=B_spd+.5
                    while True:
                        if A_spd <= 1 or B_spd <=1:
                            break
                        else:
                            A_spd=A_spd/2
                            B_spd=B_spd/2
                    A_spd = int((str(numpy.round(A_spd+0.001)))[:-2])
                    B_spd = int((str(numpy.round(B_spd+0.001)))[:-2])
                    msg.append(f'**{A_user_name}**向**{B_user_name}**發起挑戰\n攻擊頻率為{A_spd} : {B_spd}\n----------------------------------------------------\n')

                    if A_spd > B_spd:
                        A_USER=A_user_name
                        A_HP =A_hp
                        A_ATK=A_atk
                        A_DEF=A_def
                        A_SPD=A_spd
                        A_LUK=A_luk

                        B_USER=B_user_name
                        B_HP =B_hp
                        B_ATK=B_atk
                        B_DEF=B_def
                        B_SPD=B_spd
                        B_LUK=B_luk
                    elif A_spd < B_spd:
                        A_USER=A_user_name
                        A_HP =B_hp
                        A_ATK=B_atk
                        A_DEF=B_def
                        A_SPD=B_spd
                        A_LUK=B_luk

                        B_USER=B_user_name
                        B_HP =A_hp
                        B_ATK=A_atk
                        B_DEF=A_def
                        B_SPD=A_spd
                        B_LUK=A_luk
                    else:
                        random_user=random.choice(['A','B'])
                        if random_user == 'A':
                            A_USER=A_user_name
                            A_HP =A_hp
                            A_ATK=A_atk
                            A_DEF=A_def
                            A_SPD=A_spd
                            A_LUK=A_luk

                            B_USER=B_user_name
                            B_HP =B_hp
                            B_ATK=B_atk
                            B_DEF=B_def
                            B_SPD=B_spd
                            B_LUK=B_luk
                        else:
                            A_USER=B_user_name
                            A_HP =B_hp
                            A_ATK=B_atk
                            A_DEF=B_def
                            A_SPD=B_spd
                            A_LUK=B_luk

                            B_USER=A_user_name
                            B_HP =A_hp
                            B_ATK=A_atk
                            B_DEF=A_def
                            B_SPD=A_spd
                            B_LUK=A_luk
                    A_LUK_gap=(A_LUK-B_LUK)*10
                    B_LUK_gap=(B_LUK-A_LUK)*10
                    A_LUK_gap_II = 0
                    B_LUK_gap_II = 0
                    if A_LUK_gap < -100:
                        A_LUK_gap = 0
                        A_LUK_gap_II = -1
                    else:
                        while A_LUK_gap > 100:
                            A_LUK_gap -= 100
                            A_LUK_gap_II += 1
                    if B_LUK_gap < -100:
                        B_LUK_gap = 0
                        B_LUK_gap_II = -1
                    else:
                        while B_LUK_gap > 100:
                            B_LUK_gap -= 100
                            B_LUK_gap_II += 1
                    counter = 0
                    max_battle_count=(2**2**2**2)/2-1
                    record_count=10
                    msg_battle=[]
                    print(f'\n\n\n')

                    while counter <max_battle_count and A_HP >0 and B_HP>0:
                        counter +=1
                        A=A_SPD
                        B=B_SPD
                        msg_battle.append(f'- 第{counter}次戰鬥\n')
                        if counter > record_count:
                            msg_battle=msg_battle[1:]
                            while A >0:
                                A-=1
                                msg_battle=msg_battle[1:]
                                while B >0:
                                    B-=1
                                    msg_battle=msg_battle[1:]     
                        A=A_SPD
                        B=B_SPD
                        while A >0 and A_HP >0 and B_HP>0:
                            A-=1
                            atk_event = random.randrange(1,100)
                            if A_LUK_gap > 0:
                                A_ATK_I=A_ATK
                                if A_LUK_gap >= atk_event:
                                    A_ATK_I=(A_ATK+(A_ATK*0.2))
                                if A_LUK_gap_II > 0:
                                    A_ATK_II=(A_ATK_I+(A_ATK*(0.2*A_LUK_gap_II)))
                                else:
                                    A_ATK_II=A_ATK_I
                            elif A_LUK_gap <= atk_event*-1 or A_LUK_gap_II < 0:
                                A_ATK_II=A_ATK*.75
                            else:
                                A_ATK_II=A_ATK
                            Damage = numpy.round(A_ATK_II-B_DEF,2)
                            if Damage <0:
                                Damage = 0
                            B_HP -= Damage
                            if B_HP < 0:
                                B_HP =0
                            if A_LUK_gap >= atk_event:
                                msg_battle.append(f'{A_USER}打出了{A_LUK_gap_II+1}階爆擊，一共對{B_USER}造成了{Damage}點傷害\n {B_USER}的血量剩餘 : {B_HP}\n')
                            elif A_LUK_gap_II > 0:
                                msg_battle.append(f'{A_USER}打出了{A_LUK_gap_II}階爆擊，一共對{B_USER}造成了{Damage}點傷害\n {B_USER}的血量剩餘 : {B_HP}\n')
                            elif A_LUK_gap <= atk_event*-1 or A_LUK_gap_II < 0:
                                msg_battle.append(f'{A_USER}手滑了,對{B_USER}造成了{Damage}點傷害\n {B_USER}的血量剩餘 : {B_HP}\n')
                            else:
                                msg_battle.append(f'{A_USER}對{B_USER}造成了{Damage}點傷害\n {B_USER}的血量剩餘 : {B_HP}\n')

                            while B >0 and A_HP>0 and B_HP>0:
                                B-=1
                                atk_event = random.randrange(1,100)
                                if B_LUK_gap > 0:
                                    B_ATK_I=B_ATK
                                    if B_LUK_gap >= atk_event:
                                        B_ATK_I=(B_ATK+(B_ATK*0.2))
                                    if B_LUK_gap_II > 0:
                                        B_ATK_II=(B_ATK_I+(B_ATK*(0.2*B_LUK_gap_II)))
                                    else:
                                        B_ATK_II=B_ATK_I
                                elif B_LUK_gap <= atk_event*-1 or B_LUK_gap_II < 0:
                                    B_ATK_II=B_ATK*.75
                                else:
                                    B_ATK_II=B_ATK
                                Damage = numpy.round(B_ATK_II-A_DEF,2)
                                if Damage <0:
                                    Damage = 0
                                A_HP -= Damage
                                if A_HP < 0:
                                    A_HP =0
                                if B_LUK_gap >= atk_event:
                                    msg_battle.append(f'{B_USER}打出了{B_LUK_gap_II+1}階爆擊，一共對{A_USER}造成了{Damage}點傷害\n {A_USER}的血量剩餘 : {A_HP}\n')
                                elif B_LUK_gap_II > 0:
                                    msg_battle.append(f'{B_USER}打出了{B_LUK_gap_II}階爆擊，一共對{A_USER}造成了{Damage}點傷害\n {A_USER}的血量剩餘 : {A_HP}\n')
                                elif B_LUK_gap <= atk_event*-1 or B_LUK_gap_II < 0:
                                    msg_battle.append(f'{B_USER}手滑了,對{A_USER}造成了{Damage}點傷害\n {A_USER}的血量剩餘 : {A_HP}\n')
                                else:
                                    msg_battle.append(f'{B_USER}對{A_USER}造成了{Damage}點傷害\n {A_USER}的血量剩餘 : {A_HP}\n')
                    if A_HP == 0:
                        msg_battle.append(f'----------------------------------------------------\n{A_USER}先攻\n{B_USER}勝利')
                    elif B_HP == 0:
                        msg_battle.append(f'----------------------------------------------------\n{A_USER}先攻\n{A_USER}勝利')
                    else:
                        msg_battle.append(f'----------------------------------------------------\n{A_USER}先攻\n由於戰鬥回合數達到{max_battle_count}次，本場自動作廢')
            msg.append(msg_battle)




            print(str(msg).replace('[','').replace(']','').replace("'",'').replace('\\n','\n').replace(', ',''))

        else:
            print('未知錯誤')


# # MATK/ATK 以裝備決定














    async def setup(bot):
        await bot.run(RPG)