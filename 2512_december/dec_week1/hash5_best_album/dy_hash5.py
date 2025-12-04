def solution(genres, plays):
    answer = []
    # 장르별 재생횟수 카운팅하기 위한 딕셔너리 키-값: 장르-재생횟수
    p = {}
    # 장르별 분류를 위한 딕셔너리 키-값: 장르 - [(해당 곡의 인덱스 번호, 해당 곡의 재생횟수)]
    d = {}
    # 인덱스 순회, 딕셔너리의 값 할당
    for i in range(len(genres)):
        p[genres[i]] = p.get(genres[i], 0) + plays[i]
        d.setdefault(genres[i], []).append((i, plays[i]))

    # 장르별 재생횟수에 따라 정렬
    # d.items() --> 각 key,value가 tuple로 들어있는 리스트 객체로 변환
    # 변환한 리스트를 lambda 식을 활용하여 정렬
    p = sorted(p.items(), key=lambda x: x[1], reverse=True)

    # 정렬된 순서대로 순회, 장르별 재생횟수는 필요가 없으니 _로 할당
    for ca, _ in p:
        # 곡이 한개 이상, 정렬
        if len(d[ca]) > 1:
            # 재생횟수는 내림차순, 인덱스 번호는 오름차순으로 정렬
            d[ca].sort(key=lambda x: (-x[1], x[0]))
            # 각 첫번째, 두번째 곡을 앨범에 수록
            answer.append(d[ca][0][0])
            answer.append(d[ca][1][0])
        # 곡이 한개라면 그 곡만 수록
        else:
            answer.append(d[ca][0][0])

    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))