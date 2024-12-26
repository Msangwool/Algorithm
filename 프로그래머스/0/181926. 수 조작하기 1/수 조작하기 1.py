def solution(n, control):
    return eval(str(n) + control.replace('w', '+1').replace('s', '-1').replace('d', '+10').replace('a', '-10'))