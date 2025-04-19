def solution(n,a,b):
    i = 1
    
    while n > 0:
        print(n)
        a = (a + 1) // 2
        b = (b + 1) // 2
        
        print(a, b)
        if a == b:
            break
        
        n //= 2
        i += 1
        

    return i