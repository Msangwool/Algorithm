N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

min_diff = float('inf')
visited = [False] * N

def calculate_ability(team):
    ability = 0
    for i in range(len(team)):
        for j in range(i + 1, len(team)):
            a, b = team[i], team[j]
            ability += S[a][b] + S[b][a]
    return ability

def backtrack(depth, idx):
    global min_diff

    if depth == N // 2:
        start_team = [i for i in range(N) if visited[i]]
        link_team = [i for i in range(N) if not visited[i]]

        start_score = calculate_ability(start_team)
        link_score = calculate_ability(link_team)

        min_diff = min(min_diff, abs(start_score - link_score))
        return

    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            backtrack(depth + 1, i + 1)
            visited[i] = False

backtrack(0, 0)
print(min_diff)