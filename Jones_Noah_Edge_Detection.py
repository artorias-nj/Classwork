import cv2
import os
import argparse
import numpy as np
import matplotlib.pyplot as plt

def main(filename, output_filename):
    img=cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    
    if img is not None:
        test=output_filename.split(".")
        if test[1] != "png" and test[1] != "jpg" and test[1] != "jpeg" and test[1] != "bmp" and test[1] != "tif" and test[1] != "tiff" and test[1] != "webp" and test[1] !="pgm":
            print("Error file type not supported")
        else:
            ed_type=input("Enter 'R' for Roberts, 'P' for Prewitt, 'S' for Sobel: ")
            if ed_type=="R":
                Kx = np.array([[1, 0], [0, -1]], dtype=np.float32)

                Ky = np.array([[0, 1], [-1, 0]], dtype=np.float32)

                gx = cv2.filter2D(img, cv2.CV_32F, Kx)
                gy = cv2.filter2D(img, cv2.CV_32F, Ky)

                roberts = np.sqrt(gx**2 + gy**2)
                roberts = cv2.normalize(roberts, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

                cv2.imwrite(output_filename,roberts)
                full_path = os.path.abspath(output_filename)
                print(f"Image saved to: {full_path}")
            elif ed_type=="P":
                Px = np.array([[ -1, 0, 1], [ -1, 0, 1], [ -1, 0, 1]], dtype=np.float32)

                Py = np.array([[  1,  1,  1], [  0,  0,  0], [ -1, -1, -1]], dtype=np.float32)

                gx = cv2.filter2D(img, cv2.CV_32F, Px)
                gy = cv2.filter2D(img, cv2.CV_32F, Py)

                prewitt = np.sqrt(gx**2 + gy**2)
                prewitt = cv2.normalize(prewitt, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

                cv2.imwrite(output_filename,prewitt)
                full_path = os.path.abspath(output_filename)
                print(f"Image saved to: {full_path}")
                
            elif ed_type=="S":
                
                gx = cv2.Sobel(img, cv2.CV_32F, 1, 0, ksize=3)
                gy = cv2.Sobel(img, cv2.CV_32F, 0, 1, ksize=3)

                sobel = np.sqrt(gx**2 + gy**2)
                sobel = cv2.normalize(sobel, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

                cv2.imwrite(output_filename,sobel)
                full_path = os.path.abspath(output_filename)
                print(f"Image saved to: {full_path}")
                
            else:
                print("Error please enter 'R', 'P', or 'S'")
            
            
        
    else:
        print("Error image could not be read")





if __name__== "__main__":
    parser=argparse.ArgumentParser(description="Program converts file to a different file type")
    parser.add_argument("filename", nargs="?", help="Enter input file name")
    parser.add_argument("output_filename", nargs="?", help="Enter output file name")
    
    parser.add_argument("--filename", dest="filename_opt",help="Enter input file name")
    parser.add_argument("--output_filename", dest="output_filename_opt",help="Enter output file name")
    
    args=parser.parse_args()
    
    filename = args.filename_opt or args.filename
    output_filename= args.output_filename_opt or args.output_filename
    while True:
        
        if filename is None:
            filename=input("What is the name of the file? (example.xxx): ")
            
        if output_filename is None:
            output_filename=output_file=input("What is the name of the output? (example.xxx): ")
            
        main(filename, output_filename)
        
        x=input("Would you like to go again? If not press 'Q' to quit: ")
        if x == "Q":
            break
        else:
            filename=None
            output_filename=None
    