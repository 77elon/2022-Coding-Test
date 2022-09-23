temp = input()

# 값을 저장하는 원소 배열과 부호 배열에 대해 선언.
ele = [] 
operator = []

# 결과 값을 저장하는 변수
idx = 0

# idx가 temp의 길이를 초과하지 않을 경우까지만... for range <- 초기 선언한 iteration 만큼 수행되므로, 원하는 답이 안나온다.
while len(temp) != idx:
    # 만약 부호를 발견했다면....
    if temp[idx] == '+' or temp[idx] == '-':
        # 값을 저장해주며, 부호도 따로 저장해준다.
        ele.append(int(temp[:idx]))
        operator.append(temp[idx])
        # Slicing을 사용하여, 값을 분리한다.
        temp = temp[idx + 1:]
        idx = 0
    idx += 1

# 마지막 수를 저장해준다.
ele.append(int(temp))

# 만약 - 부호가 존재하고, 이후 또 다른 부호가 있다면.. - 해준다.
# 이는 Greedy한 풀이 방식이 아니다... 논리적인 풀이방식이다...
for i in range(len(operator)):
    if operator[i] == '-':
        operator[i + 1:] = '-'
        break

# 초기 값에 대한 부호가 존재하지 않으므로....
result = ele[0]

# 부호의 개수 만큼 값을 계산한다.
# 각 +, - 부호에 맞게 값을 저장한다.
for i in range(len(operator)):
    if operator[i] == '+':
        result += ele[i + 1]
    elif operator[i] == '-':
        result -= ele[i + 1]

print(result)
