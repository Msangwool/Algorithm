stack = []
priority = {"+": 1, "-": 1, "*": 2, "/": 2, "(":0}

for c in input():
    if c.isalpha():
        print(c, end="")
        continue

    if c == "(":
        stack.append(c)
    elif c == ")":
        while stack and stack[-1] != "(":
            print(stack.pop(), end="")
        stack.pop() # (는 출력 대상 아님
    else:
        while stack and priority[stack[-1]] >= priority[c]:
            print(stack.pop(), end="")
        stack.append(c)

while stack:
    print(stack.pop(), end="")