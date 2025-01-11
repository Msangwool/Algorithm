def solution(myStr):
    answer = []
    for s in myStr.replace('a', 'c').replace('b', 'c').split('c'):
        if s != '':
            answer.append(s)
    return answer if answer else ['EMPTY']