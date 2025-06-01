S = input()

l = []

for i in range(len(S)):
    l.append(S[len(S) - i - 1:])
    
l.sort()

print(*l, sep="\n")