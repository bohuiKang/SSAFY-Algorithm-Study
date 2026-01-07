#include <string>
#include <vector>
#include <set>

using namespace std;

set<int> candidates;  // 중복 제거

// 소수인지 판별
bool isPrime(int num) {
    if (num < 2) return false;
    
    for (int i = 2; i * i <= num; i++) {
        if (num % i == 0) return false;
    }
    return true;
}

// numbers = 남은 숫자들, current = 지금까지 만든 숫자
void backtrack(string numbers, string current) {
    // 지금까지 만든 숫자를 저장
    if (!current.empty()) {
        candidates.insert(stoi(current));  // stoi: 문자열을 정수로 변환
    }
    
    // numbers에 남은 각 숫자에 대해
    for (int i = 0; i < numbers.length(); i++) {
        // numbers[i]를 선택해서 current에 추가
        // 남은 숫자들(numbers[i] 제외)로 계속 만들기
        string remaining = numbers.substr(0, i) + numbers.substr(i + 1);  // substr: 파이썬의 슬라이싱
        backtrack(remaining, current + numbers[i]);
    }
}

int solution(string numbers) {
    backtrack(numbers, "");
    
    int answer = 0;
    for (int num : candidates) {
        if (isPrime(num)) answer++;
    }
    return answer;
}