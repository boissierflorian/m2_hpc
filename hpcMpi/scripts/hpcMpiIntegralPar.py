#!/usr/bin/env python3

import hpcMpi
import sys

from mpi4py import MPI
from time import time


if __name__ == '__main__':

    if len(sys.argv) != 3:
        print("usage:", sys.argv[0], "<radius> <step>")
        sys.exit(-1)

    RADIUS = int(sys.argv[1])
    step = int(sys.argv[2])

    comm = MPI.COMM_WORLD
    i = comm.Get_rank()
    n = comm.Get_size()
    ai = i / n
    bi = (i + 1) / n
    ri = hpcMpi.compute(hpcMpi.fPi, ai, bi, step)
    comm.Reduce()


    # read image
    image1 = hpcMpi.readPnm("backloop.pnm")
    if image1.size == 0:
        if worldRank == 0:
            print("error: failed to read pnm file")
        sys.exit(-1)
    height, width = image1.shape

    t0 = time()

    # compute blur
    if worldRank == 0:
        for i in range(1, worldSize):
            msg = comm.recv(source=i)
            print(i, "sent:", msg)
    else:
        x0, x1, y0, y1 = 0, width, 0, height  # the whole image
        # x0, x1, y0, y1 = 400, 1000, 100, 400  # only the guy doing backloop
        image2 = hpcMpi.blur(image1, RADIUS, x0, x1, y0, y1)
        
        data = {}
        comm.send(data, dest=0)


    t1 = time()

    # outputs
    hpcMpi.writePnm("output.pnm", image2)
    print(RADIUS, 1, t1-t0)
