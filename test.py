import json
with open('cmds\\data\\user_data.json','r',encoding='utf8') as UserDataFile:
    userdata = json.load(UserDataFile)
#抓取檔案用的不要理他



# userdata={}
user_id = 619892110421655602
new_userdata = {f"{user_id}":{"global_name":"","name":"","code":"","top_role":"","name_card":"","point":{"state":"","now_count":"","history_count":"","consumption":"","give":"","deprivation":""},"trade_count":"","VIP_tickets":"","VIP_chip":""}}


new_userdata[f"{user_id}"]["global_name"] = "Stars Shine "
new_userdata[f"{user_id}"]["name"] = "starsshine"
new_userdata[f"{user_id}"]["code"] = "901"
new_userdata[f"{user_id}"]["top_role"] = f"<@&965668031114129438>"
new_userdata[f"{user_id}"]["name_card"] = "True"
new_userdata[f"{user_id}"]["point"]["state"] = "None"
new_userdata[f"{user_id}"]["point"]["now_count"] = "0"
new_userdata[f"{user_id}"]["point"]["history_count"] = "0"
new_userdata[f"{user_id}"]["point"]["consumption"] = "0"
new_userdata[f"{user_id}"]["point"]["give"] = "0"
new_userdata[f"{user_id}"]["point"]["deprivation"] = "0"
new_userdata[f"{user_id}"]["trade_count"] = "0"
new_userdata[f"{user_id}"]["VIP_tickets"] = "0"
new_userdata[f"{user_id}"]["VIP_chip"] = "0"



userdata.update(new_userdata)
with open('cmds\\data\\user_data.json','w',encoding='utf8') as UserDataFile:
    json.dump(userdata,UserDataFile,indent=4)





# 普 965668031114129438
#  958826888950874192








