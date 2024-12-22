def solution(a, b):
    
    ab = int(f'{a}{b}')
    ab2 = 2*a*b
    
    if (ab == ab2):
        return ab
    
    return max(ab, ab2)