import json
with open('cmds\\data\\user_data.json','r',encoding='utf8') as UserDataFile:
    userdata = json.load(UserDataFile)
#抓取檔案用的不要理他

#---------------------------------------------
user = 697842681082281985
count = 1
#---------------------------------------------

# userdata_updata = {'display_name':f'{user.display_name}','global_name':f'{user.global_name}','code':f'{(code)+1}','top_role':f'<@&{user.top_role.id}>','name_card':f'{str(True)}','point':{'state':f'{str(True)}','now_count':0,'history_count':0,'consumption':0,'give':0,'deprivation':0},'trade_count': 0,'VIP_tickets': 0,'VIP_chip': 0}
userdata_updata = {'13':112}
userdata.update(userdata_updata)




with open('cmds\\data\\user_data.json','w',encoding='utf8') as UserDataFile:
    json.dump(userdata,UserDataFile,indent=4)



























