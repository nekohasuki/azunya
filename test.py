import json
with open('cmds\\data\\user_data.json','r',encoding='utf8') as UserDataFile:
    userdata = json.load(UserDataFile)
#抓取檔案用的不要理他





# omikuji_update = {"938100109240074310":{"global_name":"","name":"","code":"","top_relo":"","name_card":"","point":{"state":"","now_count":"","history_count":"","consumption":"","give":"","deprivation":""},"trade_count":"","VIP_tickets":"","VIP_chip":""}}
userdata = {}
A = ''
omikuji_update = {"":{123:"","":""}}
print(A)
A.append(omikuji_update)
print(A)


userdata = A
userdata.update(userdata)
with open('cmds\\data\\user_data.json','w',encoding='utf8') as UserDataFile:
    json.dump(userdata,UserDataFile,indent=4)













