N, B = map(int, input().split())

m = 0
while(N >= B**m):
    m += 1

result = ''
for i in reversed(range(m)):
    t = N//(B**i)
    N = N%(B**i)
    if t < 10:
        result += str(t)
    else:
        result += chr(t + ord('A') - 10)

print(result)