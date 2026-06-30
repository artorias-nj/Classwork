import cv2
import os
import argparse
import numpy as np
import matplotlib.pyplot as plt

def watershed(img):
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
    ws_img[markers == -1] = (0,0,255)
    return ws_img

def gamma_correction(img, gamma):
    table = np.array([(i / 255.0) ** gamma * 255
                        for i in range(256)]).astype("uint8")
    return cv2.LUT(img, table)

def main(filename):
    img=cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    
    if img is not None:
        
        both = cv2.convertScaleAbs(img, alpha=1.5, beta=40)
            
        gamma_low = gamma_correction(img, 0.5)
        
        median = cv2.medianBlur(img, 5)
        
        gaus=cv2.GaussianBlur(img,(5,5),0)
    
        canny_median = cv2.Canny(median, 100, 200)
        canny_gamma = cv2.Canny(gamma_low, 100, 200)
        canny_scale = cv2.Canny(both, 100, 200)
        canny_gaus= cv2.Canny(gaus, 100, 200)
        canny= cv2.Canny(img, 100, 200)
        
        watershed_median=watershed(median)
        watershed_gamma=watershed(gamma_low)
        watershed_scale=watershed(both)
        watershed_gaus=watershed(gaus)
        watershed_img=watershed(img)
        
        
        
        cv2.imshow("Base Image", img)
        cv2.imshow("canny median", canny_median)
        cv2.imshow("canny gamma", canny_gamma)
        cv2.imshow("canny contrast scale", canny_scale)
        cv2.imshow("canny gaus", canny_gaus)
        cv2.imshow("canny", canny)
        cv2.imshow("watershed median", watershed_median)
        cv2.imshow("watershed gamma", watershed_gamma)
        cv2.imshow("watershed contrast scale", watershed_scale)
        cv2.imshow("watershed gaus", watershed_gaus)
        cv2.imshow("watershed", watershed_img)
        cv2.imshow("gamma", gamma_low)
        cv2.imshow("contrast scale", both)
        cv2.imshow("gaus", gaus)
        cv2.imshow("median", median)
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
        if x == "Q" or x=="q":
            break
        else:
            filename=None
    