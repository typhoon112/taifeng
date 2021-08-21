import json
with open("zjwater2019_2020.json") as f:
    tf = json.load(f)
interest = {"202018", "202022", "202007", "202004", "202008", "201909"}
ext = [180, 0, 90, 0]
for k, v in tf.items():
    if k in interest:
        for x in v:
            ext[0] = min(ext[0], x[0])
            ext[1] = max(ext[1], x[0])
            ext[2] = min(ext[2], x[1])
            ext[3] = max(ext[3], x[1])
print(ext)