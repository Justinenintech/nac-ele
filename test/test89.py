import numpy as np
from pprint import pprint
from multiprocessing.pool import ThreadPool
import threading

blah = 2

def performCalc(binaryArray):
    # perform some operation
    rArray = blah * binaryArray
    return rArray

def main(data_array):
    numberOfThreads = 5
    pool = ThreadPool(processes=numberOfThreads)

    greyScaleChunks = np.array_split(data_array, numberOfThreads)
    results = pool.map_async(performCalc, greyScaleChunks)
    pool.close()
    pool.join()  # Block until all threads exit.

    # Final results will be a list of arrays.
    pprint(results.get())

grey_arr = np.array(range(50))
main(grey_arr)