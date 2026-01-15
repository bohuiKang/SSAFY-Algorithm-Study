#include <vector>
#include <queue>

using namespace std;

// 방문 여부 저장 배열
bool visited[205];

int solution(int n, vector<vector<int>> computers) {
    int answer = 0;
    
    for(int i = 0; i < n; i++) {
        // 이미 방문한 컴퓨터라면 건너뜀
        if(visited[i]) continue;
        
        // 새로운 네트워크 발견
        answer++;
        queue<int> Q;
        Q.push(i);
        visited[i] = true;
        
        // BFS 시작
        while(!Q.empty()) {
            int cur = Q.front(); Q.pop();
            
            for(int nxt = 0; nxt < n; nxt++) {
                // 자기 자신 제외
                if(cur == nxt) continue;
                // 연결되어 있는지 확인 & 미방문 확인
                if(computers[cur][nxt] == 1 && !visited[nxt]) {
                    visited[nxt] = true;
                    Q.push(nxt);
                }
            }
        } 
    }
    
    return answer;
}