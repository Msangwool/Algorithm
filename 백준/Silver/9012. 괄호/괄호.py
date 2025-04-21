for _ in range(int(input())):
    stack = []
    is_valid = True
    for c in input():
        if c == '(':
            stack.append(c)
            continue

        if len(stack) == 0:
            is_valid = False
            break

        if stack.pop() == ')':
            is_valid = False
            break

    if is_valid and len(stack) == 0:
        print('YES')
    else:
        print('NO')