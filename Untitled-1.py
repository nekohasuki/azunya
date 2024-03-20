import os

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n-----------------------------------------------------------\n@ALL:")
for Filename in os.listdir("./cmds"):
        print(Filename)
        
print("-----------------------------------------------------------\n@Pythin:")
for Filename in os.listdir("./cmds"):
    if Filename.endswith(".py"):
        print(Filename[:-3])
        
print("-----------------------------------------------------------")