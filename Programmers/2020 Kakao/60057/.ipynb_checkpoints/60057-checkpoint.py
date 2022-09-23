def solution(s):
    answer = len(s)
    for i in range(1, int(answer/2)):
        pos = 0
        length = len(s)
        
        while(True):
            unit = s[pos:i]
            pos += i
            
            if pos >= len(s): break
            
            cnt = 0
            
            while(True):
                if(unit == s[pos:i]):
                    cnt += 1
                    pos += i
                    
                else:   break
            if(cnt > 1):
                length -= i * (cnt-1);
                while(cnt):
                    length += 1;
                    cnt /= 10;
        answer = min(length, answer)
    return answer

s = ['aabbaccc', 'ababcdcdababcdcd', 'abcabcdede', 'abcabcabcabcdededededede', 'xababcdcdababcdcd']
for i in s:
    print(solution(i))

