n = int(input())

l = []

if n % 5 == 0:
    l.append(n//5)

if n % 3 == 0:
    l.append(n//3)

for i in range(5, n, 5):
    temp = n
    cnt = i // 5
    temp = temp - i
    if temp % 3 == 0:
        cnt += temp // 3
        l.append(cnt)
        
if l:
    print(min(l))
else:
    print(-1)