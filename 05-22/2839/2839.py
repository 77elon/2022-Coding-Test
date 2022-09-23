# 담을 수 있는 설탕 봉지를 큰 순서대로 저장하였음
sugar_bag = [5, 3]

sugar = int(input())

# 설탕 봉지에 대한 접근 인덱스 <- 한 번만 해당 설탕 봉지에 접근 할 일은 없을 것이므로.
idx = 0

# 설탕 봉지의 총 개수가 저장되는 공간이다.
num = 0

# 이는 무한 루프를 막기 위한, 그리고 논리적 확인 절차를 위한 변수다.
# 위에서 설탕 봉지에 대한 계산이 수행 될 경우 flag가 1이 된다.
flag = 0

# 현재 인덱스가 배열의 범위를 초과하지 않으며, 설탕이 모두 봉지에 담아질 경우에 반복을 중단한다.
while(idx != len(sugar_bag) and sugar != 0):
    #print(sugar, sugar % sugar_bag[idx] != 0)
    # sugar % sugar_bag[idx]가 0이 아니라면,,, 다음 계산에서 문제가 생길 것이다.
    # 간단하게 가장 큰 설탕 봉지부터 담는다.
    if(sugar >= sugar_bag[idx]):
        sugar -= sugar_bag[idx]
        num += 1
        # 작업이 수행되었으므로, flag를 1로 바꿔주었다.
        flag = 1
    # 현재 설탕 봉지보다 값이 작다면... 
    else:
        # 현재 설탕 봉지에 값이 들어가지 않으며, 다음 설탕 봉지에도 부합하지 않는 경우.
        # -1 처리를 해준다.
        if sugar_bag[idx] == 3 and sugar % sugar_bag[idx] != 0:
            num = -1
            break
        if sugar % sugar_bag[idx + 1] != 0:
            # 반대로 현재 설탕 봉지에 담기긴 하지만, 다음 설탕 봉지를 사용해도, 설탕 봉지에 딱 맞게 값을 넣을 수 없는 경우.
            # is operated 
            if flag == 1:
                # 설탕 봉지에 설탕을 담기 전으로 값을 복원해준다.
                num -= 1
                sugar += sugar_bag[idx]
                flag = 0
                
        idx += 1

print(num)