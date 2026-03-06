
import cv2
import numpy as np
import argparse

def occupancy_grid(input_file, output_file):
    img = cv2.imread(input_file, cv2.IMREAD_GRAYSCALE)
    grid = (img > 127).astype(np.uint8) * 255
    cv2.imwrite(output_file, grid)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    occupancy_grid(args.input, args.output)
