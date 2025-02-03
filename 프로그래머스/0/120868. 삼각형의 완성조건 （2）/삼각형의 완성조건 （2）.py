def solution(sides):
    answer = 0
    
    i = max(sides)
    while min(sides) + i > max(sides):
        i -= 1
        answer += 1
    
    i = max(sides) + 1
    while sides[0] + sides[1] > i:
        i += 1
        answer += 1
        
    return answer