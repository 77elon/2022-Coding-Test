#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(string s) {
    int answer = s.length();
    // 최대 2n 까지
    for (int i = 1; i < s.length() / 2; i++)
    {
        int pos = 0;
        int len = s.length();

        while(true)
        {
            // 기준점으로부터(pos) 압축 길이(i)만큼 추출한다.
            string unit = s.substr(pos, i);
            // 다음 탐색을 위한 pos 재설정
            pos += i;

            // 만약 설정한 pos가 압축 길이를 초과한다면 중단한다.
            if (pos >= unit.length()) break;

            int cnt = 0;

            while(true)
            {
                if(unit.compare(s.substr(pos, i)) == 0)
                {
                    cnt++;
                    pos += i;
                }
                else break;
            }
           if(cnt > 1) {
                len -= i * (cnt-1);
                while(cnt){
                    len++;
                    cnt/=10;
                }
           }
        }
        //answer = min(answer, len);
        answer = answer > len ? len : answer;
    }
    
    return answer;

}

int main()
{
    string ary[5] = {"aabbaccc", "ababcdcdababcdcd", "abcabcdede", "abcabcabcabcdededededede", "xababcdcdababcdcd"};
    for (const auto &t : ary)
    {
        cout << solution(t) << endl;
    }
}