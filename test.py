import datetime
Current_Time = datetime.datetime.now().strftime("%H:%M")
print(Current_Time)




@commands.command()
async def omikuji(self, ctx):
    user = ctx.get_user()
    if Current_Time != ("18:00"):
        if "history.json" == 有紀錄:
            await ctx.send(f"User : {user}\n你今天已經抽過了啦!\n[點我看抽到的籤]({對應訊息網址})")
        else:
            random_pic = random.choice(setting["Omikuji"])
            await ctx.send(random_pic)
            將 User : 對應訊息網址 存入"history.json"
    else:
        await ctx.send("系統維護中，請稍等1分鐘")


Clock = 0
if Current_Time == ("18:00"):
    print(Clock)
    Clock == 1
    print(Clock)
if Current_Time == ("18:01") and Clock == 0:
    # 清空 history.json
    print(Clock)
    Clock += 1
    print(Clock)


