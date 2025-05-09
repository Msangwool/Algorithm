import sys
input = sys.stdin.readline

cnt = 0
isHi = set()
for _ in range(int(input())):
    s = input().strip()
    
    if s == 'ENTER':
        isHi = set()
        continue
    
    if s in isHi:
        continue
    
    cnt += 1
    isHi.add(s)

print(cnt)