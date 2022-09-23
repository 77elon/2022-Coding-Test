import numpy as np
import time

start = time.time()

file = open("sample_input.txt")
input = file.readline
# input Number of Test Case
T = int(input())

stor = np.empty((T, 0), dtype=np.uint)
for i in range(T):

    # Escape Deletion
    temp = np.array(list(str(int(input())))).astype('int')

    # 인덱스의 최소, 최대 값을 추출하기 위해..
    rank = np.argsort(temp)
    
    # 크기 순서대로 정렬 된, rank 배열의 시작 인덱스는 가장 작은 인덱스 번호일 것이며, 반대는 가장 큰 인덱스 번호일 것이다.
    max_idx = rank[-1]
    min_idx = rank[0]
    sec_min_idx = rank[1]
    sec_max_idx = rank[-2]

    print(max_idx, min_idx, sec_min_idx, sec_max_idx)

    max_val = temp.copy()
    min_val = temp.copy()

    # Max <-> Min value swap
    if max_val[max_idx] != 0 : 
        max_val[0] = temp[max_idx]
        max_val[max_idx] = temp[0]
    print("max_val: ", max_val)

    # 가장 앞 자리가 0이 되면 안되므로... 0이 없다면... 일반적으로 시행

    if min_val[min_idx] != 0:
        min_val[0] = temp[min_idx]
        min_val[min_idx] = temp[0]

    if min_val[min_idx] == 0: 
        # 최고 자리 숫자가 2번째로 작은 숫자라면...
        # 두 번째로 작은 숫자와 0의 자리를 바꿔준다...
        if min_idx == 0:
            min_val[0] = temp[sec_min_idx]
            min_val[sec_min_idx] = temp[0]
        # 최소 값이 0이면서, 최고 자릿 수가 2번째로 작은 숫자가 아닌 경우
        else: #min_val[min_idx] == 0 & sec_min_idx != 0:
            min_val[0] = temp[sec_min_idx]
            min_val[sec_min_idx] = temp[0]

    print("min_val: ", min_val)

    #print("#{} {} {}".format(i + 1, min_val, max_val))

end = time.time()
# Time Complexity: N(input) + N * O(1) -> 2N or less
print(f"{end - start:.5f} sec")
