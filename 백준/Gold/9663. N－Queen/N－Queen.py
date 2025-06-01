N = int(input())

cnt = 0

visited1 = [False] * N
visited2 = [False] * (N + N)
visited3 = [False] * (2 * (N - 1) + 1)

def backtrack(k):
    global cnt

    if k == N:
        cnt += 1
        return
    
    for i in range(N):
        if not visited1[i] and not visited2[k + i] and not visited3[N - 1 + k - i]:
            visited1[i] = True
            visited2[k + i] = True
            visited3[N - 1 + k - i] = True
            backtrack(k + 1)
            visited1[i] = False
            visited2[k + i] = False
            visited3[N - 1 + k - i] = False
            
backtrack(0)

print(cnt)