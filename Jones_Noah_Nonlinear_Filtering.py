import cv2 as cv
import os
import sys
import argparse
import random

def add_noise(img):
#gotten from geeks for geeks 
#https://www.geeksforgeeks.org/python/add-a-salt-and-pepper-noise-to-an-image-with-python/
    # Getting the dimensions of the image
    row , col = img.shape
    
    # Randomly pick some pixels in the
    # image for coloring them white
    # Pick a random number between 300 and 10000
    number_of_pixels = random.randint(300, 10000)
    for i in range(number_of_pixels):
      
        # Pick a random y coordinate
        y_coord=random.randint(0, row - 1)
        
        # Pick a random x coordinate
        x_coord=random.randint(0, col - 1)
        
        # Color that pixel to white
        img[y_coord][x_coord] = 255
        
    # Randomly pick some pixels in
    # the image for coloring them black
    # Pick a random number between 300 and 10000
    number_of_pixels = random.randint(300 , 10000)
    for i in range(number_of_pixels):
      
        # Pick a random y coordinate
        y_coord=random.randint(0, row - 1)
        
        # Pick a random x coordinate
        x_coord=random.randint(0, col - 1)
        
        # Color that pixel to black
        img[y_coord][x_coord] = 0
        
    return img


def main(filename, output_filename):
    img=cv.imread(filename, cv.IMREAD_GRAYSCALE)

    if img is not None:
        test=output_filename.split(".")
        if test[1] != "png" and test[1] != "jpg" and test[1] != "jpeg" and test[1] != "bmp" and test[1] != "tif" and test[1] != "tiff" and test[1] != "webp" and test[1] !="pgm":
            print("Error file type not supported")
        img=add_noise(img)
        box_img1=cv.blur(img,(3,3))
        box_img2=cv.blur(img,(5,5))
        #box_img3=cv.blur(img,(15,15))
        #gaus_img1=cv.GaussianBlur(img,(3,3),0)
        gaus_img1=cv.GaussianBlur(img,(3,3),0)
        gaus_img2=cv.GaussianBlur(img,(5,5),0)
        
        outputname, ext = os.path.splitext(output_filename)
        output_filename1=f"{outputname}_box_filtered_3x3{ext}"
        output_filename2=f"{outputname}_box_filtered_5x5{ext}"
        #output_filename3=f"{outputname}_box_filtered_15x15{ext}"
        #output_filename4=f"{outputname}_gaus_filtered_3x3{ext}"
        output_filename5=f"{outputname}_gaus_filtered_3x3{ext}"
        output_filename6=f"{outputname}_gaus_filtered_5x5{ext}"
        
        peper=f"{filename}_salted_and_peppered{ext}"
        cv.imwrite(peper,img)
        full_path = os.path.abspath(peper)
        print(f"Image saved to: {full_path}")
        cv.imwrite(output_filename1,box_img1)
        full_path = os.path.abspath(output_filename1)
        print(f"Image saved to: {full_path}")
        cv.imwrite(output_filename2,box_img2)
        full_path = os.path.abspath(output_filename2)
        print(f"Image saved to: {full_path}")
        #cv.imwrite(output_filename3,box_img3)
        full_path = os.path.abspath(output_filename3)
        print(f"Image saved to: {full_path}")
        #cv.imwrite(output_filename4,gaus_img1)
        full_path = os.path.abspath(output_filename4)
        print(f"Image saved to: {full_path}")
        cv.imwrite(output_filename5,gaus_img1)
        full_path = os.path.abspath(output_filename5)
        print(f"Image saved to: {full_path}")
        cv.imwrite(output_filename6,gaus_img2)
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