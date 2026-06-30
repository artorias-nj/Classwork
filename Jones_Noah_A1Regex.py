import re
z=input("Please enter file name: ")
file=open(z,"r")
x=input("Please enter a regular expression: ")
count=0
for i in file:
    if re.search(x,i)!=None:
        count=count+1
print(z+" had "+str(count)+" lines that matched "+str(x))