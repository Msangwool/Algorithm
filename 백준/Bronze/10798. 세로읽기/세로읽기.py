l = []
l_len = []

for _ in range(5):
    v = input()
    l.append(v)
    l_len.append(len(v))
    
for i in range(max(l_len)):
    for j in range(len(l_len)):
        if i < l_len[j]:
            print(l[j][i], end="")
            