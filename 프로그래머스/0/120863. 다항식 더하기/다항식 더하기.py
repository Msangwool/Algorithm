def solution(polynomial):
    x1 = 0
    x0 = 0
    for i in polynomial.split():
        if i == '+':
            continue
        
        if 'x' in i:
            if i == 'x':
                x1 += 1
                continue
                
            x1 += int(i.replace('x', ''))
        else:
            x0 += int(i)
            
    if x1 == 0:
        return f'{x0}'
    elif x0 == 0:
        if x1 == 1:
            return 'x'
        
        return f'{x1}x'
    
    if x1 == 1:
        return f'x + {x0}'
    
    return f'{x1}x + {x0}'