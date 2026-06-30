y=open("mbox.txt","r")
d={}
for z in y:
    if z.startswith("From "):
        words=z.split()
        d[words[5]]=d.get(words[5],0)+1
li=list()
for key, val in d.items():
   li.append((val,key)) 
li=sorted(li, reverse=True)
print(li[0])