import json
with open('cmds\\data\\user_data.json','r',encoding='utf8') as UserDataFile:
    userdata = json.load(UserDataFile)
#抓取檔案用的不要理他



userdata={}
user_id = 938100109240074310
new_userdata = {f"{user_id}":{"global_name":"","name":"","code":"","top_relo":"","name_card":"","point":{"state":"","now_count":"","history_count":"","consumption":"","give":"","deprivation":""},"trade_count":"","VIP_tickets":"","VIP_chip":""}}


print(new_userdata[f"{user_id}"]["point"])
new_userdata = userdata
print(new_userdata[f"{user_id}"]["point"])
new_userdata[f"{user_id}"]["point"]["state"] = "56"
print(new_userdata[f"{user_id}"]["point"])



userdata.update(new_userdata)
with open('cmds\\data\\user_data.json','w',encoding='utf8') as UserDataFile:
    json.dump(userdata,UserDataFile,indent=4)















