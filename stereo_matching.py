import os
import argparse
def read_img(filename):
    f = open(filename, "rb")
    magic = f.readline().decode().strip()
    line = f.readline().decode()
    while line.startswith("#"): 
        line = f.readline().decode()
    cols, rows = map(int, line.split())
    mgl = int(f.readline().decode())
    img = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(int.from_bytes(f.read(1), 'big'))
        img.append(row)
    f.close()
    return img, rows, cols, mgl

def write_image(filename, image, rows, cols, mgl):
    x=filename.split(".")
    if len(x)==1:
        filename=filename+".pgm"
    elif len(x)==2:
        x.pop()
        x.append(".pgm")
        filename="".join(x)
    else:
        print("error to many .")
        sys.exit(0)
    f=open(filename,"wb")
    magic="P5"
    img_header = f"{magic}\n{cols} {rows}\n{mgl}\n"
    f.write(img_header.encode())
    for i in range(0, int(rows)):
        for j in range(0, int(cols)):
            x=image[i][j].to_bytes(1, 'big')
            f.write(x)
    f.close()

def main(left_image_name, right_image_name):
    limg, lrows, lcols, lmgl = read_img(left_image_name)
    rimg, rrows, rcols, rmgl = read_img(right_image_name)
    dmax = 20
    wv = 20
    wh = 20
    half_wv = wv // 2
    half_wh = wh // 2
    stereo = [[0]*lcols for _ in range(lrows)]
    for j in range(half_wv, lrows-half_wv):
        for i in range(dmax + half_wh, lcols - half_wh - dmax):
            best_cost = float('inf')
            best_d = 0
            for d in range(0, dmax+1):
                acc = 0
                for l in range(-half_wv, half_wv+1):
                    for k in range(-half_wh, half_wh+1):
                        diff = limg[j+l][i+k] - rimg[j+l][i-d+k]
                        acc += diff * diff
                if acc < best_cost:
                    best_cost = acc
                    best_d = d
            stereo[j][i] = min(255, int(best_d * 255 / dmax))
    write_image("Stereo_"+left_image_name, stereo, lrows, lcols, lmgl)
   


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