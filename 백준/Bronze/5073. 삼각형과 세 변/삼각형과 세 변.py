while 1:
    l = sorted(list(map(int, input().split())))
    
    if l[0] == 0 and l[2] == 0:
        break
        
    if l[0] + l[1] <= l[2]:
        print('Invalid')
        continue
        
    if l[0] == l[2]:
        print('Equilateral')
    elif l[0] == l[1] or l[1] == l[2]:
        print('Isosceles')
    else:
        print('Scalene')