def solution(a, d, included):
    answer = 0
    for i, value in enumerate(list(range(a, a + len(included)*d, d))):
        answer += value * int(included[i])
    return answer