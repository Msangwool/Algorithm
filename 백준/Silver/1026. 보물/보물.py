N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()

B_indices = sorted(range(N), key=lambda i: -B[i])

S = 0
for i in range(N):
    S += A[i] * B[B_indices[i]]

print(S)