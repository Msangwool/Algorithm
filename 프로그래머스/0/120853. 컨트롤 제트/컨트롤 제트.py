def solution(s):
    l = s.split()
    answer = 0
    for i, num in enumerate(l):
        if num == 'Z':
            answer -= int(l[i-1])
            continue
        
        answer += int(l[i])
    return answer