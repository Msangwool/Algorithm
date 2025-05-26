N, M = map(int, input().split())
visited = [False] * (N + 1)
result = []
hash = set()

def backtrack():
    temp = tuple(sorted(result))
    if len(result) == M and temp not in hash:
        print(*result)
        hash.add(temp)
        return

    for i in range(1, N + 1):
        if not visited[i]:
            visited[i] = True
            result.append(i)
            backtrack()
            result.pop()
            visited[i] = False

backtrack()