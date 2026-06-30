import math
import sys
def absqrt(img,gh,gv,rows,cols,mabs,msqrt):
    for i in range(rows):
        if i==0 or i==rows-1:
            continue
        for j in range(cols):
            if j==0 or j==cols-1:
                continue
            gh[i][j]=img[i][j-1]-img[i][j+1]
            gv[i][j]=img[i-1][j]-img[i+1][j]
    #magnitude
    for i in range(rows):
        if i==0 or i==rows-1:
            continue
        for j in range(cols):
            if j==0 or j==cols-1:
                continue
            mabs[i][j]=int(abs(gh[i][j])+abs(gv[i][j]))
            msqrt[i][j]=int(math.sqrt(gh[i][j]*gh[i][j]+gv[i][j]*gv[i][j]))
    th_h=float(input("Please enter the high threshold factor: "))
    th_l=float(input("Please enter the low threshold factor: "))
    maxabs=0
    maxsqrt=0
    for i in range(rows):
        for j in range(cols):
            if mabs[i][j]>maxabs:
                maxabs=mabs[i][j]
            if msqrt[i][j]>maxsqrt:
                maxsqrt=msqrt[i][j]
    thresholdabsh=int(th_h*maxabs)
    thresholdsqrth=int(th_h*maxsqrt)
    thresholdabsl=int(th_l*maxabs)
    thresholdsqrtl=int(th_l*maxsqrt)
    #print(maxabs,maxsqrt,thresholdabs,thresholdsqrt,th)
    
    
    for i in range(rows):
        for j in range(cols):
            if mabs[i][j]>=thresholdabsh:
                mabs[i][j]=255
            elif mabs[i][j]<thresholdabsl:
                mabs[i][j]=0
            else:
                if mabs[i-1][j-1]==255:
                    mabs[i][j]=255
                else:
                    mabs[i][j]=0
            if msqrt[i][j]>=thresholdsqrth:
                msqrt[i][j]=255
            elif msqrt[i][j]<thresholdsqrtl:
                msqrt[i][j]=0
            else:
                if msqrt[i-1][j-1]==255:
                    msqrt[i][j]=255
                else:
                    msqrt[i][j]=0
    return mabs, msqrt
    



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
        gh=[]
        for i in range(0, int(rows)):
            row=[0]*int(columms)
            for j in range(0, int(columms)):
                row[j]=0
                
            gh.append(row)
        gv=[]
        for i in range(0, int(rows)):
            row=[0]*int(columms)
            for j in range(0, int(columms)):
                row[j]=0
                
            gv.append(row)
        mabs=[]
        for i in range(0, int(rows)):
            row=[0]*int(columms)
            for j in range(0, int(columms)):
                row[j]=0
                
            mabs.append(row)
        msqrt=[]
        for i in range(0, int(rows)):
            row=[0]*int(columms)
            for j in range(0, int(columms)):
                row[j]=0
                
            msqrt.append(row)
        

        simg, yimg=absqrt(img,gh,gv,int(rows),int(columms),mabs,msqrt)

        
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
                f.write((yimg[i][j]).to_bytes(1, 'big'))
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