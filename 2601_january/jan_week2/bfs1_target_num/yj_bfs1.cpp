#include <string>
#include <vector>
#include <iostream>

using namespace std;

int answer = 0;

// 재귀
void recur(int current, int index, int target, vector<int> numbers) {  // 현재까지 더한 값, numbers의 인덱스, 타겟 값, numbers
    int result = 0;
    // 다 뽑으면 멈추기, target과 같으면 answer값 +1
    if(index == numbers.size()) {  // numbers의 size만큼 다 뽑았으면 값이 target과 같은지 비교
        if(current == target) {
            answer++;
            return;    
        } else {
            return;
        }
    }
    
    // 재귀 파트
    // + 뽑기
    recur(current + numbers[index], index + 1, target, numbers);
    // - 뽑기
    recur(current - numbers[index], index + 1, target, numbers);
}

int solution(vector<int> numbers, int target) {
    recur(0, 0, target, numbers); // length()는 string 전용. vector는 size()를 사용해야 한다.
    return answer;
}