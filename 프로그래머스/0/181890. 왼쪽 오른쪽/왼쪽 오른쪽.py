def solution(str_list):
    answerL = []
    
    idx = -1;
    for i, s in enumerate(str_list):
        answerL
        if s == 'l':
            return answerL
        if s == 'r':
            idx = i
            break
        answerL.append(s)
    
    if idx != -1:
        return str_list[idx+1:]
        
    return []