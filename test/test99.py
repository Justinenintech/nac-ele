import itertools
import time
from itertools import zip_longest
import itertools as it

batch_size = 7
arr_len = 298937
numss = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# def performCalc(binaryArray):
#     # perform some operation
#     # rArray = blah * binaryArray
#     print('binaryArray',binaryArray)
#     return binaryArray
start = time.time()
# def grouper(iterable, n, padvalue=None):
#     "grouper(3, 'abcdefg', 'x') --> ('a','b','c'), ('d','e','f'), ('g','x','x')"
#     return zip_longest(*[iter(iterable)] * n, fillvalue=padvalue)
#
# ls = []
#
# arr = list(it.permutations(numss, 10))
# cs = []
# for i in set(it.permutations(numss, 10)):
#     # print('i',i)
#     if i[0]==1:
#         cs.append(i)
    # break
# print('arr',arr)
# for x in grouper(arr, batch_size):
#     tmp = x
#     # print(tmp)
#     for i in tmp:
#         # print('i',i)
#         del_num = list(map(int, i))
#         del del_num[2:10]
#         if sum(del_num) in [3, 4, 18, 19]:
#             ls.append(''.join(list(map(str, i))))
#     # break
#
# # print(ls)
# print(len(ls))

# print(list(itertools.islice(range(11), 1, 11)))


bonus_one = [3, 4, 18, 19]
print(set(list(it.permutations(numss, 2))))
for i in set(list(it.permutations(numss, 2))):
    # print('i',i)
    # print('sum',sum(i))
    if bonus_one.__contains__(sum(i)):
        print('i', i)
    # if sum

# l=[1,2,3]
# l.__contains__(3)
#
# print('l',l.__contains__(3))

l = {1, 2, 3}
# l.__contains__({2,3})

print('l', l.__contains__({2, 3}))

from collections import deque

d = deque(['a', 'b', 'c', 'd', 'e', 'f'])
for i in d:
    print(i)
print(d)
print(len(d))  # 获取双端队列的长度

# file=open('data.txt','w')
# file.write(str(cs))
# file.close()

with open('data.txt', 'r') as f:
    data = f.readlines()  # txt中所有字符串读入data
    print('data',''.join(list(data)[0]))
    print('data', type(''.join(list(data)[0])))
    # for i in list(data)[0]:
    #     print('i',i)
# ls = []
# for i in data:
#     # print('i',i)
#     for v in list(i):
#         print('v',v)
    # del_num = list(map(int, i))
    # del del_num[2:10]
    # if sum(del_num) in [3, 4, 18, 19]:
    #     ls.append(''.join(list(map(str, i))))
print(time.time() - start)
