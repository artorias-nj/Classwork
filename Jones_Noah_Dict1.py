nfh=open("mbox-short.txt","r")
d={}
for z in nfh:
    if z.startswith("From "):
        words=z.split()
        d[words[2]]=d.get(words[2],0)+1
print(d)
    