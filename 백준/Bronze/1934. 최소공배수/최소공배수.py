def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

for _ in range(int(input())):
    A, B = map(int, input().split())
    if A > B:
        print(A*B//gcd(A, B))
    else:
        print(A*B//gcd(A, B))