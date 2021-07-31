import datetime
import json
import requests
import tqdm

listURL = "http://typhoon.zjwater.gov.cn/Api/TyphoonList/{}" # starts from 1945
detailURL = "http://typhoon.zjwater.gov.cn/Api/TyphoonInfo/{}"

def str2datetime(timestr: str) -> datetime.datetime:
    return datetime.datetime.strptime(timestr, "%Y/%m/%d %H:%M:%S")

for year in range(1945, 2020 + 1):
    print(year)
    dataCollection = dict()
    listRes = requests.get(listURL.format(year))
    listJSON = json.loads(listRes.text)
    listTyphoon = [tf["tfid"] for tf in listJSON]
    for tfid in tqdm.tqdm(listTyphoon):
        detailRes = requests.get(detailURL.format(tfid))
        detail = json.loads(detailRes.text)[0]
        timeline = list()
        lat= list()
        lng = list()
        pressure = list()
        power = list()
        movespeed = list()
        starttime = str2datetime(detail["starttime"])
        for pnt in detail["points"]:
            timeline.append(int((str2datetime(pnt["time"]) - starttime).total_seconds()) // 3600)
            lat.append(float(pnt["lat"]))
            lng.append(float(pnt["lng"]))
            try:
                pressure.append(int(pnt["pressure"]))
            except:
                pressure.append(-1)
            try:
                power.append(int(pnt["power"]))
            except:
                power.append(-1)
            try:
                movespeed.append(int(pnt["movespeed"]))
            except:
                movespeed.append(-1)
        dataCollection[tfid] = dict(
            enname=detail["enname"],
            starttime=str(starttime),
            timeline=timeline,
            lat=lat,
            lng=lng,
            pressure=pressure,
            power=power,
            movespeed=movespeed
        )
        # break
    with open("zjwater{}.json".format(year), "w") as f:
        json.dump(dataCollection, f)
    # break