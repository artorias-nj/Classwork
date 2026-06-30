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
                label_value = clabel
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
                is_perimeter = False
                for di, dj in neighbors:
                    ni, nj = i + di, j + dj
                    if not safe(ni, nj) or img[ni][nj] != label:
                        is_perimeter = True
                        break
                if is_perimeter:
                    if label not in perimeters:
                        perimeters[label] = 0
                    perimeters[label] += 1
    return perimeters

def coins(pcount, p, n, d, q):
    areas = [area for (_, area) in pcount]
    areas.sort()

    types_present = []
    if p: types_present.append("penny")
    if n: types_present.append("nickel")
    if d: types_present.append("dime")
    if q: types_present.append("quarter")

    k = len(types_present)

    if k == 0:
        print("No coin types selected.")
        return

    if k == 1:
        coin = types_present[0]
        count = len(areas)
        value = {"penny":0.01, "nickel":0.05, "dime":0.10, "quarter":0.25}[coin]
        total = count * value
        print(f"There are {count} {coin}s.")
        print("Total money = ${:.2f}".format(total))
        return

    cuts = []
    for i in range(k - 1):
        midpoint = (areas[i] + areas[i+1]) / 2
        cuts.append(midpoint)

    counts = {"penny":0, "nickel":0, "dime":0, "quarter":0}
    values = {"penny":0.01, "nickel":0.05, "dime":0.10, "quarter":0.25}

    for area in areas:
        index = 0
        while index < len(cuts) and area >= cuts[index]:
            index += 1

        coin_type = types_present[index]
        counts[coin_type] += 1

    total = sum(counts[c] * values[c] for c in types_present)

    print(f"There are {counts['penny']} pennies, {counts['nickel']} nickels, {counts['dime']} dimes, {counts['quarter']} quarters")
    print("Total amount of money is ${:.2f}".format(total))



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
img=threshed(img, cols, rows, init_thresh)
limg = []
for i in range(int(rows)):
    limg.append(img[i][:])
limg=labeling(limg, int(cols), int(rows),int(mgl))


pcount= pixel_count([], limg, cols, rows)
perims = perimeter_count(limg, int(cols), int(rows))
radius = {}
for label, area in pcount:
    radius[label] = 2 * (area / perims[label])
print(radius)
print("Are there any pennies 1 for yes, 0 for no")
p=int(input())
print("Are there any nickels 1 for yes, 0 for no")
n=int(input())
print("Are there any dimes 1 for yes, 0 for no")
d=int(input())
print("Are there any quarters 1 for yes, 0 for no")
q=int(input())
coins(pcount, p, n, d, q)