import itertools
import time
from itertools import zip_longest
import itertools as it
from multiprocessing.pool import ThreadPool
from pprint import pprint

batch_size = 7
arr_len = 298937
start = time.time()
def performCalc(binaryArray):
    # perform some operation
    # rArray = blah * binaryArray
    # print('binaryArray',binaryArray)
    # del binaryArray[2:10]
    # print('del del_num[2:10]',binaryArray)
    # ls = []
    # if binaryArray[0]+binaryArray[1] in [3, 4, 18, 19]:
    #     ls.append(ls)
    return binaryArray

def grouper(iterable, n, padvalue=None):
    "grouper(3, 'abcdefg', 'x') --> ('a','b','c'), ('d','e','f'), ('g','x','x')"
    return zip_longest(*[iter(iterable)] * n, fillvalue=padvalue)

ls = []
def chunk():

# arr = [i for i in range(0, arr_len)]
    arr = list(it.permutations(list(itertools.islice(range(11), 1, 11)), 10))
    # print('arr',arr)
    print("grouper")
    start = time.time()
    ls = []
    for x in grouper(arr, batch_size):
        tmp = x
        # print(tmp)
        for i in tmp:
            # print('i',i)
            del_num = list(map(int, i))
            del del_num[2:10]
            if sum(del_num) in [3, 4, 18, 19]:
                ls.append(''.join(list(map(str, i))))
    return ls

def main():
    numberOfThreads = 20
    pool = ThreadPool(processes=numberOfThreads)
    greyScaleChunks = chunk()
    # print('greyScaleChunks',greyScaleChunks)
    results = pool.apply_async(performCalc, greyScaleChunks)
    pool.close()
    pool.join()  # Block until all threads exit.

    # Final results will be a list of arrays.
    # pprint(results.get())
# print('te,',tmp)
# for x in grouper(arr, batch_size):
#     tmp = x
#     # print(tmp)
#     for i in tmp:
#         # print('i',i)
#         del_num = list(map(int, i))
#         del del_num[2:10]
#         if sum(del_num) in [3, 4, 18, 19]:
#             ls.append(''.join(list(map(str, i))))
    # break

# print(ls)
# print(len(ls))
main()
print(time.time() - start)
# print(list(itertools.islice(range(11), 1, 11)))