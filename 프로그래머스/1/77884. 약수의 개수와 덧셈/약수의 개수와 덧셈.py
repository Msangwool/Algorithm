def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        if (len([j for j in range(1, i//2 + 1) if i % j == 0]) + 1) % 2 == 0:
            answer += i
            continue
        answer -= i
    return answer