#include <iostream>

using namespace std;

int edge = 0; 

int graph[20][20];
int visit[20];

void dfs(int node)
{
    visit[node] = 1;

    cout << node << endl;

    for (int i = 1; i < edge + 1; i++)
    {
        // 모든 edge에 연결된 노드에 대해 방문하지 않았다면...
        if(!visit[i] && graph[node][i]) dfs(i);
    }
}

int main()
{
    cin >> edge;

    for (int i = 0; i < edge; i++)
    {
        int input1, input2;
        cin >> input1 >> input2;

        graph[input1][input2] = 1;
        graph[input2][input1] = 1;
    }
    dfs(1);
}