import numpy as np

T = int(input())

for i in range(T):
    N = int(input())
    stor = np.empty(0)

    stor = np.array(input().split(), dtype='int')
    result = 0
    next_index = -1
    ary_max = np.max(stor)
    ary_min = np.min(stor)

    for c in range(len(stor)): # same as range N
        #최고가 일 때 무조건 판매...

        if stor[c] == ary_max and c != 0:
            temp = (ary_max - stor[:c])
            result += np.sum(temp)
            next_index = c + 1
            #print(next_index, result, "Execute 1")
        #중간 값일 때... 판매되지 않은 이전 날들의 제품만 모두 판매
        #라고 생각했으나, 위에서 도출된 next_index를 기반으로, 배열 슬라이싱을 통한 최대값을 찾아내는 방식.
        elif next_index < len(stor):
            
            if stor[c + 1] < stor[c]:
                temp = (stor[c] - stor[next_index:c])
                result += np.sum(temp)
                if(c + 1 == len(stor)):
                    break;
                else:
                    next_index = c + 1
                #print(next_index, result, "Execute 2")
        else: 
            temp = (stor[c] - stor[next_index:c])
            result += np.sum(temp)
            #print(next_index, result, "Execute 3")
    print("#{} {}".format(i + 1, result))
        