def top_bottom(img, columms, rows):
    for i in range(0, int(rows)):
        for j in range(0, int(columms)):
            if i<int(rows)/2:
                img[i][j]=0
            else:
                img[i][j]=255
    
def left_right(img, columms, rows):
    for i in range(0, int(rows)):
        for j in range(0, int(columms)):
            if j<int(columms)/2:
                img[i][j]=0
            else:
                img[i][j]=255
    
def checkered(img, columms, rows):
    for i in range(0, int(rows)):
        for j in range(0, int(columms)):
            if i<int(rows)/2 and j<int(columms)/2 or i>int(rows)/2 and j>int(columms)/2:
                img[i][j]=0
            else:
                img[i][j]=255


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
columms=input("Please input the number of columms: ")
rows=input("please enter the number of rows: ")
mgl="255"
print("Press 1 for left right pattern")
print("Press 2 for top bottom pattern")
print("Press 3 for checkered pattern")
pattern=int(input())

img_header = f"{'P5'}\n{columms} {rows}\n{mgl}\n"

img=[]
for i in range(0, int(rows)):
    row=[0]*int(columms)
    for j in range(0, int(columms)):
        row[j]=0
    img.append(row)
if pattern ==1:
    left_right(img, columms, rows)
        
elif pattern ==2:
    top_bottom(img, columms, rows)
    
elif pattern ==3:
    checkered(img, columms, rows)
    

f=open(filename,"wb")
f.write(img_header.encode())
for i in range(0, int(rows)):
    for j in range(0, int(columms)):
        f.write((img[i][j]).to_bytes(1, 'big'))
f.close()
