from collections import defaultdict

def solution(genres, plays):
    answer = []

    # 데이터 입력
    musics_listening = defaultdict(int)
    music_num = defaultdict(list)

    for i in range(len(genres)):
        musics_listening[genres[i]] += plays[i] # {'classic': 1450, 'pop': 3100}
        music_num[genres[i]] += [(plays[i], i)] # {'classic': [(500, 0), (150, 2), (800, 3)], 'pop': [(600, 1), (2500, 4)]}

    # 데이터 정렬
    listening = sorted(musics_listening.items(), key=lambda item: item[1], reverse=True)
    
    for i in range(len(listening)):
        num_lst = music_num[listening[i][0]]
        if len(num_lst) == 1:
            answer.append(num_lst[0][1])
        else:
            num = sorted(num_lst, key=lambda x:(-x[0], x[1]))
            answer.append(num[0][1])
            answer.append(num[1][1])

    return answer 
