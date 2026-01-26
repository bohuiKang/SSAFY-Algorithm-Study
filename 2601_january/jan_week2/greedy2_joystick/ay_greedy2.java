class Solution {
    public int solution(String name) {
        int answer = 0;
        int A_to_ch, Z_to_ch, min_val;
        char ch; // for 문에서 사용할 변수
        // 길이 입력 받고 길이 -1 만큼 오른쪽으로 이동 하므로 그만큼 더해줌
        int name_len = name.length();
        // 문자열 길이만큼 정수 배열 만들어주기
        int[] intArray = new int[name_len];
        // 문자열을 문자 배열로 변환
        char[] charArray = name.toCharArray();
        for(int i=0; i<name_len;i++){
            ch = charArray[i]; // 해당 문자를 받아오기
        // 문자에서 A를 뺀 값과 Z에서 문자를 뺴고 +1 한 값 중 더 작은 값 가져오기
            A_to_ch = (int)ch - (int)'A';
            Z_to_ch = (int)'Z' - (int)ch + 1;
            min_val = Math.min(A_to_ch, Z_to_ch);
            answer += min_val; // 이동 값 더해주기
            intArray[i] = min_val;
        }
        // 앞에서 부터 바꿀 경우 조이스틱 사용 횟수
        // 뒤에서 세었을 때 0이 아닌 값이 나오면 해당 인덱스가 바꾸는 횟수
        int front_to_back = 0;
        for (int i=name_len-1; i>0; i-- ){
            if (intArray[i] != 0){
                front_to_back = i;
                break;
            }
        }
        // 뒤에서 부터 바꿀 경우 조이스틱 사용 횟수 - 인덱스 1부터 앞에서부터 차례대로 순회하여 0이 아닌 값이 나오면 전체 개수 - 인덱스가 해당 값 
        int back_to_front = 1;
        for (int i=1;i<name_len; i++){
            if (intArray[i] != 0){
                back_to_front = name_len - i;
                break;
            }
        }

        // 앞에서 부터 중간 위치 까지 조이스틱으로 한번 갔다가 다시 왼쪽으로 진행해서 중간 위치 까지 순회하는 것, 그러면 앞에서 부터 인덱스 값이 2번 중복 되므로
        int mix_front = 0;
        for (int i = name_len/2; i>0; i--){
            if (intArray[i] != 0){
                mix_front = 2*i;
                break;
            }
        }
        for (int i = name_len/2 + 1; i<name_len;i++){
            if (intArray[i] != 0){
                mix_front += name_len - i;
                break;
            }
        }
        
        // 왼쪽으로 먼저 중간 위치 까지 갔다가 다리 오른쪽으로 진행해서 중간 위치 까지 순회하는 것, 그러면 왼쪽으로 먼저 간 값이 2번 중복 됨
        int mix_back = 0;
        for (int i = name_len/2; i>0; i--){
            if (intArray[i] != 0){
                mix_back = i;
                break;
            }
        }
        for (int i = name_len/2 + 1; i<name_len;i++){
            if (intArray[i] != 0){
                mix_back += 2*(name_len - i);
                break;
            }
        }
        // 그래서 4개 값 중에 가장 작은 값 할당
        int min_val_1, min_val_2;
        min_val_1 = Math.min(front_to_back, back_to_front);
        min_val_2 = Math.min(mix_front, mix_back);
        answer += Math.min(min_val_1, min_val_2);
        
        return answer;
    }
}