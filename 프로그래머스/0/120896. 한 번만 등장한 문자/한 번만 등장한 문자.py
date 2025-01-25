def solution(s):
    l = []
    for i in s:
        if s.count(i) == 1:
            l.append(i)
            
    if not l:
        return l
    
    return ''.join(sorted(l))