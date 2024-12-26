def solution(n, control):
    keys = dict(zip(['w', 's', 'd', 'a'], [1, -1, 10, -10]))
    return n + sum([keys[c] for c in control])