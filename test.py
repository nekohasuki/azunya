import discord
import datetime
import asyncio
from discord.ext import tasks

t=1
while t>0:
    Current_hours = datetime.datetime.now().strftime("%H")
    Current_minutes = datetime.datetime.now().strftime("%M")
    Current_seconds = datetime.datetime.now().strftime("%S")
    time = (f"{int(Current_hours)}:{int(Current_minutes)}:{int(Current_seconds)}")
    asyncio.sleep(1)
    print(time)

