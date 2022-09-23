import numpy as np
import time

start = time.time()

file = open("./20291/input.txt")
input = file.readline
# input Number of Test Case
T = int(input())

stor = np.empty((T, 0), dtype=np.string_)

for i in range(T):
    stor = np.append(stor, input().strip('\n').split(sep='.')[1])
    
uq = np.unique(stor)

for s in uq:
    print(s, " ", stor.tolist().count(s))

end = time.time()
# Time Complexity: N(input) + N * O(1) -> 2N or less
print(f"{end - start:.5f} sec")
