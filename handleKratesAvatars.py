import requests
import json
import sys

url = "https://krat.es/908f435af83b640b336f"
record = "624c33c65a015dc4d2223b6e"
headers = {
    "Content-Type": "application/json",
    "x-api-key": "a1fc3572-8633-480a-8cc3-7c12aa978558",
}
with open(sys.path[0] + "\db.json", "r") as dbJson:
    dbData = json.load(dbJson)
    dbJson.close()
data = {"avatars": []}


def putKrates():
    # data = {"sample": "Hello World"}
    req = requests.put(url + "/" + record, json=dbData, headers=headers)
    print(req.text)


def getKrates():
    req = requests.get(url + "/record/" + record, json=None, headers=headers)
    reqList = json.loads(req.text)
    reqDict = reqList[0]
    data["avatars"] = reqDict["avatars"]
    with open(sys.path[0] + "\db.json", "w+") as f:
        f.write(json.dumps(data))
        f.close()


if __name__ == "__main__":
    putKrates()
    # getKrates()
