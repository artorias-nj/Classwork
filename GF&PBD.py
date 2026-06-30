import os
import argparse
import cv2
import numpy as np
from scipy.signal import convolve
import matplotlib.pyplot as plt

def gabor_1d(x, sigma, f0):
    return np.exp(-(x**2)/(2*sigma**2)) * np.exp(1j*2*np.pi*f0*x)


def main(left_image_name, right_image_name):
    L = cv2.imread(left_image_name, 0).astype(float)
    R = cv2.imread(right_image_name, 0).astype(float)

    row = L.shape[0] #// 2    take one scanline
    image=np.zeros_like(L)
    x = np.arange(-20, 21)
    sigma = 5
    f0 = 0.1
    g = gabor_1d(x, sigma, f0)
    
    plt.plot(np.real(g))
    plt.title("Real part of Gabor")
    plt.show()

    plt.plot(np.imag(g))
    plt.title("Imaginary part of Gabor")
    plt.show()
    
    for i in range (row):
        L_row = L[i, :]
        R_row = R[i, :]
        
        
        
        R_L = convolve(L_row, g, mode='same')
        R_R = convolve(R_row, g, mode='same')
        
        phi_L = np.angle(R_L)
        phi_R = np.angle(R_R)
        
        """plt.plot(phi_L, label="Left")
        plt.plot(phi_R, label="Right")
        plt.legend()
        plt.title("Phase")
        plt.show()"""
        
        delta_phi = phi_R - phi_L
        
        delta_phi = np.angle(np.exp(1j * delta_phi))
        
        d = -delta_phi / (2 * np.pi * f0)
        image[i, :] = d
    plt.imshow(image)
    plt.title("Disparity Map")
    plt.colorbar()
    plt.show()
    

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