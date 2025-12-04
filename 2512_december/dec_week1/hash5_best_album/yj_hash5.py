def solution(genres, plays):
    answer = []

    # 1. 장르별 재생횟수 구하기
    genre_play_cnt = {}  # 장르별 총 재생횟수
    genre_songs = {}  # "장르명": (고유번호, 노래 재생횟수)
    
    for i in range(len(genres)):
        if genres[i] in genre_play_cnt:  # 기존꺼 있으면 재생 횟수 더하기
            genre_play_cnt[genres[i]] += plays[i]
            genre_songs[genres[i]].append((i, plays[i]))
        else:  # 없으면 초기화
            genre_play_cnt[genres[i]] = plays[i]
            genre_songs[genres[i]] = [(i, plays[i])]
    
    genre_play_cnt = sorted(genre_play_cnt.items(), key=lambda x: x[1], reverse=True)  # value 기준으로 정렬
            
    # 2. 노래 재생횟수 순으로 정렬
    for genre, total_play in genre_play_cnt:
        sorted_songs = sorted(genre_songs[genre], key=lambda x: x[1], reverse=True)  # 재생횟수 순으로 정렬
        answer.extend([x[0] for x in sorted_songs][:2])  # 고유번호만 뽑아내고 앞 두 개만 정답에 추가
        
    return answer