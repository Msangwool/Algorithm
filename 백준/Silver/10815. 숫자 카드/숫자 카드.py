import sys
input = sys.stdin.readline

n = int(input())
target = set(map(int, input().split()))

m = int(input())
print(*[1 if i in target else 0 for i in map(int, input().split())])