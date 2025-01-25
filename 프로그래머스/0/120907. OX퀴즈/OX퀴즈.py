def solution(quiz):
    return ['O' if eval(s.replace('=', '==')) else 'X' for s in quiz]