def solution(progresses, speeds):
    days = []
    for i in range(len(progresses)):
        remain = 100 - progresses[i]
        day = (remain + speeds[i] - 1) // speeds[i]   # 올림
        days.append(day)

    result = []
    temp = days[0]   # 기준날짜
    cnt = 1

    for i in range(1, len(days)):
        if days[i] <= temp:
            cnt += 1
        else:
            result.append(cnt)
            cnt = 1
            temp = days[i]

    result.append(cnt)
    return result
