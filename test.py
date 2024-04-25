import json
with open('cmds\\data\\test.json','r',encoding='utf8') as UserDataFile:
    userdata = json.load(UserDataFile)
#抓取檔案用的不要理他

#---------------------------------------------
user = 938100109240074310
count = 1
#---------------------------------------------

userdata_updata = userdata[f"{user}"]
print(userdata)
now_count = userdata_updata['point']['now_count']
history_count = userdata_updata['point']['history_count']
userdata_updata['point']['now_count'] = int(now_count) + count
userdata_updata['point']['history_count'] = int(history_count) + count


userdata[f"{user}"].update(userdata_updata)
with open('cmds\\data\\test.json','w',encoding='utf8') as UserDataFile:
    json.dump(userdata,UserDataFile,indent=4)



























