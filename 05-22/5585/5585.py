# 모든 지불 금액은 1000원이라고 하였으므로...
money = 1000
# 추후 참조를 위해 거스름돈을 줄 수 있는 금액의 리스트를 작성하였음
charge_list = [500, 100, 50, 10, 5, 1]

price = int(input())
# 거스름돈의 정도를 알기 위해 총 잔돈을 계산함.
charge = money - price

# 거스름돈 단위를 계산하기 위한 idx 선언
idx = 0
# 잔돈의 개수를 저장한다.
charge_num = 0

# 단순히 모든 금액을 계산하기 위해, 가장 크게 거슬러 줄 수 있는 잔돈부터 count해준다.
while(idx != len(charge_list)):
    # 작동원리는 다음과 같다. 만약 총 거스름돈이 현재 인덱스의 거스름돈보다 크거나 같을 경우에.
    # 잔돈의 개수를 추가해주며, 총 거스름돈을 정리해준다.
    if charge >= charge_list[idx]:
        charge_num += 1
        charge -= charge_list[idx]
    # 만약 해당 조건에 부합하지 않는다면, 다음 순서의 큰 거스름돈을 가져와 계산해준다.
    else:
        idx += 1

# Greedy Algorithm에 부합하지 않는 풀이 방식이다.
# 단순하게 아주 직관적인 풀이지만, 결국 Locally Optimal Solution에 대한 검증이 수반되지 않았기 때문이다.

print(charge_num)