import sys
input = sys.stdin.readline

l_a, l_b = map(int, input().split())

a = set(map(int, input().split()))
b = set(map(int, input().split()))

print(len(a - b) + len(b - a))