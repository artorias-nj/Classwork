import os
import argparse
import cv2
import numpy as np


def main(left_image_name, right_image_name):
    limg = cv2.imread(left_image_name, cv2.IMREAD_GRAYSCALE)
    rimg = cv2.imread(right_image_name, cv2.IMREAD_GRAYSCALE)
    lrows, lcols = limg.shape
    rrows, rcols = rimg.shape
    dmax = 53   
    wv = 20
    wh = 20
    half_wv = wv // 2
    half_wh = wh // 2
    stereo = np.zeros((lrows, lcols), dtype=np.float32)
    cost_volume = np.zeros((lrows, lcols, dmax+1), dtype=np.float32)
    min_disp = None
    max_disp = None
    for j in range(half_wv, lrows - half_wv):
        for i in range(dmax + half_wh, lcols - half_wh - dmax):
            for d in range(0, dmax + 1):
                acc = 0
                for l in range(-half_wv, half_wv + 1):
                    for k in range(-half_wh, half_wh + 1):
                        L = int(limg[j + l][i + k])
                        R = int(rimg[j + l][i - d + k])
                        acc += abs(L - R)
                cost_volume[j][i][d] = acc
    
    P1 = 10
    P2 = 100
    for j in range(half_wv, lrows - half_wv):
        start_i = dmax + half_wh
        end_i = lcols - half_wh - dmax
        dp = np.zeros((lcols, dmax+1), dtype=np.float32)
        for d in range(dmax+1):
            dp[start_i][d] = cost_volume[j][start_i][d]
        for i in range(start_i + 1, end_i):
            prev_min = np.min(dp[i-1])
            for d in range(dmax+1):
                val = dp[i-1][d]
                if d > 0:
                    val = min(val, dp[i-1][d-1] + P1)
                if d < dmax:
                    val = min(val, dp[i-1][d+1] + P1)
                val = min(val, prev_min + P2)
                dp[i][d] = cost_volume[j][i][d] + val
        for i in range(start_i, end_i):
            best_d = np.argmin(dp[i])
            stereo[j][i] = best_d
            if min_disp is None or best_d < min_disp:
                min_disp = best_d
            if max_disp is None or best_d > max_disp:
                max_disp = best_d
    
    for j in range(half_wv, lrows - half_wv):
        for i in range(dmax + half_wh, lcols - half_wh - dmax):
            if max_disp != min_disp:
                stereo[j][i] = int(((stereo[j][i] - min_disp) / (max_disp - min_disp)) * 255)
            else:
                stereo[j][i] = 0
    stereo = np.array(stereo, dtype=np.uint8)
    cv2.imwrite("dynamic.pgm", stereo)


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