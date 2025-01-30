def solution(polynomial):
    x1 = 0
    x0 = 0
    for i in polynomial.split(' + '):
        if i == 'x':
            x1 += 1
            continue
            
        if 'x' in i:        
            x1 += int(i[:-1])
        else:
            x0 += int(i)
            
    if x1 == 0:
        return str(x0)
    elif x1 == 1:
        return 'x' if x0 == 0 else f'x + {x0}'
    
    return f'{x1}x' if x0 == 0 else f'{x1}x + {x0}'