def solution(s):
    n = len(s)
    result = 1001
    # i 단위로 자른다.
    for i in range(1, n+1):
        # 압축 단위 수
        cnt = 1
        # 단위가 i 일 때 압축한 문자열
        tmp = ''    
        # 비교를 위한 i개 문자열 추출
        before_c = s[:i]

        # i부터 i 단위로 자름
        # 이를 기반으로 2번째 압축 문자열부터 문자열 전체 길이까지 탐색한다.
        for j in range(i, n, i):
            c = s[j:j+i]

            # i로 추출된 문자열과 중복되는 경우
            if before_c == c:
                cnt += 1
            # 중복되지 않은 경우
            else:
                # 단지 1개 밖에 없는 경우.
                if cnt == 1:
                    tmp += before_c
                else:
                    # 2개 이상 발견된 경우.
                    tmp += (str(cnt)+before_c)
                cnt = 1
                before_c = c

        if cnt == 1:
            tmp += before_c
        else:
            tmp += (str(cnt)+before_c)
        # 가장 짧은 문자열의 길이값을 result로
        result = min(result, len(tmp))
    return result

s = ['aabbaccc', 'ababcdcdababcdcd', 'abcabcdede', 'abcabcabcabcdededededede', 'xababcdcdababcdcd']
for i in s:
    print(solution(i))

