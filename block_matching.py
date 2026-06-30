import cv2
import os
import argparse

def block(left_image_name, right_image_name):
    limg=cv2.imread(left_image_name, cv2.IMREAD_GRAYSCALE).astype(int)
    rimg=cv2.imread(right_image_name, cv2.IMREAD_GRAYSCALE).astype(int)
    block_img=limg.copy()
    if limg is not None and rimg is not None:
        lin=left_image_name.split(".")
        rin=right_image_name.split(".")
        name="block_"+lin[0]+"+"+rin[0]+".pgm"
        lrows = limg.shape[0]
        lcols = limg.shape[1]
        rrows = rimg.shape[0]
        rcols = rimg.shape[1]
        w=9
        h=9
        dmin=0
        dmax=10
        for i in range(h//2, lrows-h//2):
            for j in range(w//2, lcols-w//2):
                avgl=0
                for l in range ((-(h//2)), (h//2+1)):
                    for k in range ((-(w//2)), (w//2+1)):
                        avgl=avgl+ limg[i+k, j+l]
                avgl=avgl//(w*h)
                cost_min=None
                d_best=None
                for d in range (dmin, dmax):
                    avgr=0
                    count = 0
                    for x in range ((-(h//2)), (h//2)):
                        for r in range ((-(w//2)), (w//2)):
                            if 0<=i+r-d<rrows:
                                avgr+=rimg[i+r-d,j+x]
                                count+=1
                    if count>0:
                        avgr=avgr//(w*h)
                    cost = 0
                    for l in range(-(h//2), h//2+1):
                        for k in range(-(w//2), w//2+1):
                            if 0<=i+k-d< rrows:
                                cost += abs((limg[i+k, j+l] - avgl) - (rimg[i+k-d, j+l] - avgr))
                    if cost_min==None:
                        cost_min=cost
                        d_best=d
                    elif cost<cost_min:
                        cost_min=cost
                        d_best=d
                block_img[i, j] = d_best
        block_img = ((block_img - dmin) / (dmax - dmin)) * 255
        block_img = block_img.clip(0, 255)
        display_img = block_img.astype('uint8')
        cv2.imshow('block img', display_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        cv2.imwrite(name, display_img)
        
        
    else:
        print("Error image could not be read")

def main(left_image_name, right_image_name):
    block(left_image_name, right_image_name)
    block(right_image_name, left_image_name)

if __name__== "__main__":
    parser=argparse.ArgumentParser(description="Does block matching")
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