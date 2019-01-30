#!/usr/bin/env python3

import cv2 as cv
import time
import sys

if __name__ == '__main__':

    # arguments
    if len(sys.argv) != 7:
        print("usage:", sys.argv[0], "<filename> <outfile> <flou gaussien> <sigma> <Canny min> <Canny max>")
        sys.exit(-1)
    FILENAME = sys.argv[1]
    OUTFILE = sys.argv[2]
    GAUSSIEN_BLUR = int(sys.argv[3])
    SIGMA = float(sys.argv[4])
    CANNY_MIN = int(sys.argv[5])
    CANNY_MAX = int(sys.argv[6])


    t0 = time.time()
 
    cap = cv.VideoCapture(FILENAME)  # lit depuis un fichier
    # cap = cv.VideoCapture(0)

    # flux de sortie (fichier)
    fourcc = cv.VideoWriter_fourcc(*'MPEG')
    fps = cap.get(cv.CAP_PROP_FPS)
    width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
    out = cv.VideoWriter(OUTFILE, fourcc, fps, (width, height))

    while(cap.isOpened()):
        ret, frame = cap.read()
        frame = cv.GaussianBlur(frame, (GAUSSIEN_BLUR, GAUSSIEN_BLUR), SIGMA)
        frame = cv.Canny(frame,CANNY_MIN, CANNY_MAX)
        if not ret:
            break

        out.write(frame)
        cv.imshow('bmx', frame)
        if cv.waitKey(30) == 27:
            break


    t1 = time.time()