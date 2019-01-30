#!/usr/bin/env python3

import cv2 as cv
import time
import sys



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

    def onChange(newValue):
        imgOut = imgIn.copy()
        grayscaled = cv.cvtColor(imgOut, cv.COLOR_BGR2GRAY)
        _, threshold = cv.threshold(grayscaled, newValue, 255, cv.THRESH_BINARY_INV)
        cv.imshow("threshold", threshold)

    # display image 
    
    cv.namedWindow("threshold")
    cv.createTrackbar("trackbar", "threshold", 0, 100, onChange)

    while True:
        k = cv.waitKey(25) & 0xFF
        if (k == 27):
            break