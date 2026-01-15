// 재귀 & 그래프
#include <string>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

// 각 공항에서 갈 수 있는 목적지들을 담을 map
map<string, vector<string>> adj;
vector<string> ans;

void dfs(string cur) {
    // 현재 공항에서 갈 수 있는 티켓이 남아있는 동안 반복
    while(!adj[cur].empty()) {
        string nxt = adj[cur].back();  // 정렬된 것 중 가장 앞선 것(뒤에 있음) 선택
        adj[cur].pop_back(); // 사용한 티켓 제거
        dfs(nxt); // 다음 공항으로 이동
    }
    // 더 이상 갈 곳이 없으면 현재 공항을 경로에 추가 (역순으로 쌓임)
    ans.push_back(cur);
}

vector<string> solution(vector<vector<string>> tickets) {
    // 1. 그래프 구성
    for(auto& t : tickets) {
        adj[t[0]].push_back(t[1]);
    }
    
    // 2. 목적지 리스트를 내림차순 정렬 (back()으로 꺼내면 알파벳 순서가 됨)
    for(auto& airport : adj) {
        sort(airport.second.begin(), airport.second.end(), greater<string>());
    }
    
    // 3. ICN 공항에서 DFS 시작
    dfs("ICN");
    
    // 4. 역순으로 담긴 경로를 올바른 순서로 뒤집기
    reverse(ans.begin(), ans.end());
    
    return ans;
}