n = int(input())

is_exist = False
for i in range(1, n):
    if i + sum(map(int, list(str(i)))) == n:
        is_exist = True
        print(i)
        break

if not is_exist:
    print(0)