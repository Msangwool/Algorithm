import sys
input = sys.stdin.readline

stack = []

for _ in range(int(input())):
    t = int(input())
    if t == 0:
        stack.pop()
        continue
    
    stack.append(t)
            
print(sum(stack)) 