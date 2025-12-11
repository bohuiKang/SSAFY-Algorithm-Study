def solution(arr):
    result = []
    i = -1  

    while arr:
        j = arr.pop()     
        if j != i:
            result.append(j)
            i = j

    result.reverse()
    return result
