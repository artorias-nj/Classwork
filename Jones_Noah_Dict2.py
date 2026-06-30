y=open("mbox.txt","r")
d={}
for z in y:
    if z.startswith("From "):
        words=z.split()
        d[words[1]]=d.get(words[1],0)+1
print(d)
count=0
most=" "
for key, val in d.items():
    if val > count:
        count = val
        most = key
print(most+" "+str(count))