import sys
input = sys.stdin.readline

l_stack = []
r_stack = []

for i in input().strip():
    l_stack.append(i)

for _ in range(int(input().strip())):
    cmd = input().strip()
    if cmd.startswith('P'):
        _, c = cmd.split()
        l_stack.append(c)
    elif cmd == 'L' and l_stack:
        r_stack.append(l_stack.pop())
    elif cmd == 'D' and r_stack:
        l_stack.append(r_stack.pop())
    elif cmd == 'B' and l_stack:
        l_stack.pop()

print(''.join(l_stack) + ''.join(reversed(r_stack)))