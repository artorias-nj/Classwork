import sys

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


def BGThresh(img, columms, rows,mgl,thresh):
    scv=1
    g1=[]
    g2=[]
    for i in range(0, int(rows)):
        for j in range(0, int(columms)):
            if img[i][j]>=thresh:
                g2.append(img[i][j])
            else:
                g1.append(img[i][j])
    m1=sum(g1)/len(g1)
    m2=sum(g2)/len(g2)
    new_thresh=(m1+m2)/2
    if abs(new_thresh-thresh)<50:
        return new_thresh
    else:
        thresh=BGThresh(img, columms, rows,mgl,new_thresh)
        return thresh
    

def threshed(img, columms, rows,mgl,thresh):
    for i in range(0, int(rows)):
        for j in range(0, int(columms)):
            x=int.from_bytes(img[i][j], byteorder='big')
            img[i][j]=x
    
    threshold=BGThresh(img, columms, rows,mgl,thresh)
    
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

def get_threshold(mgl):
    thresh=int(int(mgl)/2)
    return thresh


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
init_thresh=get_threshold(mgl)
img=threshed(img, columms, rows,mgl,init_thresh)
write(img, columms, rows, mgl, img_header)