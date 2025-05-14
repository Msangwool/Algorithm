N = int(input())

init = ['***', '* *', '***']

def rep(n, arr):
    if n == N:
        return arr
    
    tmp = []
    
    for i in range(n):
        tmp.append(arr[i] * 3)
        
    for i in range(n):
        tmp.append(arr[i] + ' ' * n + arr[i])
        
    for i in range(n):
        tmp.append(arr[i] * 3)
    
    return rep(n * 3, tmp)
    
output = rep(3, init)

print('\n'.join(output))