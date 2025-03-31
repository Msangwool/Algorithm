N = int(input())
for _ in range(N):
    a, b = input().split()
    print(''.join([str(i*int(a)) for i in b]))