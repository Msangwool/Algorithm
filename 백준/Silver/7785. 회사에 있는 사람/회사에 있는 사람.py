import sys
input = sys.stdin.readline

info = dict()
for i in range(int(input())):
    name, log = input().split()
    info[name] = log

print(*sorted([name for name, log in info.items() if log == 'enter'], reverse=True), sep="\n")