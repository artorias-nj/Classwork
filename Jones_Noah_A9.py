import os
fn=input("Please input file name: ")
ufh=open(fn,'w')
ufh=ufh.write("This is my first file!")
input("WAIT!")
ufh=open(fn,'r')
for i in ufh:
    i=i.rstrip()
    print(i)
