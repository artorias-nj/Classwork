import cv2
import os
import argparse
import numpy as np
import matplotlib.pyplot as plt

def main(filename):
    img_gray=cv2.imread(filename,cv2.IMREAD_GRAYSCALE)
    img_color = cv2.imread(filename)
    
    if img_gray is not None and img_color is not None:
            bright = cv2.convertScaleAbs(img_gray, alpha=1.0, beta=40)
            contrast = cv2.convertScaleAbs(img_gray, alpha=1.5, beta=0)
            both = cv2.convertScaleAbs(img_gray, alpha=1.5, beta=40)
            

            gamma_low = gamma_correction(img_gray, 0.5)
            gamma_high = gamma_correction(img_gray, 2.0)
            
            hsv = cv2.cvtColor(img_color, cv2.COLOR_BGR2HSV)
            lab = cv2.cvtColor(img_color, cv2.COLOR_BGR2LAB)
            
            cv2.imshow("Base img", img_gray)
            cv2.imshow("Bright, img_gray", bright)
            cv2.imshow("Contrast, img_gray", contrast)
            cv2.imshow("Bright + Contrast, img_gray", both)
            cv2.imshow("Low Gamma img_gray", gamma_low)
            cv2.imshow("High Gamma img_gray", gamma_high)
            cv2.imshow("HSV img_color", hsv)
            cv2.imshow("LAB img_color", lab)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

    else:
        print("Error image could not be read")


def gamma_correction(img, gamma):
    table = np.array([(i / 255.0) ** gamma * 255
                        for i in range(256)]).astype("uint8")
    return cv2.LUT(img, table)


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
        if x == "Q" or x=="q":
            break
        else:
            filename=None
    