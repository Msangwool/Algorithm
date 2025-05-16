a, b = map(int, input().split())
n = a * b
for i in input().split():
    print(int(i) - n, end=" ")