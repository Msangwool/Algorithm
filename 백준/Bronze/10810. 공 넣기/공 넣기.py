N, M = map(int, input().split())

basket = [0] * N
for _ in range(M):
    a, b, c = map(int, input().split())
    basket[a-1:b] = [c] * (b - a + 1)

print(' '.join(map(str, basket)))