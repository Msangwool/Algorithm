import sys
input = sys.stdin.readline

N, M = map(int, input().split())
    
not_see = set()
not_listen = set()
for _ in range(N):
    not_see.add(input().strip())
for _ in range(M):
    not_listen.add(input().strip())

l = not_see & not_listen
print(len(l))
for i in sorted(l):
    print(i)