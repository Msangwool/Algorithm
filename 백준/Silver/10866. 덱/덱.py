from collections import deque
import sys

input = sys.stdin.readline

d = deque()

for _ in range(int(input())):
    query = input().strip()
    if query.startswith("push_front"):
        _, X = query.split()
        d.appendleft(int(X))
    elif query.startswith("push_back"):
        _, X = query.split()
        d.append(int(X))
    elif query == "pop_front":
        if d:
            print(d.popleft())
        else:
            print(-1)
    elif query == "pop_back":
        if d:
            print(d.pop())
        else:
            print(-1)
    elif query == "size":
        print(len(d))
    elif query == "empty":
        print(1 if len(d) == 0 else 0)
    else:
        if not d:
            print(-1)
            continue

        if query == "front":
            print(d[0])
        else:
            print(d[-1])