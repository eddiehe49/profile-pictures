import requests
import json
import sys

url = "https://api.jsonbin.io/v3/b/624173ee0618276743817ab6"
headers = {
    "X-Master-Key": "$2b$10$Dr3C03m96HY3V014.oTOf.kh/veUr7PF2tLr7FK/B9v03pstYPCSO"
}
with open(sys.path[0] + "\db.json", "r") as dbJson:
    dbData = json.load(dbJson)
    dbJson.close()


def putBin():
    headers["Content-Type"] = "application/json"
    # data = {"sample": "Hello World"}
    req = requests.put(url + "/", json=dbData, headers=headers)
    print(req.text)


def getBin():
    req = requests.get(url + "/latest", json=None, headers=headers)
    reqDict = json.loads(req.text)
    print(reqDict["record"])
    # with open(sys.path[0] + "\db.json", "w+") as f:
    #     f.write(json.dumps(reqDict["record"]))
    #     f.close()


def deleteVersion():
    headers["X-Preserve-Latest"] = "true"
    req = requests.delete(url + "/versions", json=None, headers=headers)
    print(req.text)


if __name__ == "__main__":
    # putBin()
    getBin()
    # deleteVersion()
