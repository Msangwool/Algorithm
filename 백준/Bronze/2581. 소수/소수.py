def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num//2 + 1):
        if num % i == 0:
            return False
    return True

start = int(input())
end = int(input())

primes = []
target = 0
for i in range(start, end+1):
    if is_prime(i):
        if len(primes) == 0:
            target = i
        primes.append(i)
        
if target == 0:
    print(-1)
else:
    print(sum(primes))
    print(target)