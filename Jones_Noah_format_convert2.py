import cv2 as cv
import os
import sys
import argparse

def main(filename, output_filename):
    img=cv.imread(filename)

    if img is not None:
        test=output_filename.split(".")
        if test[1] != "png" and test[1] != "jpg" and test[1] != "jpeg" and test[1] != "bmp" and test[1] != "tif" and test[1] != "tiff" and test[1] != "webp":
            print("Error file type not supported")
            sys.exit()
        if test[1]=="jpg" or test[1]=="jpeg" :
            quality=int(input("Please enter number 0-100: "))
            if quality>100 or quality<0:
                quality=90
            cv.imwrite(output_filename,img,[cv.IMWRITE_JPEG_QUALITY, quality])
        elif test[1]=="png":
            quality=int(input("Please enter number 0-9: "))
            if quality>9 or quality<0:
                quality=4
            cv.imwrite(output_filename,img,[cv.IMWRITE_PNG_COMPRESSION, quality])
        else:
            cv.imwrite(output_filename,img)
        full_path = os.path.abspath(output_filename)
        print(f"Image saved to: {full_path}")
    else:
        print("Error image could not be read")

def batch():
    extensions=[".png", ".jpg", ".jpeg", ".bmp", ".tif", ".tiff", ".webp"]
    into=input("What is the name of the input extension? (ie. .png): ").lower()
    out=input("What is the name of the output extension? (ie. .jpg): ").lower()
    if into in extensions and out in extensions:
       folder=input("What is the name of the folder press . if images in current folder: ")
       files=os.listdir(folder)
       into_files=[]
       for i in files:
           if i.endswith(into):
               into_files.append(i)
       out_files=[]
       for i in into_files:
           out_files.append(i.replace(into, out))
       for i in range(0,len(into_files)):
           img=cv.imread(into_files[i])
           cv.imwrite(out_files[i],img)
    else:
        print("Error image could not be read")

if __name__== "__main__":
    parser=argparse.ArgumentParser(description="Program converts file to a different file type")
    parser.add_argument("filename", nargs="?", help="Enter input file name")
    parser.add_argument("output_filename", nargs="?", help="Enter output file name")
    
    parser.add_argument("--filename", dest="filename_opt",help="Enter input file name")
    parser.add_argument("--output_filename", dest="output_filename_opt",help="Enter output file name")
    
    args=parser.parse_args()
    
    filename = args.filename_opt or args.filename
    output_filename= args.output_filename_opt or args.output_filename
    b=input("Enter batch is this is to be a batch conversion, enter anything else if not: ")
    if b=="batch":
       batch() 
    else:
        if filename is None:
            filename=input("What is the name of the file? (example.xxx): ")
            
        if output_filename is None:
            output_filename=output_file=input("What is the name of the output? (example.xxx): ")
        
        main(filename, output_filename)