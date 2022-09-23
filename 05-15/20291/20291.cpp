#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int num;
    cin >> num;

    vector<string> stor;

    for (int i =0; i< num; i++)
    {
        string input;
        cin >> input;
        unsigned int index = input.find(".");
        // '.'의 위치를 기반으로 확장자의 위치를 알아내며, 동시에 확장자만 보관한다.
        input = input.substr(index + 1, input.size());
        stor.push_back(input);
    }
    // for unique, 
    sort(stor.begin(), stor.end());
    vector<string> uq = stor;
    uq.erase(unique(uq.begin(), uq.end()), uq.end());

    for (const auto &T : uq)
    {
        cout << T << "\t" << count(stor.begin(), stor.end(), T) << endl;
    }
}