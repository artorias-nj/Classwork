import cv2 as cv
import os
import sys
import argparse
from matplotlib import pyplot as plt

def main(filename, output_filename):
    img=cv.imread(filename, cv.IMREAD_GRAYSCALE)

    if img is not None:
        test=output_filename.split(".")
        if test[1] != "png" and test[1] != "jpg" and test[1] != "jpeg" and test[1] != "bmp" and test[1] != "tif" and test[1] != "tiff" and test[1] != "webp":
            print("Error file type not supported")
            sys.exit()
        hist=cv.calcHist([img],[0], None, [256], [0,256])
        clahe = cv.createCLAHE()
        hist_img=clahe.apply(img)
        hist2=cv.calcHist([hist_img],[0], None, [256], [0,256])
        cv.imwrite(output_filename,hist_img)
        full_path = os.path.abspath(output_filename)
        print(f"Image saved to: {full_path}")
        plt.plot(hist)
        plt.title('Grayscale Histogram')
        plt.xlabel('Pixel Intensity')
        plt.ylabel('Number of Pixels')
        plt.xlim([0, 256])
        plt.show()
        plt.plot(hist2)
        plt.title('Grayscale Histogram')
        plt.xlabel('Pixel Intensity')
        plt.ylabel('Number of Pixels')
        plt.xlim([0, 256])
        plt.show()
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
    if filename is None:
        filename=input("What is the name of the file? (example.xxx): ")
        
    if output_filename is None:
        output_filename=output_file=input("What is the name of the output? (example.xxx): ")
        
    main(filename, output_filename)