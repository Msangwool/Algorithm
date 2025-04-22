for _ in range(int(input())):
    stack = []
    is_valid = True
    for c in input():
        if c == '(':
            stack.append(c)
            continue

        if not stack:
            is_valid = False
            break

        stack.pop()

    if is_valid and len(stack) == 0:
        print('YES')
    else:
        print('NO')