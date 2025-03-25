total_amount = int(input())

l = int(input())
for _ in range(l):
    amount, qty = map(int, input().split())
    total_amount -= amount * qty

print('Yes' if total_amount == 0 else 'No')