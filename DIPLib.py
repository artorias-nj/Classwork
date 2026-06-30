import math

def read_img_pgm(filename):
    f=open(filename, "rb")
    magic=f.readline().strip()
    cols=f.read(3)
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
    img_header = f"{magic}\n{columms} {rows}\n{mgl}\n"
    f.write(img_header.encode())
    for i in range(0, int(rows)):
        for j in range(0, int(columms)):
            x=image[i][j].to_bytes(1, 'big')
            f.write(x)
    f.close()

def write_image_tiff(filename, image, rows, cols)
    f=open(filename,"wb")
    bo='II'
    f.write(bo.encode())
    magic=42
    f.write(magic.to_bytes(2, 'little'))
    ifdoffset=8
    f.write(ifdoffset.to_bytes(4, 'little'))
    tags=8
    f.write(tags.to_bytes(2, 'little'))
    tag=256 #0x0100 	ImageWidth
    ftype=4
    values=1
    value=columms
    f.write(tag.to_bytes(2, 'little'))
    f.write(ftype.to_bytes(2, 'little'))
    f.write(values.to_bytes(4, 'little'))
    f.write(value.to_bytes(4, 'little'))
    tag=257 #0x0101 	ImageLength
    value=rows
    f.write(tag.to_bytes(2, 'little'))
    f.write(ftype.to_bytes(2, 'little'))
    f.write(values.to_bytes(4, 'little'))
    f.write(value.to_bytes(4, 'little'))
    tag=258 #0x0102 	BitsPerSample
    ftype=3
    value=8
    f.write(tag.to_bytes(2, 'little'))
    f.write(ftype.to_bytes(2, 'little'))
    f.write(values.to_bytes(4, 'little'))
    f.write(value.to_bytes(4, 'little'))
    tag=259 #0x0103 	Compression
    value=1
    f.write(tag.to_bytes(2, 'little'))
    f.write(ftype.to_bytes(2, 'little'))
    f.write(values.to_bytes(4, 'little'))
    f.write(value.to_bytes(4, 'little'))
    tag=262 # 0x0106 	PhotometricInterpretation
    f.write(tag.to_bytes(2, 'little'))
    f.write(ftype.to_bytes(2, 'little'))
    f.write(values.to_bytes(4, 'little'))
    f.write(value.to_bytes(4, 'little'))
    tag=273 # 0x0111 	StripOffsets
    ftype=4
    value=8+2+tags*12+4
    f.write(tag.to_bytes(2, 'little'))
    f.write(ftype.to_bytes(2, 'little'))
    f.write(values.to_bytes(4, 'little'))
    f.write(value.to_bytes(4, 'little'))
    tag=277 #0x0115 	SamplesPerPixel
    ftype=3
    value=1
    f.write(tag.to_bytes(2, 'little'))
    f.write(ftype.to_bytes(2, 'little'))
    f.write(values.to_bytes(4, 'little'))
    f.write(value.to_bytes(4, 'little'))
    tag=279 #0x0117 	StripByteCounts
    ftype=4
    value=(rows*columms)
    f.write(tag.to_bytes(2, 'little'))
    f.write(ftype.to_bytes(2, 'little'))
    f.write(values.to_bytes(4, 'little'))
    f.write(value.to_bytes(4, 'little'))
    f.write((0).to_bytes(4, 'little'))
    
    for i in range(0, rows):
        for j in range(0, columms):
            f.write((image[i][j]).to_bytes(1, 'little'))
    f.close()

def compute_hist(image, rows, cols, mgl)
    imghist=[0]*(int(mgl)+1)
    for row in image:
        for pixel in row:
            imghist[pixel]+=1
    return imghist
  
def hist_equal(image, rows, cols, mgl)
    imghist=[0]*256
    for row in image:
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
        for j in range(0, int(cols)):
            temp=mgl*cdf[image[i][j]]
            temp=int(temp)
            image[i][j]=temp
    return image

def box_filter_smooth(image, rows, cols, filter_v, filter_h)
    filter_ = [[1 for _ in range(filter_h)] for _ in range(filter_v)]
    simg=[]
    for i in range(0, int(rows)):
        row=[0]*int(cols)
        simg.append(row)
    for i in range(int((filter_v)/2), int(rows)-int(((filter_v)/2))):
        for j in range(int((filter_h)/2), int(columms)-(int((filter_h)/2))):
            for k in range(0, filter_v):
                for l in range(0, filter_h):
                    simg[i][j]+=filter_[k][l]+image[i+(k-(int((filter_v)/2)))][j+(l-(int((filter_h)/2)))]
            simg[i][j]/=((filter_h)*(filter_v))
            simg[i][j]=int(simg[i][j])
            if simg[i][j] > int(mgl):
                simg[i][j]=int(mgl)

def gauss_smooth(image, rows, cols, gauss_kernel, kernel_coeff, k_v, k_h)
    for i in range(0, 4):
        for j in range(0, 4):
            gauss_kernel[i][j]=gauss_kernel[i][j]*(1/kernel_coeff)
    simg=[]
    for i in range(0, int(rows)):
        row=[0]*int(cols)
        simg.append(row)
    for i in range(int((k_v)/2), int(rows)-int(((k_v)/2))):
        for j in range(int((k_h)/2), int(cols)-(int((k_h)/2))):
            for k in range(0, k_v):
                for l in range(0, k_h):
                    simg[i][j]+=gauss_kernel[k][l]+img[i+(k-(int((k_v)/2)))][j+(l-(int((k_h)/2)))]
            simg[i][j]/=((k_h)*(k_v))
            simg[i][j]=int(simg[i][j])
            if simg[i][j] > int(mgl):
                simg[i][j]=int(mgl)
 
def rank_filter(image, rows, cols, filter_v, filter_h, rank)
    filtered_img = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(filter_v//2, rows - filter_v//2):
        for j in range(filter_h//2, cols - filter_h//2):
            neighborhood = []
            for k in range(-filter_v//2, filter_v//2 + 1):
                for l in range(-filter_h//2, filter_h//2 + 1):
                    neighborhood.append(image[i+k][j+l])
            neighborhood.sort()

            if rank == 0:
                filtered_img[i][j] = neighborhood[0]  # min
            elif rank == 1:
                filtered_img[i][j] = neighborhood[len(neighborhood)//2]  # median
            elif rank ==2:
                filtered_img[i][j] = neighborhood[-1]  # max
    return filtered_img

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

def finite_diff_v(image, rows, cols)
    Gx = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            if i == 0:
                Gx[i][j] = image[i + 1][j] - image[i][j]
            elif i == rows - 1:
                Gx[i][j] = image[i][j] - image[i - 1][j]
            else:
                Gx[i][j] = image[i + 1][j] - image[i - 1][j]
    
    return Gx

def kernel_based_grad(image, rows, cols, kernel, k_v, k_h)
    G = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(k_v // 2, rows - k_v // 2):
        for j in range(k_h // 2, cols - k_h // 2):
            acc = 0
            for ki in range(k_v):
                for kj in range(k_h):
                    acc += kernel[ki][kj] * image[i + (ki - k_v // 2)][j + (kj - k_h // 2)]
            G[i][j] = acc

    return G
   
def magnitude(Gx, Gy, rows, cols, mt)
    magnitude_map = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            gx = Gx[i][j]
            gy = Gy[i][j]

            if mt == 0:
                magnitude_map[i][j] = abs(gx) + abs(gy)
            elif mt == 1:
                magnitude_map[i][j] = math.sqrt(gx**2 + gy**2)

    return magnitude_map

def edge_detection(img, magnitude, rows, cols, thresh_lo, thresh_hi)
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
    th_h=thresh_hi
    th_l=thresh_lo
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

def mg_seg_thresh(image, rows, cols)
    def find_threshold(image, columms, rows):
        max_var=0
        best_t=0
        for i in range(0,256):
            t=0
            g1=[]
            g2=[]
            for j in range(0, int(rows)):
                for k in range(0, int(columms)):
                    if image[j][k]>=i:
                        g2.append(image[j][k])
                    else:
                        g1.append(image[j][k])
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
        
    
    threshold=find_threshold(image, columms, rows)
    
    for i in range(0, int(rows)):
        for j in range(0, int(columms)):
            if image[i][j]>=threshold:
                image[i][j]=255
            else:
                image[i][j]=0
    return image
