import sys
input = sys.stdin.readline

def calculator(num1, num2, t):
    if t == '+':
        return num2 + num1
    if t == '-':
        return num2 - num1
    if t == '/':
        return num2 / num1
    if t == '*':
        return num2 * num1

N = int(input())
l = []
stack = []
target = input().strip()
for _ in range(N):
    l.append(int(input()))

for c in target:
    if ord('A') <= ord(c) <= ord('Z'):
        stack.append(l[ord(c) - ord('A')])
        continue

    stack.append(calculator(stack.pop(), stack.pop(), c))

print(f"{stack.pop():.2f}")