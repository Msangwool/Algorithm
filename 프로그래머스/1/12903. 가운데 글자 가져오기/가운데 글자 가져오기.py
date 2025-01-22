def solution(s):    
    return s[len(s)//2+(-1 * (len(s) % 2 == 0)):len(s)//2 + 1]
