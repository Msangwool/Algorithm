N = int(input())
times = list(map(int, input().split()))

times.sort()

total_time = 0
current_sum = 0

for time in times:
    current_sum += time
    total_time += current_sum

print(total_time)
