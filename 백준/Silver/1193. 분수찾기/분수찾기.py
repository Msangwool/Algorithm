n = int(input())

i = 1
target = 1

while target < n:
    i += 1
    target += i

sub = target - n

if i % 2 == 0:
    x = i - sub
    y = 1 + sub
else:
    x = 1 + sub
    y = i - sub

print(f'{x}/{y}')