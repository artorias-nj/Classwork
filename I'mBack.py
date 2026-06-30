x=input("Please enter file name:  ")
y=open(x,"r")
counts=dict()
for i in y:
    names=i.split()
    for name in names:
        counts[name]=counts.get(name,0)+1
print(counts)
   