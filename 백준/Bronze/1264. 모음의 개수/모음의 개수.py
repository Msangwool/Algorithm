vowels = "aeiouAEIOU"

while True:
    line = input()
    if line == "#":
        break

    count = 0
    for ch in line:
        if ch in vowels:
            count += 1

    print(count)