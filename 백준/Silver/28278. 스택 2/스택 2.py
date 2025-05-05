import sys
input = sys.stdin.readline

stack = []
output = []
for _ in range(int(input())):
    query = input().strip()
    if query.startswith('1'):
        _, X = map(int, query.split())
        stack.append(X)  
        continue
    query = int(query)
    if query == 2:
        output.append(str(stack.pop()) if stack else "-1")
    elif query == 3:
        output.append(str(len(stack)))
    elif query == 4:
        output.append("1" if not stack else "0")
    elif query == 5:
        output.append(str(stack[-1]) if stack else "-1")

print("\n".join(output)) 