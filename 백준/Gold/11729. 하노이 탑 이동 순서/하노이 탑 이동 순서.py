n = int(input())
def top(n, start, middle, goal):
    if n == 1:
        print(start, goal)
    else:
        top(n - 1, start, goal, middle)
        print(start, goal)
        top(n - 1, middle, start, goal)

sum = 2 ** n - 1
print(sum)

top(n, 1, 2, 3)