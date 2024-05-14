import numpy, random

A_user = '戰士'
A_hp =(15+0)*10
A_atk=10 +0
A_def=6 +0
A_spd=2 +0
A_luk=2 +0

# A_user = '盜賊'
# A_hp =(10+0)*10
# A_atk=7 +0
# A_def=5 +0
# A_spd=8 +0
# A_luk=10 +0


# A_user = '坦克'
# A_hp =(16+0)*10
# A_atk=8 +0
# A_def=9 +0
# A_spd=1 +0
# A_luk=1 +0

B_user = '弓箭手'
B_hp =(6+0)*10
B_atk=8 +0
B_def=6 +0
B_spd=10 +0
B_luk=5 +0

# B_user = '戰士'
# B_hp =(15+0)*10
# B_atk=10 +0
# B_def=6 +0
# B_spd=2 +0
# B_luk=2 +0
#-----------------------------------------------------
A=A_spd
B=B_spd
A_spd=(10/(A+B)*A)
B_spd=(10/(A+B)*B)
if A_spd <0.5 or B_spd <0.5:
    print(f'{A_spd} : {B_spd}')
    A_spd=A_spd+.5
    B_spd=B_spd+.5
while True:
    print(f'{A_spd} : {B_spd}')
    if A_spd <= 1 or B_spd <=1:
        break
    else:
        A_spd=A_spd/2
        B_spd=B_spd/2
A_spd = int((str(numpy.round(A_spd+0.001)))[:-2])
B_spd = int((str(numpy.round(B_spd+0.001)))[:-2])
print(f'{A_spd} : {B_spd}')

if A_spd > B_spd:
    print(f'{A_user}先攻')
    A_USER=A_user
    A_HP =A_hp
    A_ATK=A_atk
    A_DEF=A_def
    A_SPD=A_spd
    A_LUK=A_luk

    B_USER=B_user
    B_HP =B_hp
    B_ATK=B_atk
    B_DEF=B_def
    B_SPD=B_spd
    B_LUK=B_luk
elif A_spd < B_spd:
    print(f'{B_user}先攻')
    A_USER=B_user
    A_HP =B_hp
    A_ATK=B_atk
    A_DEF=B_def
    A_SPD=B_spd
    A_LUK=B_luk

    B_USER=A_user
    B_HP =A_hp
    B_ATK=A_atk
    B_DEF=A_def
    B_SPD=A_spd
    B_LUK=A_luk
else:
    random_user=random.choice(['A','B'])
    if random_user == 'A':
        print(f'{A_user}先攻')
        A_USER=A_user
        A_HP =A_hp
        A_ATK=A_atk
        A_DEF=A_def
        A_SPD=A_spd
        A_LUK=A_luk

        B_USER=B_user
        B_HP =B_hp
        B_ATK=B_atk
        B_DEF=B_def
        B_SPD=B_spd
        B_LUK=B_luk
    else:
        print(f'{B_user}先攻')
        A_USER=B_user
        A_HP =B_hp
        A_ATK=B_atk
        A_DEF=B_def
        A_SPD=B_spd
        A_LUK=B_luk

        B_USER=A_user
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
print(f'\n\n\n')
while A_HP >0 and B_HP>0:
    print(f'--------------------------')
    A=A_SPD
    B=B_SPD
    counter +=1
    print(f'第{counter}次戰鬥')
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
            print(f'{A_USER}打出了{A_LUK_gap_II+1}階爆擊，一共對{B_USER}造成了{Damage}點傷害\n   {B_USER}的血量剩餘 : {B_HP}')
        elif A_LUK_gap_II > 0:
            print(f'{A_USER}打出了{A_LUK_gap_II}階爆擊，一共對{B_USER}造成了{Damage}點傷害\n   {B_USER}的血量剩餘 : {B_HP}')
        elif A_LUK_gap <= atk_event*-1 or A_LUK_gap_II < 0:
            print(f'{A_USER}手滑了,對{B_USER}造成了{Damage}點傷害\n   {B_USER}的血量剩餘 : {B_HP}')
        else:
            print(f'{A_USER}對{B_USER}造成了{Damage}點傷害\n   {B_USER}的血量剩餘 : {B_HP}')

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
                print(f'{B_USER}打出了{B_LUK_gap_II+1}階爆擊，一共對{A_USER}造成了{Damage}點傷害\n   {A_USER}的血量剩餘 : {A_HP}')
            elif B_LUK_gap_II > 0:
                print(f'{B_USER}打出了{B_LUK_gap_II}階爆擊，一共對{A_USER}造成了{Damage}點傷害\n   {A_USER}的血量剩餘 : {A_HP}')
            elif B_LUK_gap <= atk_event*-1 or B_LUK_gap_II < 0:
                print(f'{B_USER}手滑了,對{A_USER}造成了{Damage}點傷害\n   {A_USER}的血量剩餘 : {A_HP}')
            else:
                print(f'{B_USER}對{A_USER}造成了{Damage}點傷害\n   {A_USER}的血量剩餘 : {A_HP}')
print(f'--------------------------')
if A_HP == 0:
    print(f'{B_USER}勝利')
else:
    print(f'{A_USER}勝利')


# MATK/ATK 以裝備決定
