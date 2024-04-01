import json
with open("cmds\data\omikuji.json","r",encoding="utf8") as omikuji_file:
    omikuji = json.load(omikuji_file)
    omikuji={"userdata": [],"namedata": []}
    omikuji.update(omikuji)
with open("cmds\data\omikuji.json","w",encoding="utf8") as omikuji_file:
    json.dump(omikuji,omikuji_file)