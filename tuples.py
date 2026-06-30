fn=input("please enter file name: ")
file=open(fn,r)
d={}
for i in file:
    words=i.split()
    for z in words:
        d[words[z]]=d.get(words[z],0)+1
for key, val in d.items():
    newtuple=(val,key)
highest=[newtuple]
highest=sort(highest, reverse order)
print(highest[:5])