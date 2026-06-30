import sys

def writetiff(img, filename, rows, columms):
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
            f.write((img[i][j]).to_bytes(1, 'little'))
    f.close()
    

rows=int(input("Enter the number of rows: "))
columms=int(input("Enter the number of columms: "))

img=[]
for i in range(0, rows):
    row=[0]*columms
    for j in range(0, columms):
        row[j]=0
    img.append(row)
for i in range(0, rows):
        for j in range(0, columms):
            if i<rows/2 and j<columms/2 or i>rows/2 and j>columms/2:
                img[i][j]=0
            else:
                img[i][j]=255
filename=input("What is the name of the file: ")
x=filename.split(".")
if len(x)==1:
    filename=filename+".tiff"
elif len(x)==2:
    x.pop()
    x.append(".tiff")
    filename="".join(x)
else:
    print("error to many .")
    sys.exit(0)
writetiff(img, filename, rows, columms)