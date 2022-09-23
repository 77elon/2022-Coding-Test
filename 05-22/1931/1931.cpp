#include <iostream>

using namespace std;

int main()
{
    int count;
    cin >> count;

    int temp2 = 0;
    int result = 0;

    for (int i =0; i < count; i++)
    {
        int num1, num2;

        cin >> num1 >> num2;
        // 입력된 회의 시작시간이 이전에 입력된 종료 시간보다 크거나 같아야 한다.
        if(temp2 <= num1)
        {
            temp2 = num2;
            result += 1;
        }
    }
    cout << result << endl;
}