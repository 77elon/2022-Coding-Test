import numpy as np
import time

start = time.time()

file = open("./22993/input.txt")
input = file.readline
# input Number of Test Case
T = int(input())

stor = np.empty((0), dtype=np.uint)

for i in range(T):
    stor = np.append(stor, input().split())
stor = stor.astype(np.uint)
#print(stor)
jw = stor[0]

rank = stor.argsort()
rank = rank[np.where(rank != 0)]

for i in rank:
    if(jw > stor[i]):
        jw += stor[i]
print(jw == np.sum(stor))
end = time.time()
# Time Complexity: N(input) + N + nlog(n)-> 2N ++
print(f"{end - start:.5f} sec")
