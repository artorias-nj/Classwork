import re
z=input("Please enter file name: ")
file=open(z,"r")
y=list()
for i in file:
    i=i.rstrip()
    words=i.split()
    for digit in words:
        n=re.findall("^([0-9]+)$",digit)
        if len(n)>0:
            y.append(n)
nums=list()
for i in y:
    for q in i:
        q=int(q)
        nums.append(q)
        
sums=0
total=len(nums)
for i in nums:
    sums=sums+i
print(sums)