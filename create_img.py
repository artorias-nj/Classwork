import sys
filename=input("What is the name of the file: ")
x=filename.split(".")
if len(x)==1:
    filename=filename+".pgm"
elif len(x)==2:
    x.pop()
    x.append(".pgm")
    filename="".join(x)
else:
    print("error to many .")
    sys.exit(0)
tob=int(input("Enter 1 for text or 2 for binary: "))
if tob<3 and tob>0:
    if tob==1:
        tob="P2"
    if tob==2:
        tob="P5"
else:
    print("error please enter 1 or 2")
    sys.exit(0)
columms=input("Please input the number of columms: ")
rows=input("please enter the number of rows: ")
mgl="255"

pixel_value=int(input("Please enter a number 0-255: "))

img_header = f"{tob}\n{columms} {rows}\n{mgl}\n"

img=[]
for i in range(0, int(rows)):
    row=[0]*int(columms)
    for j in range(0, int(columms)):
        row[j]=pixel_value
    img.append(row)

if tob=="P2":
    f=open(filename,"w")
    f.write(img_header)
    for row in img:
        rowwidth=0
        for j in row:
            f.write(str(j)+" ")
            rowwidth=rowwidth+1
            if rowwidth==25:
                f.write('\n')
                rowwidth=0
        f.write("\n")
    f.close()
else:
    f=open(filename,"wb")
    f.write(img_header.encode())
    for i in range(0, int(rows)):
        for j in range(0, int(columms)):
            f.write((img[i][j]).to_bytes(1, 'big'))
    f.close()
