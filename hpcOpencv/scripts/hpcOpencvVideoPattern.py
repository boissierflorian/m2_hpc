#!/usr/bin/env python3

import cv2 as cv
import time
import sys

if __name__ == '__main__':

    # arguments
    if len(sys.argv) != 4:
        print("usage:", sys.argv[0], "<filename> <pattern> <TM_CCOEFF_NORMED>")
        sys.exit(-1)

    FILENAME = sys.argv[1]
    PATTERN = sys.argv[2]
    THRESHOLD = sys.argv[3]

    # lit depuis un fichier
    cap = cv.VideoCapture(FILENAME)  

    # Motif
    patternImg = cv.imread(PATTERN)
    if patternImg.size == 0:
        print("failed to load", PATTERN)
        sys.exit(-1)
    
    w, h, _ = patternImg.shape[::-1]

    # Lecture de la vidéo
    i = 0
    while(cap.isOpened()):
        ret, frame = cap.read()
        if not ret:
            break

        result = cv.matchTemplate(frame, patternImg, cv.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

        print("frame={}, maxVal={}, maxLoc={}".format(i, max_val, max_loc))

        top_left = max_loc
        bottom_right = (top_left[0] + 50, top_left[1] + 30)

        if max_val > 0.7:
            cv.rectangle(frame, top_left, bottom_right, 255, 2)

        cv.imshow('pattern matching', frame)
        if cv.waitKey(30) == 27:
            break

        i = i + 1

    print("..")

