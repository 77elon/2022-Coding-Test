#include <iostream>
#include <string.h>

using namespace std;
 
const int MAX = 50;
int w, h;
int map[MAX][MAX];
// 현재 이어져 있는지, 그리고 방문했는지와 같은 의미.
bool edge[MAX][MAX];

// 아래, 위, 왼쪽, 오른쪽, 왼쪽 위, 왼쪽 아래, 오른쪽 위, 오른쪽 아래
// 반복문, 조건을 사용해서 색인하게 하였지만, 결과가 제대로 나오지 않아, 해당 조건을 인터넷에서 참조하였음.
int dh[] = {1,-1,0,0,-1,1,-1,1};
int dw[] = {0,0,-1,1,-1,-1,1,1};

// m_count는 각 입력값의 크기가 되겠다.
int m_count = 0;

// 섬의 개수를 저장하는 배열
int result[MAX];
 
void dfs(int height, int width) {
    edge[height][width] = true;
    
    // 전역 배열로 선언한 위치 값과 메인함수에서 입력된 섬의 좌표에 대해,
    // 재귀 함수를 사용하여, 모든 방향의 섬이 존재하는지 확인한다.
    for (int i = 0; i < 8; i++) {
        int nh = height + dw[i];
        int nw = width + dh[i];

        // 만약 섬의 시작 좌표를 넘거나, 입력된 좌표를 초과한다면... 색인하지 않는다.
        if (nh < 0 || nw < 0 || nh >= h || nw >= w)
            continue;
        // 만약 현재 섬이 존재하며, 동시에 방문하지 않았다면... (edge가 연결되지 않았다면...)
        if (map[nh][nw] == 1 && edge[nh][nw] == 0) {
            dfs(nh, nw);
        }
    }
}
 
int main() {
    // 섬의 개수를 저장하는 배열 초기화
    memset(result, 0, sizeof(result));
    // 무한 반복문을 사용하여, 0, 0 입력에 대해서 프로그램을 종료시킨다.
    while (true) {
        // 매 반복문마다 들어오는 섬의 정보, 연결 정보를 초기화해준다.
        memset(map, 0, sizeof(map));
        memset(edge, false, sizeof(edge));

        cin >> w >> h;
        // 종료 선언.
        if (w == h && h == 0) break; 

        // 위에서 입력된 좌표에 맞춰 데이터를 입력 받는다.
        for (int i = 0; i < h; i++) 
        {
            for (int j = 0; j < w; j++) 
            {
                cin >> map[i][j];
            }
        }

        // 모든 좌표에 대해 섬이 존재하고 연결되지 않았다면... dfs 함수를 호출한다.
        for (int i = 0; i < h; i++) 
        {
            for (int j = 0; j < w; j++) 
            {
                if (map[i][j] == 1 && edge[i][j] == 0) 
                {
                    dfs(i, j);
                    // 결국 해당 조건이 만족해야 섬의 개수를 찾는 것이므로,,,
                    result[m_count] += 1;
                }
            }
        }
        // 반복문이 끝나는 것은 다음 데이터에 대한 섬을 불러오는 것이므로...
        m_count += 1;
    }
    for(int i = 0; i < m_count; i++)
    {
        cout << result[i] << endl;
    }
}
