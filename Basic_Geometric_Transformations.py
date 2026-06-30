import sys

def read_img_pgm(filename):
    f=open(filename, "rb")
    magic=f.readline().strip()
    columms=f.read(3)
    f.read(1)
    rows=f.read(3)
    f.read(1)
    mgl=f.read(3)
    f.read(1)
    magic=magic.decode('utf-8')
    cols=columms.decode('utf-8')
    rows=rows.decode('utf-8')
    mgl=mgl.decode('utf-8')
    img=[]
    for i in range(0, int(rows)):
        row=[0]*int(columms)
        for j in range(0, int(columms)):
            row[j]=int.from_bytes(f.read(1), byteorder='big')
        img.append(row)
    f.close
    return img, rows, cols, mgl

def write_image_pgm(filename, image, rows, cols, mgl):
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
    f=open(filename,"wb")
    magic="P5"
    img_header = f"{magic}\n{cols} {rows}\n{mgl}\n"
    f.write(img_header.encode())
    for i in range(0, int(rows)):
        for j in range(0, int(cols)):
            x=image[i][j].to_bytes(1, 'big')
            f.write(x)
    f.close()

def horizontal_flip(img, rows, cols):
    limg = []
    for i in range(int(rows)):
        limg.append(img[i][:])
    for i in range(0,rows):
        for j in range(0, cols):
            limg[i][j]=img[i][(cols-1-j)]
    return limg

def vertical_flip(img, rows, cols):
    limg = []
    for i in range(int(rows)):
        limg.append(img[i][:])
    for i in range(0,rows):
        for j in range(0, cols):
            limg[i][j]=img[(rows-1-i)][j]
    return limg

def rotation(img, rows, cols):
    limg = []
    for i in range(cols):
        limg.append([0]*rows)
    for i in range(0,rows):
        for j in range(0, cols):
            limg[j][i]=img[i][j]
    return limg

def shrink(img, rows, cols):
    limg=[]
    for i in range(0, rows,2):
        row=[]
        for j in range(0, cols,2):
            row.append(img[i][j])
        limg.append(row)
    return limg

def enlarge(img, rows, cols):
    limg=[]
    for i in range(0, rows):
        row1=[]
        row2=[]
        for j in range(0, cols):
            row1.append(img[i][j])
            row1.append(img[i][j])
            row2.append(img[i][j])
            row2.append(img[i][j])
        limg.append(row1)
        limg.append(row2)
    return limg
filename=input("What is the name of the file to be parsed: ")
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

img, rows, cols, mgl=read_img_pgm(filename)
print("What would you like to do")
print("1 for horizontal flip")
print("2 for vertical flip")
print("3 for 90 degree rotation (clockwise)")
print("4 for shruken version")
print("5 for enlarged version")
pointer=int(input())

if pointer==1:
    img=horizontal_flip(img, int(rows), int(cols))
    filename=input("What is the name of the new image: ")
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
        
    write_image_pgm(filename, img, rows, cols, mgl)
elif pointer==2:
    img=vertical_flip(img, int(rows), int(cols))
    filename=input("What is the name of the new image: ")
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
        
    write_image_pgm(filename, img, rows, cols, mgl)
elif pointer==3:
    img=rotation(img, int(rows), int(cols))
    filename=input("What is the name of the new image: ")
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
        
    write_image_pgm(filename, img, cols, rows, mgl)
elif pointer==4:
    img=shrink(img, int(rows), int(cols))
    rows=str(int(int(rows)/2))
    cols=str(int(int(cols)/2))
    filename=input("What is the name of the new image: ")
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
        
    write_image_pgm(filename, img, rows, cols, mgl)
elif pointer==5:
    img=enlarge(img, int(rows), int(cols))
    rows=str(int(int(rows)*2))
    cols=str(int(int(cols)*2))
    filename=input("What is the name of the new image: ")
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
        
    write_image_pgm(filename, img, rows, cols, mgl)