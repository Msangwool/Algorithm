import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().strip().split()))

F = [0] * 1000001
for i in range(N):
    F[A[i]] += 1

NGF = [-1] * N
stack = []
for i in range(N):
    while stack and F[A[i]] > F[A[stack[-1]]]:
        idx = stack.pop()
        NGF[idx] = A[i]
    stack.append(i)

print(*NGF)