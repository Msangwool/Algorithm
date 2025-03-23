def multi(l):
    result = 1
    
    for i in l:
        result *= i
    
    return result

print(multi(map(int, input().split())))