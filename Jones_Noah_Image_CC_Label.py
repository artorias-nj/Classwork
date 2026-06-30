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
            

            
            num_labels, labQels, stats, centroids = cv2.connectedComponentsWithStats(closed)

            out = img.copy()
            for i in range(1, num_labels):  # skip background
                x, y, w, h, area = stats[i]
                if area < 50:  # filter tiny noise
                    continue
                cv2.rectangle(out, (x,y), (x+w, y+h), (0,255,0), 2)
                cx, cy = centroids[i]
                cv2.putText(out, f"#{i}", (int(cx), int(cy)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,255), 2)

            print("Detected objects:", num_labels-1)
            cv2.imshow("connected components", out)
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
    