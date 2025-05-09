import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().strip().split()))
    
output = [-1] * N
stack = []

for i in range(N):
    while stack and A[i] > A[stack[-1]]:
        idx = stack.pop()
        output[idx] = A[i]
    
    stack.append(i)
            
print(*output)