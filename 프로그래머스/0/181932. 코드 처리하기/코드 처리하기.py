def solution(code):
    mode = 0
    answer = ''
    for idx, c in enumerate(code):
        if (c == '1'):
            mode = changeMode(mode)
            continue
        
        if (mode == 0 and idx % 2 == 0 or mode == 1 and idx % 2 == 1):
            answer += c
    return answer if answer != '' else 'EMPTY'

def changeMode(mode):
    return 1 if mode == 0 else 0