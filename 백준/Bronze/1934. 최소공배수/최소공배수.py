def GCD(a, b):
    if a % b == 0:
        return b
    return GCD(b, a % b)

for _ in range(int(input())):
    a, b = map(int, input().split())
    
    if a > b:
        print((a * b) // GCD(a, b))
    else:
        print((a * b) // GCD(b, a))