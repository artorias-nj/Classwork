import cv2
import sys

def convert_to_pgm(input_path, output_path):
    # Read the image
    img = cv2.imread(input_path)

    if img is None:
        print("Error: Could not open image.")
        return

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Save as PGM
    cv2.imwrite(output_path, gray)

    print(f"Saved PGM image to {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python convert_to_pgm.py input_image output.pgm")
    else:
        convert_to_pgm(sys.argv[1], sys.argv[2])