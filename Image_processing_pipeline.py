import sys
import math
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
        f.close()
        return img, columms, rows, mgl, img_header 
    else:
        print("error not Binary")
        sys.exit(0)
        
    
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
            pixel = img[i][j]
            if isinstance(pixel, bytes):
                f.write(pixel)
            else:
                f.write(int(pixel).to_bytes(1, 'big'))
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
    if abs(new_thresh-thresh)<1:
        return new_thresh
    else:
        thresh=BGThresh(img, columms, rows,mgl,new_thresh)
        return thresh
    

def threshed(img, columms, rows,mgl,thresh):    
    threshold=BGThresh(img, columms, rows,mgl,thresh)
    
    for i in range(0, int(rows)):
        for j in range(0, int(columms)):
            if img[i][j]>=threshold:
                img[i][j]=255
            else:
                img[i][j]=0
    return img

def get_threshold(mgl):
    thresh=int(int(mgl)/2)
    return thresh

def rank_filter(orig, imgvsize, imghsize):
    size_h=int(input("Please enter an odd number: "))
    if (size_h) % 2==0:
        print("Enter an odd number")
        sys.exit(0)
    size_v=int(input("Please enter an odd number: "))
    if (size_v) % 2==0:
        print("Enter an odd number")
        sys.exit(0)
    filtered_img = [[0 for _ in range(imghsize)] for _ in range(imgvsize)]

    for i in range(size_v//2, imgvsize - size_v//2):
        for j in range(size_h//2, imghsize - size_h//2):
            neighborhood = []
            for k in range(-size_v//2, size_v//2 + 1):
                for l in range(-size_h//2, size_h//2 + 1):
                    neighborhood.append(orig[i+k][j+l])
            neighborhood.sort()

            filtered_img[i][j] = neighborhood[len(neighborhood)//2]  # median
    return filtered_img


def roberts(img,rows,cols,x):
    roberts_x=[[1,0],[0,-1]]
    roberts_y=[[0,1],[-1,0]]
    z=[]
    if x==1:
        z=convolve(img,roberts_x,rows,cols)
    else:
        z=convolve(img,roberts_y,rows,cols)
    return z

def convolve(img, kernel, rows, cols):
    kr=len(kernel)
    kc=len(kernel[0])
    kr2=kr//2
    kc2=kc//2
    x=[[0]*cols for _ in range(rows)]
    for i in range(rows):
        if i==0 or i==rows-1:
            continue
        for j in range(cols):
            if j==0 or j==cols-1:
                continue
            y=0
            for ki in range(kr):
                for kj in range(kc):
                    ii=i+(ki-kr2)
                    jj=j+(kj-kc2)
                    y += img[ii][jj]*kernel[ki][kj]
            x[i][j]=y
    return x

def robsqrt(img,rows,cols):
    msqrt=[]
    for i in range(0, int(rows)):
        row=[0]*int(columms)
        for j in range(0, int(columms)):
            row[j]=0
        msqrt.append(row)
    
    gh=roberts(img,rows,cols,1)
    gv=roberts(img,rows,cols,2)

    
    #magnitude
    for i in range(rows):
        if i==0 or i==rows-1:
            continue
        for j in range(cols):
            if j==0 or j==cols-1:
                continue
            msqrt[i][j]=int(math.sqrt(gh[i][j]*gh[i][j]+gv[i][j]*gv[i][j]))
    th_h=float(input("Please enter the high threshold factor: "))
    th_l=float(input("Please enter the low threshold factor: "))
    maxsqrt=0
    for i in range(rows):
        for j in range(cols):
            if msqrt[i][j]>maxsqrt:
                maxsqrt=msqrt[i][j]
    thresholdsqrth=int(th_h*maxsqrt)
    thresholdsqrtl=int(th_l*maxsqrt)
    
    for i in range(rows):
        for j in range(cols):
            if msqrt[i][j]>=thresholdsqrth:
                msqrt[i][j]=255
            elif msqrt[i][j]<thresholdsqrtl:
                msqrt[i][j]=0
            else:
                if msqrt[i-1][j-1]==255:
                    msqrt[i][j]=255
                else:
                    msqrt[i][j]=0
    return msqrt

def merge(robert_img, bgt_img, cols, rows):
    for i in range(0, rows):
        for j in range(0, cols):
            if robert_img[i][j] != 0 and bgt_img[i][j] != 0:
                bgt_img[i][j]=127
    return bgt_img

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
img=rank_filter(img,int(rows),int(columms))
print("For the filtered image")
write(img, columms, rows, mgl, img_header)
simg=[]
for i in range(int(rows)):
        simg.append(img[i]) 
simg=robsqrt(img,int(rows),int(columms))
print("For the roberts image")
write(simg, columms, rows, mgl, img_header)
init_thresh=get_threshold(mgl)
nimg=[]
for i in range(int(rows)):
        nimg.append(img[i]) 
nimg=threshed(img, columms, rows,mgl,init_thresh)
print("For the basic global threshold image")
write(nimg, columms, rows, mgl, img_header)
mimg=merge(simg, nimg,int(columms), int(rows))
print("For the merged image")
write(mimg, columms, rows, mgl, img_header)