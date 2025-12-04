def solution(genres, plays):

    # 장르별 재생 횟수 저장
    genre_total = {}

    # 장르별 노래 저장 (재생수, 인덱스)
    songs_by_genre = {}

    for i in range(len(genres)):
        # g = 장르, p = 재생수
        g = genres[i]
        p = plays[i]

        # 딕셔너리 안에 장르 g가 있으면 값을 가져오고 없으면 0을 반환한다네용 ~ 우와 ~ !!
        # 거기에 재생수를 누적.
        genre_total[g] = genre_total.get(g, 0) + p

        # 장르 추가 전 없으면 리스트 새로 만들어줌
        if g not in songs_by_genre:
            songs_by_genre[g] = []

        songs_by_genre[g].append((p, i))

    # 총 재생 수 기준으로 장르 정렬
    genre_order = sorted(genre_total.items(), key=lambda x: x[1], reverse=True)

    answer = []
    for g, _ in genre_order:
        # 장르 내 정렬: 재생수 내림차순 → 인덱스 오름차순
        songs = sorted(songs_by_genre[g], key=lambda x: (-x[0], x[1]))

        # 상위 2곡만
        for song in songs[:2]:
            answer.append(song[1])

    return answer
