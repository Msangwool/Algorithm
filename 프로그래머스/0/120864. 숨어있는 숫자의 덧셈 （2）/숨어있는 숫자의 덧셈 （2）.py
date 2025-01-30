def solution(my_string):
    temp = ''
    answer = 0
    for s in my_string:
        if s.isdigit():
            temp += s
            continue
        
        if temp.isdigit():
            answer += int(temp)
        
        temp = ''
    
    if temp.isdigit():
        answer += int(temp)
    return answer