def solution(num_list):
    answer = 0
    for num in num_list:
        while num != 1:
            answer += 1
            num //= 2
    return answer