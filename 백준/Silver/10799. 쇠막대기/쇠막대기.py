import sys
s = sys.stdin.readline().strip()
    
result = 0
stack = []
i = 0
while i < len(s):
    if s[i] == '(':
        if s[i + 1] == ')':
            result += len(stack)
            i += 1
        else:
            stack.append('(')
    elif s[i] == ')':
        stack.pop()
        result += 1

    i += 1

print(result)