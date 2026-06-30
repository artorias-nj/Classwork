import sys

def read_img_pgm(filename):
    f=open(filename, "rb")
    magic=f.readline().strip()
    if magic==b"P5":
        columms=f.read(3)
        f.read(1)
        rows=f.read(3)
        f.read(1)
        mgl=f.read(3)
        f.read(1)
        magic=magic.decode('utf-8')
        columms=columms.decode('utf-8')
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
    else:
        print("error not Binary")
        sys.exit(0)

def write_image_pgm(img, rows, cols, mgl):
    filename=input("What is the name of the file to be written to: ")
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
    img_header = f"{magic}\n{columms} {rows}\n{mgl}\n"
    f.write(img_header.encode())
    for i in range(0, int(rows)):
        for j in range(0, int(columms)):
            x=img[i][j].to_bytes(1, 'big')
            f.write(x)
    f.close()f

def finite_diff_h(image, rows, cols):
    Gy = [[0 for _ in range(cols)] for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            if j==0:                
                Gy[i][j]=image[i][j+1]-image[i][j]
            elif j==cols-1:
                Gy[i][j]=image[i][j]-image[i][j-1]
            else:
                Gy[i][j]=image[i][j+1]-image[i][j-1]
    return Gy