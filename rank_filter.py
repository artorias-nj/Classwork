import sys
def rank_filter(orig, size_h, size_v, imgvsize, imghsize, mmm):
    filtered_img = [[0 for _ in range(imghsize)] for _ in range(imgvsize)]

    # iterate over valid pixel centers (avoid borders)
    for i in range(size_v//2, imgvsize - size_v//2):
        for j in range(size_h//2, imghsize - size_h//2):
            neighborhood = []
            for k in range(-size_v//2, size_v//2 + 1):
                for l in range(-size_h//2, size_h//2 + 1):
                    neighborhood.append(orig[i+k][j+l])
            neighborhood.sort()

            if mmm == 0:
                filtered_img[i][j] = neighborhood[0]  # min
            elif mmm == 1:
                filtered_img[i][j] = neighborhood[len(neighborhood)//2]  # median
            else:
                filtered_img[i][j] = neighborhood[-1]  # max
    return filtered_img

    
def binary(filename):
    f=open(filename, "rb")
    magic=f.readline().strip()
    if magic==b"P5":
        imgsize = f.readline().strip()
        imgsize = imgsize.split()
        columms= imgsize[0]
        rows= imgsize[1]
        mgl=f.read(3)
        f.read(1)
        magic=magic.decode('utf-8')
        columms=columms.decode('utf-8')
        rows=rows.decode('utf-8')
        mgl=mgl.decode('utf-8')
        img_header = f"{magic}\n{columms} {rows}\n{mgl}\n"
        img=[]
        for i in range(0, int(rows)):
            row=[0]*int(columms)
            for j in range(0, int(columms)):
                row[j]=int.from_bytes(f.read(1), byteorder='big')
                
            img.append(row)
        filter_h=int(input("Please enter an odd number: "))
        if (filter_h) % 2==0:
            print("Enter an odd number")
            sys.exit(0)
        filter_v=int(input("Please enter an odd number: "))
        if (filter_v) % 2==0:
            print("Enter an odd number")
            sys.exit(0)
        
        print("0 for min")
        print("1 for median")
        print("2 for max")
        mmm=int(input())
        simg=rank_filter(img,filter_h,filter_v,int(rows),int(columms),mmm)
        
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
        f.write(img_header.encode())
        for i in range(0, int(rows)):
            for j in range(0, int(columms)):
                f.write((simg[i][j]).to_bytes(1, 'big'))
        f.close()
    else:
        print("error not Binary")
        sys.exit(0)

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
binary(filename)        