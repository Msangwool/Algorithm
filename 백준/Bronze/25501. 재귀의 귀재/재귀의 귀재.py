import sys
input = sys.stdin.readline

def recursion(s, l, r, cnt):
    cnt += 1
    if l >= r: 
        return (1, cnt)
    elif s[l] != s[r]:
        return (0, cnt)
    else:
        return recursion(s, l + 1, r - 1, cnt)
            
output = []
for _ in range(int(input())):
    s = input().strip()
    output.append(recursion(s, 0, len(s) - 1, 0))

for t in output:
    print(*t)