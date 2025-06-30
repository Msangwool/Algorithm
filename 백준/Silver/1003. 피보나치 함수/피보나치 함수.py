T = int(input())

count = [[0, 0] for _ in range(41)]

count[0] = [1, 0]  
count[1] = [0, 1] 

for i in range(2, 41):
    count[i][0] = count[i - 1][0] + count[i - 2][0]
    count[i][1] = count[i - 1][1] + count[i - 2][1]

for _ in range(T):
    N = int(input())
    print(count[N][0], count[N][1])