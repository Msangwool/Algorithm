import sys
from collections import deque
input = sys.stdin.readline

l = deque()

for _ in range(int(input())):
    query = input().strip()

    if query.startswith('push'):
        _, num = query.split()
        l.append(int(num))
    elif query == 'pop':
        if l:
            print(l.popleft())
        else:
            print(-1)
    elif query == 'size':
        print(len(l))
    elif query == 'empty':
        if not l:
            print(1)
        else:
            print(0)
    elif query == 'front':
        if l:
            print(l[0])
        else:
            print(-1)
    elif query == 'back':
        if l:
            print(l[-1])
        else:
            print(-1)