import cv2
import os
import argparse
import numpy as np
import matplotlib.pyplot as plt

def main(filename, rotate):
    img_gray=cv2.imread(filename,cv2.IMREAD_GRAYSCALE)
    img_color = cv2.imread(filename)
    
    if img_gray is not None and img_color is not None:
        small = cv2.resize(img_gray, None, fx=0.5, fy=0.5)
        large = cv2.resize(img_gray, None, fx=2.0, fy=2.0)
        
        h, w = img_gray.shape
        M = np.float32([[1, 0, 50],
                        [0, 1, 30]])

        translated = cv2.warpAffine(img_gray, M, (w, h))
        
        center = (w // 2, h // 2)
        M = cv2.getRotationMatrix2D(center, rotate, 1.0)
        rotated = cv2.warpAffine(img_gray, M, (w, h))
        
        cv2.imshow("Shruken", small)
        cv2.imshow("Enlarged", large)
        cv2.imshow("Translated", translated)
        cv2.imshow("Rotated", rotated)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

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
            
        rotate=int(input("Please enter the number of degrees you would like the image to be rotated: "))    
        main(filename, rotate)
        
        x=input("Would you like to go again? If not press 'Q' to quit: ")
        if x == "Q" or x=="q":
            break
        else:
            filename=None
    