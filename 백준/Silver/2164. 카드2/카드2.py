import sys
from collections import deque
inpurt = sys.stdin.readline

q = deque(range(1, int(input()) + 1))
        
for _ in range(len(q) - 1):
    q.popleft()
    q.append(q.popleft())

print(q[0])