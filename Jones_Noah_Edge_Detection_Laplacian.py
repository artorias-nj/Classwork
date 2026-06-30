import cv2
import os
import argparse
import numpy as np
import matplotlib.pyplot as plt

def main(filename):
    img=cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    
    if img is not None:
            edges_lap = cv2.Laplacian(img, cv2.CV_64F)
            edges_lap = cv2.convertScaleAbs(edges_lap)

            plt.imshow(edges_lap, cmap='gray')
            plt.title("Laplacian Edges")
            plt.show()
            
            img_blur = cv2.GaussianBlur(img, (5,5), 1)
            img_blur = cv2.Laplacian(img_blur, cv2.CV_64F)
            img_blur = cv2.convertScaleAbs(edges_lap)
            plt.imshow(img_blur, cmap='gray')
            plt.title("Img Blur to Laplacian Edges")
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
    