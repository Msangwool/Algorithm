import sys
input = sys.stdin.readline

cnt = int(input())
   
l = list(map(int, input().strip().split()))
print(max(l) * min(l))