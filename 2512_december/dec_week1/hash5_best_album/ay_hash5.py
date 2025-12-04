genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
def solution(genres, plays):
    answer = []
    gener_dic ={}
    plays_num = len(genres)
    # 장르별 노래 총 재생횟수랑 인덱스별 노래 값 딕셔너리로 만들기
    # 구조 {
    #     장르 : {
    #         'total' : 총 재생 횟수,
    #         'song' : [(고유번호, 재생횟수), (고유번호, 재생횟수)]
    #     }
    # }

    for i in range(plays_num):
        if genres[i] not in gener_dic:
            gener_dic[genres[i]] = {
                'total' : plays[i],
                'song' : [(i, plays[i])],
            }
        else:
            gener_dic[genres[i]]['song'] += [(i,plays[i])]
            gener_dic[genres[i]]['total'] += plays[i]
    # print(gener_dic)

    gener_num = len(gener_dic) #장르 종류 개수
    gener_total_list = [0]*gener_num # 장르 종류 만큼 리스트 크기 만들어서 
    i = 0
    for kind in gener_dic:
        gener_total_list[i] = (kind, gener_dic[kind]['total'])
        i += 1

    gener_total_list.sort(key= lambda x:x[1], reverse=True) # 재생 횟수로 정렬
    # print(gener_total_list)

    for kind, total in gener_total_list: # 정렬된 장르 돌면서 노래 고르기
        songs = gener_dic[kind]['song'] 
        songs.sort(key= lambda x: (-x[1], x[0])) # 노래 재생횟수, 번호로 정렬
        answer.append(songs[0][0]) # 제일 재생횟수 많은 노래 번호 추가

        if len(songs) > 1: # 2개 이상일 경우 하나 더 추가
            answer.append(songs[1][0])

    return answer


print(solution(genres, plays))
