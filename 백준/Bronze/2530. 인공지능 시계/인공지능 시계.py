import sys
input = sys.stdin.readline

A, B, C = map(int, input().strip().split())
D = int(input())

second = A * 3600 + B * 60 + C + D
print((second // 3600) % 24, (second % 3600) // 60, (second % 3600) % 60)