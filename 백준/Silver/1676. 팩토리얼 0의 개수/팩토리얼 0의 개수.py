def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

N = int(input())

tg = factorial(N)

cnt = 0
for i in str(tg)[::-1]:
    if i != '0':
        break
    cnt += 1
    
print(cnt)