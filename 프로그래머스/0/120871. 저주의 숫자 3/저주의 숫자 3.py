def solution(n):
    i = 1
    result = 1
    while n != i:
        result += 1
        if result % 3 == 0 or '3' in str(result):
            continue
            
        i += 1
    return result