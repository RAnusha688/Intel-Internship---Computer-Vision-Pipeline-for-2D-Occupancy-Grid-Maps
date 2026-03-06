
import cv2
import argparse

def preprocess(input_file, output_file):
    img = cv2.imread(input_file, cv2.IMREAD_GRAYSCALE)
    img = cv2.GaussianBlur(img, (5,5), 0)
    cv2.imwrite(output_file, img)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    preprocess(args.input, args.output)
