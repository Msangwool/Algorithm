def solution(s):
    answer = ''
    i = 0
    for j in s:
        if j == ' ':
            i = 0
            answer += j
            continue
        
        if i % 2 == 0:
            answer += j.upper()
        else:
            answer += j.lower()
            
        i += 1
    return answer
