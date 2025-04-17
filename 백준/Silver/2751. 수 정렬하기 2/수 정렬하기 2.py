import sys

input = sys.stdin.readline  # 빠른 입력

N = int(input())
l = [int(input()) for _ in range(N)]

l.sort()
print('\n'.join(map(str, l)))