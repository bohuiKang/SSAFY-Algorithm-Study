#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> answers) {
    vector<int> answer;
    
    // 1. 수포자들 패턴 정의
    vector<int> p1 = {1, 2, 3, 4, 5};
    vector<int> p2 = {2, 1, 2, 3, 2, 4, 2, 5};
    vector<int> p3 = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
    
    // 2. 맞힌 개수를 저장할 배열
    vector<int> score(3, 0);  // {0, 0, 0}
    
    // 3. 정답과 비교
    for(int i = 0; i < answers.size(); i++) {
        if(answers[i] == p1[i % p1.size()]) score[0]++;  
        if(answers[i] == p2[i % p2.size()]) score[1]++;  
        if(answers[i] == p3[i % p3.size()]) score[2]++;  
    }
    
    // 4. 가장 높은 점수 찾기
    int max_score = max({score[0], score[1], score[2]});
    
    // 5. 최고 점수와 같은 수포자 번호 담기(1번부터 순서대로 확인하므로 자동 오름차순)
    for (int i = 0; i < 3; i++) {
        if(score[i] == max_score) {
            answer.push_back(i + 1);
        }
    }
        
    return answer;
}