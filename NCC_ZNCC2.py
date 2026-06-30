import os
import argparse
import cv2
import numpy as np


def main(left_image_name, right_image_name):
    limg=cv2.imread(left_image_name, cv2.IMREAD_GRAYSCALE)
    rimg=cv2.imread(right_image_name, cv2.IMREAD_GRAYSCALE)
    lrows = limg.shape[0]
    lcols = limg.shape[1]
    rrows = rimg.shape[0]
    rcols = rimg.shape[1]
    dmax = 20
    wv = 20
    wh = 20
    half_wv = wv // 2
    half_wh = wh // 2
    stereo = [[0]*lcols for _ in range(lrows)]
    min_disp=None
    max_disp=None
    for j in range(half_wv, lrows-half_wv):
        for i in range(dmax + half_wh, lcols - half_wh - dmax):
            best_cost = float('inf')
            best_d = 0
            for d in range(0, dmax+1):
                sum_L = 0
                sum_R = 0
                count = 0
                for l in range(-half_wv, half_wv+1):
                    for k in range(-half_wh, half_wh+1):
                        L = int(limg[j+l][i+k])
                        R = int(rimg[j+l][i-d+k])
                        sum_L += L
                        sum_R += R
                        count += 1
                mean_L = sum_L / count
                mean_R = sum_R / count
                acc = 0
                for l in range(-half_wv, half_wv+1):
                    for k in range(-half_wh, half_wh+1):
                        L = int(limg[j+l][i+k])
                        R = int(rimg[j+l][i-d+k])
                        diff = (L - mean_L) - (R - mean_R)
                        acc += abs(diff)
                if acc < best_cost:
                    best_cost = acc
                    best_d = d
            stereo[j][i] = best_d
    for j in range(half_wv, lrows-half_wv):
        for i in range(dmax + half_wh, lcols - half_wh - dmax):
            stereo[j][i] = int(((stereo[j][i]-min_disp)/(max_disp-min_disp))*255)
    stereo = np.array(stereo, dtype=np.uint8)
    cv2.imwrite("ZSAD.pgm", stereo)
   


if __name__== "__main__":
    parser=argparse.ArgumentParser(description="Program converts file to a different file type")
    parser.add_argument("left_image", nargs="?", help="Enter left image name")
    parser.add_argument("right_image", nargs="?", help="Enter right image name")
    
    parser.add_argument("--left_image", dest="filename_opt",help="Enter left image name")
    parser.add_argument("--right_image", dest="output_filename_opt",help="Enter right image name")
    
    args=parser.parse_args()
    
    left_image = args.filename_opt or args.left_image
    right_image= args.output_filename_opt or args.right_image
    while True:
        
        if left_image is None:
            left_image=input("What is the name of the left image? (example.xxx): ")
        
        if right_image is None:
            right_image=input("What is the name of the right image? (example.xxx): ")
            
            
        main(left_image, right_image)
        
        x=input("Would you like to go again? If not press 'Q' to quit: ")
        if x == "Q" or x=="q":
            break
        else:
            left_image=None
            right_image=None