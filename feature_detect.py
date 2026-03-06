
import cv2
import argparse

def detect_features(input_file, output_file):
    img = cv2.imread(input_file, cv2.IMREAD_GRAYSCALE)
    edges = cv2.Canny(img, 100, 200)
    cv2.imwrite(output_file, edges)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    detect_features(args.input, args.output)
