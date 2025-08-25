N = input().strip()

counts = [0] * 10

for ch in N:
    counts[int(ch)] += 1

counts[6] = (counts[6] + counts[9] + 1) // 2
counts[9] = counts[6]

print(max(counts))
