def solution(s):
    count = 0
    for i in s.lower():
        if i == 'p':
            count += 1
        elif i == 'y':
            count -= 1
    return count == 0