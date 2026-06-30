import json

from urllib.request import urlopen


x=input("Please enter an adress: ")

data = urlopen(x).read()

info = json.loads(data)

y = 0
for z in info["comments"]:
    y = y + z["count"]

print("Total comments/count:", y)
