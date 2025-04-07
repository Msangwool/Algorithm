l = [25, 10, 5, 1]
for _ in range(int(input())):
    C = int(input())
    for i in l:
        print(C//i, end=" ")
        C = C%i
    print()