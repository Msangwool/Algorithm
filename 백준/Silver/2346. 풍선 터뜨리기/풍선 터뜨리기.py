from collections import deque
    
N = int(input())
paper = list(map(int, input().strip().split()))
    
d = deque(range(2, N + 1))
output = [1]
target = paper[0]

for _ in range(N - 1):
    if target > 0:
        for _ in range(target - 1):
            d.append(d.popleft())
    else:
        for _ in range(abs(target)):
            d.appendleft(d.pop())
    k = d.popleft()
    target = paper[k - 1]
    output.append(k)
print(*output)