import sys
input = sys.stdin.readline

for age, name in sorted([tuple(input().split()) for _ in range(int(input()))], key=lambda t: int(t[0])):
    print(age, name)