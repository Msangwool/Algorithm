def solution(a, d, included):
    
    answer = 0
    for i, value in enumerate(list(range(a, a + len(included)*d, d))):
        if (included[i]):
            answer += value
    return answer