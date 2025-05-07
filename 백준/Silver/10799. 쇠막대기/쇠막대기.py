import sys
s = sys.stdin.readline().strip()
    
result = 0
stack = []

for i in range(len(s)):
    if s[i] == '(':
        stack.append(s[i])
        continue
    
    stack.pop()
    if s[i - 1] == '(':
        result += len(stack)
    else:
        result += 1

print(result)