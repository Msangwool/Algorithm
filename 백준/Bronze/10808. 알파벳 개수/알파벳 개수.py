l = [0] * 26

for c in input():
    l[ord(c) - ord('a')] += 1

print(' '.join(map(str, l)))