import cv2
import os
import argparse
import numpy as np
import matplotlib.pyplot as plt

def main(filename):
    img=cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    
    if img is not None:
            scharr_x = cv2.Scharr(img, cv2.CV_64F, 1, 0)
            scharr_y = cv2.Scharr(img, cv2.CV_64F, 0, 1)

            edges_scharr = cv2.magnitude(scharr_x, scharr_y)

            # Normalize and display:
            edges_scharr = cv2.normalize(edges_scharr, None, 0, 255, cv2.NORM_MINMAX)
            edges_scharr = edges_scharr.astype("uint8")

            plt.imshow(edges_scharr, cmap='gray')
            plt.title("Scharr Edges")
            plt.show()
            
            img_blur = cv2.GaussianBlur(img, (5,5), 1)
            
            scharr_x = cv2.Scharr(img_blur, cv2.CV_64F, 1, 0)
            scharr_y = cv2.Scharr(img_blur, cv2.CV_64F, 0, 1)

            img_blur = cv2.magnitude(scharr_x, scharr_y)

            # Normalize and display:
            img_blur = cv2.normalize(img_blur, None, 0, 255, cv2.NORM_MINMAX)
            img_blur = img_blur.astype("uint8")
            
            plt.imshow(img_blur, cmap='gray')
            plt.title("Img Blur to Scharr Edges")
            plt.show()

    else:
        print("Error image could not be read")





if __name__== "__main__":
    parser=argparse.ArgumentParser(description="Program converts file to a different file type")
    parser.add_argument("filename", nargs="?", help="Enter input file name")
    
    parser.add_argument("--filename", dest="filename_opt",help="Enter input file name")
    
    args=parser.parse_args()
    
    filename = args.filename_opt or args.filename
    while True:
        
        if filename is None:
            filename=input("What is the name of the file? (example.xxx): ")
            
            
        main(filename)
        
        x=input("Would you like to go again? If not press 'Q' to quit: ")
        if x == "Q":
            break
        else:
            filename=None
    