a, b = map(int, input().strip().split(' '))
print(''.join('*'*a + '\n' for _ in range(b)))
