N = int(input())
l = list(map(int, input().split()))
print(sum(i/max(l)*100 for i in l)/N)