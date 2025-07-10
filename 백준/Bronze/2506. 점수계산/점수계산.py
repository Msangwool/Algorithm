N = int(input())
results = list(map(int, input().split()))

score = 0
consecutive = 0
for r in results:
    if r == 1:
        consecutive += 1
        score += consecutive
    else:
        consecutive = 0

print(score)
