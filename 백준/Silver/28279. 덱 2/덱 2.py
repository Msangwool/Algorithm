import sys
from collections import deque

input = sys.stdin.readline

q = deque()
output = []
for _ in range(int(input())):
    query = input().strip()
    
    if query.startswith('1'):
        _, X = query.split()
        q.appendleft(X)
    elif query.startswith('2'):
        _, X = query.split()
        q.append(X)
    elif query == '3':
        output.append(q.popleft() if q else '-1')
    elif query == '4':
        output.append(q.pop() if q else '-1')
    elif query == '5':
        output.append(str(len(q)))
    elif query == '6':
        output.append('1' if not q else '0')
    elif query == '7':
        output.append(q[0] if q else '-1')
    elif query == '8':
        output.append(q[-1] if q else '-1')
            
print('\n'.join(output))