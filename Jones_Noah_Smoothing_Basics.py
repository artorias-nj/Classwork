import cv2 as cv
import os
import sys
import argparse

def main(filename, output_filename):
    img=cv.imread(filename, cv.IMREAD_GRAYSCALE)

    if img is not None:
        test=output_filename.split(".")
        if test[1] != "png" and test[1] != "jpg" and test[1] != "jpeg" and test[1] != "bmp" and test[1] != "tif" and test[1] != "tiff" and test[1] != "webp" and test[1] !="pgm":
            print("Error file type not supported")
        box_img1=cv.blur(img,(3,3))
        box_img2=cv.blur(img,(7,7))
        box_img3=cv.blur(img,(15,15))
        gaus_img1=cv.GaussianBlur(img,(3,3),0)
        gaus_img2=cv.GaussianBlur(img,(7,7),0)
        gaus_img3=cv.GaussianBlur(img,(15,15),0)
        
        outputname, ext = os.path.splitext(output_filename)
        output_filename1=f"{outputname}_box_filtered_3x3{ext}"
        output_filename2=f"{outputname}_box_filtered_7x7{ext}"
        output_filename3=f"{outputname}_box_filtered_15x15{ext}"
        output_filename4=f"{outputname}_gaus_filtered_3x3{ext}"
        output_filename5=f"{outputname}_gaus_filtered_7x7{ext}"
        output_filename6=f"{outputname}_gaus_filtered_15x15{ext}"
        
        cv.imwrite(output_filename1,box_img1)
        full_path = os.path.abspath(output_filename1)
        print(f"Image saved to: {full_path}")
        cv.imwrite(output_filename2,box_img2)
        full_path = os.path.abspath(output_filename2)
        print(f"Image saved to: {full_path}")
        cv.imwrite(output_filename3,box_img3)
        full_path = os.path.abspath(output_filename3)
        print(f"Image saved to: {full_path}")
        cv.imwrite(output_filename4,gaus_img1)
        full_path = os.path.abspath(output_filename4)
        print(f"Image saved to: {full_path}")
        cv.imwrite(output_filename5,gaus_img2)
        full_path = os.path.abspath(output_filename5)
        print(f"Image saved to: {full_path}")
        cv.imwrite(output_filename6,gaus_img3)
        full_path = os.path.abspath(output_filename6)
        print(f"Image saved to: {full_path}")
        
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
    if filename is None:
        filename=input("What is the name of the file? (example.xxx): ")
        
    if output_filename is None:
        output_filename=output_file=input("What is the name of the output? (example.xxx): ")
        
    main(filename, output_filename)