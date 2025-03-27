import sys

m = 0
idx = 0

for i, line in enumerate(sys.stdin):
    v = int(line)
    if v > m:
        m = v
        idx = i + 1

print(m, idx)