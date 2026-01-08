def solution(answers):
    student_1 = [1, 2, 3, 4, 5]
    student_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    scores = [0, 0, 0]
    
    for i, v in enumerate(answers):
        if student_1[i % len(student_1)] == v:
            scores[0] += 1
        if student_2[i % len(student_2)] == v:
            scores[1] += 1
        if student_3[i % len(student_3)] == v:
            scores[2] += 1
    
    max_v = 0
    for v in scores:
        max_v = max(max_v, v)
    
    answer = []
    for i, v in enumerate(scores):
        if v == max_v:
            answer.append(i+1)
        
    return answer
