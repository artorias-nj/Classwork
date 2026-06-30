import sys

def asci(filename):
    f=open(filename,"r")
    magic=f.readline().strip()
    if magic=="P2":
        file=f.readlines()
        file=[s.replace("\n","") for s in file]
        splitfile=[]
        for i in file:
            splitfile.extend(i.split())
        columms=splitfile[0]
        splitfile.pop(0)
        rows=splitfile[0]
        splitfile.pop(0)
        mgl=splitfile[0]
        splitfile.pop(0)
        img_header = f"{magic}\n{columms} {rows}\n{mgl}\n"
        img=[]
        index=0
        for i in range(0, int(rows)):
            row=[0]*int(columms)
            for j in range(0, int(columms)):
                row[j]=int(splitfile[index])
                index=index+1
            img.append(row)
        imghist=[0]*256
        for row in img:
            for pixel in row:
                imghist[pixel]+=1
        counter=0
        for i in imghist:
            print(str(counter)+"\t"+str(i))
            counter+=1
            
    
    else:
        print("error not Ascii")
        sys.exit(0)

def binary(filename):
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
        imghist=[0]*256
        for row in img:
            for pixel in row:
                imghist[pixel]+=1
            
        counter=0
        for i in imghist:
            print(str(counter)+"\t"+str(i))
            counter+=1
        
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
print("Enter 1 for a P2 file")
print("Enter 2 for a P5 file")
typ=int(input())
if typ==1:
    asci(filename)
elif typ==2:
    binary(filename)
else:
    print("error enter 1 or 2")
    sys.exit(0)
