stack = []
result = []

for _ in range(int(input())):
    query = input()
    
    l = len(stack)
    if query == 'size':
        result.append(l)
    elif query == 'empty':
        result.append(1 if l == 0 else 0)
    elif query == 'pop':
        result.append(-1 if l == 0 else stack.pop())
    elif query == 'top':
        result.append(-1 if l == 0 else stack[-1])
    else:
        stack.append(int(query.split()[1]))
        
print('\n'.join(map(str, result)))