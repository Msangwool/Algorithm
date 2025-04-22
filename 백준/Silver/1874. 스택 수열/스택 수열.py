import sys
input = sys.stdin.readline

N = int(input())
target = [int(input()) for _ in range(N)]

j = 1
stack = []
result = []
is_valid = True

for num in target:
    while j <= num:
        stack.append(j)
        result.append('+')
        j += 1
        
    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        is_valid = False
        break

if is_valid:
    print('\n'.join(result))
else:
    print('NO')