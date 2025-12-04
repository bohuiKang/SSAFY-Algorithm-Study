def solution(genres, plays):
    total = {}   # 장르별 총 재생수
    songs = {}   # 장르별 (재생수, 고유번호) 리스트

    for i in range(len(genres)):
        g = genres[i]
        p = plays[i]

        total.setdefault(g, 0)
        total[g] += p

        songs.setdefault(g, [])
        songs[g].append((p, i))

    # 장르 정렬
    genre_order = sorted(total.keys(), key=lambda g: total[g], reverse=True)

    answer = []
    for g in genre_order:
        # 곡 정렬
        songs[g].sort(key=lambda x: (-x[0], x[1]))

        # 장르당 최대 2곡 선택
        answer.append(songs[g][0][1])
        if len(songs[g]) >= 2:
            answer.append(songs[g][1][1])

    return answer
