from collections import Counter  # {'요소': '요소의 개수'}

def solution(participant, completion):
    counter = Counter(participant) - Counter(completion)  # 딕셔너리는 값을 뺄 수 있다.
    return list(counter.keys())[0]