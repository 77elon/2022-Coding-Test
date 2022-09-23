import numpy as np
import time

start = time.time()

file = open("input.txt")
input = file.readline
# input Number of Test Case
T = int(input())

for i in range(T):
    # Number of Coord
    N = int(input())
    # ary declare
    grad = np.empty(0, dtype=np.float16)
    # Result Variable
    result = 0
    # like grad, grad vs length what's the best?
    for n in range(N):
        # coord input
        p1, p2 = map(int, input().split())
        gradient = p1 / p2
        if p1 > p2:
            gradient *= -1.0
        grad = np.append(grad, gradient)
    # Gradient cmp
    for c in range(N):
        # Gradient indexing
        idx = np.where(grad != grad[c])
        # For tuple counting
        idx = np.array(idx).reshape(-1)
        if(result < idx.shape[0]): result = idx.shape[0]
        # Found the best results
        if(result == N - 1): break;
        #print(result, idx.shape[0], len(idx))
    print("#{} {}".format(i + 1, result))

end = time.time()
# Time Complexity: N(input) + N * O(1) -> 2N or less
print(f"{end - start:.5f} sec")
