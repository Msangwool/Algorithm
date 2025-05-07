import sys
from collections import deque
input = sys.stdin.readline

q = deque()
output = []
for _ in range(int(input())):
    query = input().strip()
    if query.startswith('push'):
        _, X = query.split()
        q.append(int(X))
    elif query == 'pop':
        output.append(str(q.popleft()) if q else '-1')
    elif query == 'size':
        output.append(str(len(q)))
    elif query == 'empty':
        output.append('1' if not q else '0')
    elif query == 'front':
        output.append(str(q[0]) if q else '-1')
    elif query == 'back':
        output.append(str(q[-1]) if q else '-1')

print('\n'.join(output))