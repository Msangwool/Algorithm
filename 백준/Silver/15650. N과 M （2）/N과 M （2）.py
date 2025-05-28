N, M = map(int, input().split())

visited = [False] * (N + 1)
result = []
s = set()

def backtrack():
    if len(result) == M:
        t = tuple(sorted(result))
        if t in s:
            return
        
        print(' '.join(map(str, result)))
        s.add(t)
        return
    
    for i in range(1, N + 1):
        if not visited[i]:
            visited[i] = True
            result.append(i)
            backtrack()
            visited[i] = False
            result.pop()
            
backtrack()