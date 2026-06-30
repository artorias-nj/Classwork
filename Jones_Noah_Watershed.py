import cv2
import os
import argparse
import numpy as np
import matplotlib.pyplot as plt

def main(filename):
    img=cv2.imread(filename,cv2.COLOR_BGR2GRAY)
    
    if img is not None:
            gray =img.copy()
            blur = cv2.GaussianBlur(gray, (5,5), 0)

            _, th_otsu = cv2.threshold(blur, 0, 255,
                          cv2.THRESH_BINARY + cv2.THRESH_OTSU)

            kernel = np.ones((3,3), np.uint8)
            opened = cv2.morphologyEx(th_otsu, cv2.MORPH_OPEN, kernel, iterations=2)
            closed = cv2.morphologyEx(opened, cv2.MORPH_CLOSE, kernel, iterations=1)
            closed = cv2.bitwise_not(closed)
            kernel = np.ones((3,3), np.uint8)
            sure_bg = cv2.dilate(closed, kernel, iterations=3)

            dist = cv2.distanceTransform(closed, cv2.DIST_L2, 5)
            dist_norm = cv2.normalize(dist, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

            _, sure_fg = cv2.threshold(dist, 0.5*dist.max(), 255, 0)
            sure_fg = sure_fg.astype(np.uint8)

            unknown = cv2.subtract(sure_bg, sure_fg)

            num_markers, markers = cv2.connectedComponents(sure_fg)
            markers = markers + 1
            markers[unknown == 255] = 0

            ws_img = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
            markers = cv2.watershed(ws_img, markers)
            ws_img[markers == -1] = (0,0,255)  # watershed boundaries in red

            cv2.imshow("distance transform", dist_norm)
            cv2.imshow("watershed result", ws_img)
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
            
            
        main(filename)
        
        x=input("Would you like to go again? If not press 'Q' to quit: ")
        if x == "Q":
            break
        else:
            filename=None
    