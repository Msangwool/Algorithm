number = int(input())
a = number // 10
b = number % 10
s = a + b
count = 1

while True:
    new_number = b * 10 + s % 10
    if new_number == number:
        break
    a = b
    b = s % 10
    s = a + b
    count += 1

print(count)