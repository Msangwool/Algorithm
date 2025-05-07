import sys
from collections import deque
inpurt = sys.stdin.readline

q = deque()

for i in range(1, int(input()) + 1):
    q.append(i)
        
for _ in range(len(q) - 1):
    q.popleft()
    q.append(q.popleft())

print(q[0])