n, m = map(int, input().split())
l = list(map(int, input().split()))

sum = 0;
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for t in range(j + 1, n):
            temp_sum = l[i] + l[j] + l[t]
            if temp_sum <= m: 
                sum = max(sum, l[i] + l[j] + l[t])

print(sum)