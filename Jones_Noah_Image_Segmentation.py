import cv2
import os
import argparse
import numpy as np
import matplotlib.pyplot as plt

def main(filename):
    img=cv2.imread(filename,cv2.IMREAD_GRAYSCALE)
    
    if img is not None:
            gray =img.copy()
            blur = cv2.GaussianBlur(gray, (5,5), 0)

            _, th_otsu = cv2.threshold(blur, 0, 255,
                          cv2.THRESH_BINARY + cv2.THRESH_OTSU)

            kernel = np.ones((3,3), np.uint8)
            opened = cv2.morphologyEx(th_otsu, cv2.MORPH_OPEN, kernel, iterations=2)
            closed = cv2.morphologyEx(opened, cv2.MORPH_CLOSE, kernel, iterations=1)
            

            cv2.imshow("otsu", th_otsu)
            cv2.imshow("opened+closed", closed)
            cv2.waitKey(0)
            

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
    