#include <iostream>
#include <string.h>

using namespace std;

int island[50][50];
int edge[50][50];

int num = 0;
int result[50];

int size_w = 0;
int size_h = 0;

void dfs(int height, int width)
{
    edge[height][width] = 1;

    for (int h = -1; h <= 1; h++)
    {
        for (int w = -1; w <= 1; w++)
        {
            if (width + w < 0 || width + w >= size_w || height + h < 0 || height + h >= size_h || (h == w && h == 0)) continue;
            if (edge[height + h][width + w] == 0 && island[height + h][width + w] == 1)
            {
                //num++;
                //cout << "Execute 1" << endl;
                dfs(height + h, width + w);
            }
        }
    }
}


int main()
{
    memset(result, 0, sizeof(result));
    while (true)
    {
        memset(edge, 0, sizeof(edge));
        memset(island, 0, sizeof(island));
        cin >> size_w >> size_h;
        if (size_h == size_w && size_h == 0) break;
        for (int i = 0; i < size_h; i++)
        {
            for (int j = 0; j < size_w; j++)
            {
                cin >> island[i][j];
                // 0 or 1
                //cout << i << j << endl;
            }
        }
        for (int i = 0; i < size_h; i++)
        {
            for (int j = 0; j < size_w; j++)
            {
                if (island[i][j] == 1 && edge[i][j] == 0)
                {
                    dfs(i, j);
                    result[num] += 1;
                }
            }
        }
        //cout << num << endl;
        num += 1;
    }
    for (int i = 0; i < num; i++)
    {
        cout << result[num] << endl;
    }
}