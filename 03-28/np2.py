import numpy as np

result = 0
next_index = 0

def calc(ary):
    global result, next_index
    ary_max = np.max(ary)
    arg_max = np.argmax(ary)
    
    #for Slicing
    next_index = arg_max + 1
    temp = (ary_max - ary[:next_index])
    result += np.sum(temp)


T = int(input())

for i in range(T):
    result = 0
    next_index = 0

    N = int(input())
    stor = np.empty(0)
    stor = np.array(input().split(), dtype='int')
    
    while(len(stor) != next_index): # same as range N
        stor = stor[next_index:]
        #end num is biggest
        calc(stor)

    print("#{} {}".format(i + 1, result))