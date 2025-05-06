import sys
input = sys.stdin.readline

output = []
for _ in range(int(input())):
    stack = []
    for c in input().strip():
        if c == '(':
            stack.append(c)
            continue

        if not stack:
            output.append("NO")
            break

        stack.pop()
    else:
        output.append("NO" if stack else "YES")
print('\n'.join(output))