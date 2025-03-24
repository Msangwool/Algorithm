A, B = map(int, input().split())
C = int(input())

M = B + C
print((A+M//60)%24, M%60)