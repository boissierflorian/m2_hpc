#!/usr/bin/env python3

import cv2 as cv
import time
import sys



def onChange(newValue, imgIn):
    print(newValue)
    cv.threshold(imgIn, 127, 255, cv.THRESH_BINARY)

if __name__ == '__main__':

    # arguments
    if len(sys.argv) != 2:
        print("usage:", sys.argv[0], "<filename>")
        sys.exit(-1)
    FILENAME = sys.argv[1]

    t0 = time.time()

    imgIn = cv.imread(FILENAME)
    if imgIn.size == 0:
        print("failed to load", FILENAME)
        sys.exit(-1)

    # display image 
    cv.imshow("image threshold.png", imgIn)
    cv.createTrackbar("trackbar", "image threshold.png", 0, 100, onChange)

    while True:
        k = cv.waitKey(25) & 0xFF
        if (k == 27):
            break