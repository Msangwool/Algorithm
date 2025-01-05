def solution(my_strings, parts):
    answer = ''
    for i, part in enumerate(parts):
        s = part[0]
        e = part[1]
        
        answer += my_strings[i][s:e+1]
    return answer