import sys
import math

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

def BGThresh(img, cols, rows,thresh):
    scv=1
    g1=[]
    g2=[]
    for i in range(0, int(rows)):
        for j in range(0, int(cols)):
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
        thresh=BGThresh(img, cols, rows,new_thresh)
        return thresh
    
def threshed(img, cols, rows,thresh):    
    threshold=BGThresh(img, cols, rows,thresh)
    
    for i in range(0, int(rows)):
        for j in range(0, int(cols)):
            if img[i][j]>=threshold:
                img[i][j]=255
            else:
                img[i][j]=0
    return img

def get_threshold(mgl):
    thresh=int(mgl/2)
    return thresh

def labeling(img, cols, rows, mgl):
    clabel = 1
    directions = [(-1,-1), (-1,0), (-1,1),
                  (0,-1),          (0,1),
                  (1,-1),  (1,0),  (1,1)]

    def safe(i, j):
        return 0 <= i < rows and 0 <= j < cols

    for i in range(rows):
        for j in range(cols):
            if img[i][j] == mgl:
                label_value = clabel*15
                stack = [(i, j)]
                img[i][j] = label_value

                while stack:
                    ci, cj = stack.pop()
                    for di, dj in directions:
                        ni, nj = ci + di, cj + dj
                        if safe(ni, nj) and img[ni][nj] == mgl:
                            img[ni][nj] = label_value
                            stack.append((ni, nj))

                clabel += 1

    return img
    
def pixel_count(count, img, cols, rows):
    for i in range(int(rows)):
        for j in range(int(cols)):
            pixel = img[i][j]
            if pixel != 0:
                found = False
                for item in count:
                    if item[0] == pixel:
                        item[1] += 1
                        found = True
                        break
                if not found:
                    count.append([pixel, 1])
    return count

def perimeter_count(img, cols, rows):
    perimeters = {}

    neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def safe(i, j):
        return 0 <= i < rows and 0 <= j < cols

    for i in range(rows):
        for j in range(cols):
            label = img[i][j]
            if label != 0:
                for di, dj in neighbors:
                    ni, nj = i + di, j + dj
                    if not safe(ni, nj) or img[ni][nj] != label:
                        if label not in perimeters:
                            perimeters[label] = 0
                        perimeters[label] += 1

    return perimeters

def circularity(pcount, perims):
    circ = []
    for label, area in pcount:
        perim = perims.get(label, 0)
        if perim == 0:
            circ.append(0)
        else:
            c = (4 * math.pi * area) / (perim ** 2)
            circ.append(c)
    for i in range(0, len(circ)):
        if circ[i]>0.589 and circ[i]<0.62:
            circ[i]=True
        else:
            circ[i]=False
    return circ

def centroid(img, cols, rows, pcount):
    x = {label: 0 for label, area in pcount}
    y = {label: 0 for label, area in pcount}
    count = {label: 0 for label, area in pcount}
    for i in range(rows):
        for j in range(cols):
            pixel=img[i][j]
            if pixel in x:
                x[pixel]+=j
                y[pixel]+=i
                count[pixel]+=1
    centers={}
    for label in x:
        cx=int(x[label]/count[label])
        cy=int(y[label]/count[label])
        centers[label]=(cx, cy)
    return centers

def bounding_boxes(img, cols, rows, pcount):
    min_r={label: rows for label, area in pcount}
    max_r={label: 0 for label, area in pcount}
    min_c={label: cols for label, area in pcount}
    max_c={label: 0 for label, area in pcount}

    for i in range(rows):
        for j in range(cols):
            pixel=img[i][j]
            if pixel in min_r:
                if i<min_r[pixel]:
                    min_r[pixel]=i
                if i>max_r[pixel]:
                    max_r[pixel]=i
                if j<min_c[pixel]:
                    min_c[pixel]=j
                if j>max_c[pixel]:
                    max_c[pixel]=j

    boxes={}
    for label, area in pcount:
        boxes[label]=(min_r[label], min_c[label], max_r[label], max_c[label])
    return boxes

def add_centroid_and_bounding_box(img, boxes, centers, pcount):
    for label, area in pcount:
        box=boxes[label]    
        min_r, min_c, max_r, max_c = box
        for c in range(min_c, max_c + 1):
            img[min_r][c]=255
            img[max_r][c]=255
        for r in range(min_r, max_r + 1):
            img[r][min_c]=255
            img[r][max_c]=255
        (cx, cy)=centers[label]
        cx=int(cx)
        cy=int(cy)
        for d in range(-3, 4):
            if d == 0 or d==1 or d==-1:
                continue
            if 0<=cy<len(img) and 0<=cx+d<len(img[0]):
                img[cy][cx+d]=0
            if 0<=cy+d<len(img) and 0<=cx<len(img[0]):
                img[cy+d][cx]=0

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
init_thresh=get_threshold(int(mgl))
nimg = []
for i in range(int(rows)):
    nimg.append(img[i][:])
nimg=threshed(nimg, cols, rows, init_thresh)
limg = []
for i in range(int(rows)):
    limg.append(nimg[i][:])
limg=labeling(limg, int(cols), int(rows),int(mgl))


pcount= pixel_count([], limg, cols, rows)
perims = perimeter_count(limg, int(cols), int(rows))
circ=circularity(pcount, perims)
centers=centroid(limg, int(cols), int(rows), pcount)
boxes = bounding_boxes(limg, int(cols), int(rows), pcount)
count=0
print("Summary:")
x=str(len(pcount))
print("there are "+x+" components in the image")
for label, area in pcount:
    print(f"For label {label}: Centroid = {centers.get(label, 0)}, Circularity = {circ[count]}, Box = {boxes[label]}")
    count+=1
add_centroid_and_bounding_box(limg, boxes, centers, pcount)
filename=input("What is the name of the label image: ")
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
write_image_pgm(filename, limg, rows, cols, mgl)
add_centroid_and_bounding_box(img, boxes, centers, pcount)
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