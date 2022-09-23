#include <iostream>
#include <numeric>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int num;
    cin >> num;

    vector<int> stor;
    int result = 0;

    // Vector를 사용하여, 입력 받으며, 동시에 결과 계산을 위해 덧셈 진행.
    for (int i = 0; i < num; i++)
    {
        int temp;
        cin >> temp;
        result += temp;
        stor.push_back(temp);
    }

    // 첫 번째 입력 값을 기반으로 수행되므로, 임시로 값을 복사해둠.
    int jw = stor.at(0);
    
    // python의 argsort와 같은 역할을 하는 함수.
    vector<size_t> idx(stor.size());
    iota(idx.begin(), idx.end(), 0);
    stable_sort(idx.begin(), idx.end(), [&stor](size_t i1, size_t i2) {return stor[i1] < stor[i2];});

    // range based for, idx 값의 iterator를 기반으로 size() 만큼 반복한다.
    for(const auto &t : idx)
    {
        // 만약 jw의 인덱스에 도달하였다면, 건너띄도록 하였다,
        if(!t)
        {
            continue;
        }
        
        if(jw > stor.at(t))
        {
            jw += stor.at(t);
        }
    }

    if (jw == result)
    {
        cout << "Yes" << endl;
    }
    else
    {
        cout << "No" << endl;
    }
}