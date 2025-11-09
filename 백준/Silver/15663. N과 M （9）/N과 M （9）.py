import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = sorted(map(int, input().split()))

visited = [False] * N
path = []
out = []

def dfs(depth: int):
    if depth == M:
        out.append(' '.join(map(str, path)))
        return

    prev = None  
    for i in range(N):
        if visited[i]:
            continue
        if prev == nums[i]: 
            continue

        visited[i] = True
        path.append(nums[i])
        dfs(depth + 1)
        path.pop()
        visited[i] = False

        prev = nums[i] 

dfs(0)
print('\n'.join(out))
