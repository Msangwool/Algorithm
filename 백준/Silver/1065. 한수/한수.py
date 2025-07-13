def hansoo(n):
    if n < 100:
        return n
    else:
        result = 99
        for i in range(100, n + 1):
            hundreds = i // 100
            tens = (i % 100) // 10
            ones = i % 10
            if hundreds - tens == tens - ones:
                result += 1
        return result

n = int(input())
print(hansoo(n))
