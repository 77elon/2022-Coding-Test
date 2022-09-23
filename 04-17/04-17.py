import numpy as np
import time

start = time.time()

file = open("input.txt")
input = file.readline
# input Number of Test Case
T = int(input())

for i in range(T):
    # input Number of Coord
    N = int(input())
    # ary declare
    coord = np.empty((N, 2), dtype=np.uint)
    grad = np.empty(0, dtype=np.float16)
    # coord input
    # like grad, grad vs length calc?
    for n in range(N):
        p1, p2 = map(int, input().split())
        coord[n][0] = p1
        coord[n][1] = p2
        gradient = coord[n][0] / coord[n][1]
        
        if coord[n][0] > coord[n][1]:
            gradient *= -1.0
        grad = np.append(grad, gradient)
    result = 0
    # gradient cmp, c is tuple
    for c in range(coord.shape[0]):
        # Find diff gradient
        idx = np.where(grad != grad[c])
        # For tuple counting
        idx = np.array(idx).reshape(-1)
        if(result < idx.shape[0]): result = idx.shape[0]
        #print(result, idx.shape[0], len(idx))
    print("#{} {}".format(i + 1, result))



end = time.time()
print(f"{end - start:.5f} sec")
