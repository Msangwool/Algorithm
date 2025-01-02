def solution(intStrs, k, s, l):
    answer = []
    for str in intStrs:
        value = int(str[s:s+l])
        if value > k:
            answer.append(value)
    return answer