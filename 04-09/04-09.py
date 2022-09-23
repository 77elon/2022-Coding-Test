import numpy as np
import sys
import math
import time

start = time.time()

file = open("input.txt")
input = file.readline
# input Number of Test Case
T = int(input())

result = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]

for i in range(T):
    # input Number of Student 
    # Which Student?
    N, K = map(int, input().split()) 
    multiplyer = N / 10
    stor = np.empty(0, dtype='float')
    for n in range(N):
        score = np.empty(0)
        score = np.array(input().split(), dtype='float')

        # calc midterm, final, submission score
        #print(score, type(score))
        # length is [0][3] 
        #print(score.shape)
        # Score <- Temp Array
        score[0] *= 0.35
        score[1] *= 0.45
        score[2] *= 0.2
        
        stor = np.append(stor, np.sum(score))
        #print('stor:', stor, stor.shape)
    
    # Rank Descend for Sorting
    rank = np.argsort(stor)[::-1][:N]
    #print("rank: ", rank)

    #print(i + 1, K - 1, rank)
    # Rank[0] is Highest Value index -> Found 
    loc = np.argwhere(rank == K - 1)
    print("#{} {}".format(i + 1, result[int(loc / multiplyer)]))

# Time Complexity is nlogn + n    
end = time.time()
print(f"{end - start:.5f} sec")
