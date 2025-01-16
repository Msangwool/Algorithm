def solution(myString):
    answer = ''
    numL = ord('l')
    for s in myString:
        if ord(s) < numL:
            answer += 'l'
            continue
        answer += s
    return answer