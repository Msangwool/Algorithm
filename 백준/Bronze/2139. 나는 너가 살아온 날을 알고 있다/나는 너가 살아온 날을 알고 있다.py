def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

while True:
    d, m, y = map(int, input().split())
    if d == 0 and m == 0 and y == 0:
        break

    days = 0
    for i in range(m - 1):
        days += month_days[i]

    if is_leap_year(y) and m > 2:
        days += 1

    days += d

    print(days)