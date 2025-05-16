import sys
input = sys.stdin.readline

A, B, C = map(int, input().strip().split())
D = int(input())

A_tmp = D // 3600
D = D % 3600
B_tmp = D // 60
D = D % 60

C += D
if C >= 60:
    C %= 60
    B_tmp += 1
    
B += B_tmp
if B >= 60:
    B %= 60
    A_tmp += 1
    
A = (A + A_tmp) % 24

print(A, B, C)