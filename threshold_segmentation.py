import sys
import matplotlib.pyplot as plt
import scipy.stats as ss

def readimg(filename):
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
        img_header = f"{magic}\n{columms} {rows}\n{mgl}\n"
        img=[]
        for i in range(0, int(rows)):
            row=[0]*int(columms)
            for j in range(0, int(columms)):
                row[j]=int.from_bytes(f.read(1), byteorder='big')
            img.append(row)
        f.close
        return img, columms, rows, mgl, img_header 
    else:
        print("error not Binary")
        sys.exit(0)
        
        
        
        
def histogram(img, columms, rows, mgl):
    imghist=[0]*256
    for row in img:
        for pixel in row:
            imghist[pixel]+=1
    n=sum(imghist)
    n=float(n)
    nh=[]
    for i in imghist:
        nh.append(float(i)/n)
    cdf=[]
    for i in range(0,len(nh)):
        temp=0.0
        for k in range(0,i):
            temp=temp+nh[k]
        cdf.append(temp)
    mgl=int(mgl)-1
    for i in range(0, int(rows)):
        for j in range(0, int(columms)):
            temp=mgl*cdf[img[i][j]]
            temp=int(temp)
            img[i][j]=temp.to_bytes(1, 'big')
    return img
    
def write(img, columms, rows, mgl, img_header):
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
            f.write(img[i][j])
    f.close()

def calchist(img):
    imghist=[0]*256
    for row in img:
        for pixel in row:
            x=int.from_bytes(pixel, byteorder='big')
            imghist[x]+=1
        
    counter=0
    hist=[]
    for i in imghist:
        hist.append([counter,i])
        counter+=1
    printhist(hist)
    
def threshed(img, columms, rows):
    print("What is the threshold?")
    threshold=int(input())
    for i in range(0, int(rows)):
        for j in range(0, int(columms)):
            x=int.from_bytes(img[i][j], byteorder='big')
            img[i][j]=x
    for i in range(0, int(rows)):
        for j in range(0, int(columms)):
            if img[i][j]>=threshold:
                img[i][j]=255
            else:
                img[i][j]=0
    for i in range(0, int(rows)):
        for j in range(0, int(columms)):    
            x=img[i][j].to_bytes(1, 'big')
            img[i][j]=x
    return img



def printhist(hist):
    values = [pair[0] for pair in hist]
    frequencies = [pair[1] for pair in hist] 
    
    plt.bar(values, frequencies, edgecolor='black', width=0.8)
    plt.title("Histogram Example")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.show()

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

img, columms, rows, mgl, img_header=readimg(filename)
img=histogram(img, columms, rows, mgl)
write(img, columms, rows, mgl, img_header)
calchist(img)
img=threshed(img, columms, rows)
write(img, columms, rows, mgl, img_header)