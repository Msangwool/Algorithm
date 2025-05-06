import sys
input = sys.stdin.readline

l = ['(', ')', '[', ']']

output = []
while 1:
    s = input().rstrip()

    if s == '.':
        break

    stack = []
    for c in s:
        if c not in l:
            continue

        if c == '(' or c == '[':
            stack.append(c)
            continue

        if not stack:
            output.append("no")
            break

        target = stack.pop()
        if (c == ')' and target != '(') or (c == ']' and target != '['):
            output.append("no")
            break
    else:
        output.append("no" if stack else "yes")

print('\n'.join(output))
