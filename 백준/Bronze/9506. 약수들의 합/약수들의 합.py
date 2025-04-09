while 1:
    n = int(input())
    
    if n == -1:
        break
    
    l = [i for i in range(1, n//2 + 1) if n % i == 0]
    
    if sum(l) == n:
        print(f'{n} = ', end='')
        for i in range(len(l) - 1):
            print(f'{l[i]} + ', end='')
        print(l[len(l) - 1])
    else:
        print(f'{n} is NOT perfect.')