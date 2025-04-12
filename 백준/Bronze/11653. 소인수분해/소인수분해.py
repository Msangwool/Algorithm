n = int(input())

i = 2
while n > 1:
    while n / i == n // i:
        n /= i
        print(i)
    i += 1