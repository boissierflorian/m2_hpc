#!/usr/bin/env python3

import cv2 as cv
import time
import sys

if __name__ == '__main__':

    # arguments
    if len(sys.argv) != 5:
        print("usage:", sys.argv[0], "<filename> <outfile> <factor> <nbrun>")
        sys.exit(-1)
    FILENAME = sys.argv[1]
    OUTFILE = sys.argv[2]
    FACTOR = float(sys.argv[3])
    NB_RUN = int(sys.argv[4])

    # load input image
    imgIn = cv.imread(FILENAME)
    if imgIn.size == 0:
        print("failed to load", FILENAME)
        sys.exit(-1)

    # compute output image
    t0 = time.time()
    #imgOut = imgIn / 2

    # blur
    imgOut = None
    for i in range(NB_RUN):
        imgOut = FACTOR * (imgIn / 255)

    t1 = time.time()

    # outputs
    print("time:", t1-t0, "s")
    #cv.imwrite(OUTFILE, imgOut)
    print(imgIn)
    print(imgOut)

    # display image
    cv.imshow("image kermorvan_factor.png", imgOut)

    # waiting for esc to quit
    while True:
        k = cv.waitKey(25) & 0xFF
        if (k == 27):
            break

