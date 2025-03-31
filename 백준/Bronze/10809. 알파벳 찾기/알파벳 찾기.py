l = [-1] * 26
for i, v in enumerate(list(input())):
    if l[ord(v)-97] == -1:
      l[ord(v)-97] = i
print(*l)