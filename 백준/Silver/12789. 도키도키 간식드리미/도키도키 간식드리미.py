import sys
input = sys.stdin.readline

idx = 1
N = int(input())
l = list(map(int, input().strip().split()))

stack = []
for i in l:
    if i != idx:
        stack.append(i)
        continue

    idx += 1

    while stack and stack[-1] == idx:
        stack.pop()
        idx += 1
        
if not stack:
    print("Nice")
else:
    print("Sad")