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

def find_threshold(img, columms, rows, mgl):
    max_var=0
    best_t=0
    for i in range(0,(int(mgl)+1)):
        t=0
        g1=[]
        g2=[]
        for j in range(0, int(rows)):
            for k in range(0, int(columms)):
                if img[j][k]>=i:
                    g2.append(img[j][k])
                else:
                    g1.append(img[j][k])
        t=int(rows) * int(columms)
        if len(g1) ==0 or len(g2)==0:
            continue
        g1m=find_mean(g1)
        g2m=find_mean(g2)
        g1v=find_variance(g1, g1m)
        g2v=find_variance(g2, g2m)
        g1w=len(g1)/t
        g2w=len(g2)/t
        
        between_var =  g1w * g2w * ((g1m - g2m)*(g1m - g2m))
        if between_var > max_var:
            best_t = i
            max_var = between_var
    return best_t
        

def find_variance(img, mean):
    x=[]
    for i in img:
        z=i-mean
        z=z*z
        x.append(z)
    x=sum(x)
    v=int(x/len(img))
    return v

def find_mean(img):
    m=sum(img)
    m=int(m/len(img))
    return m
    
def threshed(img, columms, rows, mgl):
    
    threshold=find_threshold(img, columms, rows, mgl)
    
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
img=threshed(img, columms, rows, mgl)
write(img, columms, rows, mgl, img_header)