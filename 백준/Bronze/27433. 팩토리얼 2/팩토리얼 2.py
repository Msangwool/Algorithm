import sys
input = sys.stdin.readline

def factorial(num):
    if num <= 1:
        return 1
    return num * factorial(num - 1)

print(factorial(int(input())))