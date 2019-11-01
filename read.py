import urllib.request, json 

x = []
y = []

with urllib.request.urlopen("ใส่ url ที่ได้จาก Cloud Function") as url:
    data = json.loads(url.read().decode())
    for i in data.values():
        x.append(i['x'])
        y.append(i['y'])
        #print(i)
    #print(data)

print(x)
print(y)