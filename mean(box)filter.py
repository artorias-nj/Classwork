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
        filter_ = [[1 for _ in range(filter_h)] for _ in range(filter_v)]
        simg=[]
        for i in range(0, int(rows)):
            row=[0]*int(columms)
            simg.append(row)
        for i in range(int((filter_v)/2), int(rows)-int(((filter_v)/2))):
            for j in range(int((filter_h)/2), int(columms)-(int((filter_h)/2))):
                for k in range(0, filter_v):
                    for l in range(0, filter_h):
                        simg[i][j]+=filter_[k][l]+img[i+(k-(int((filter_v)/2)))][j+(l-(int((filter_h)/2)))]
                simg[i][j]/=((filter_h)*(filter_v))
                simg[i][j]=int(simg[i][j])
                if simg[i][j] > int(mgl):
                    simg[i][j]=int(mgl)
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