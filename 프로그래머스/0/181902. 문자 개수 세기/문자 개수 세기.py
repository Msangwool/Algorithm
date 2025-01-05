def solution(my_string):
    answer = [0] * 52
    
    upperInitNum = ord('A')
    lowerInitNum = ord('a')
    
    for c in my_string:
        if c.isupper():
            answer[ord(c) - upperInitNum] = answer[ord(c) - upperInitNum] + 1
        else:
            answer[ord(c) - lowerInitNum + 26] = answer[ord(c) - lowerInitNum + 26] + 1
        
    return answer