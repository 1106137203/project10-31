import requests
import json
data = requests.get(url="https://gis.taiwan.net.tw/XMLReleaseALL_public/scenic_spot_C_f.json") 
with open("test.json","w",encoding="utf-8") as myFile:
    json.dump(data.json(), myFile,ensure_ascii=False)
myFile.close() 
print(data.json())  