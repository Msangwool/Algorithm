import sys
input = sys.stdin.readline

print(sum(i**2 for i in map(int, input().split())) % 10)