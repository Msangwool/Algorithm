N = int(input())
A = list(map(int, input().split()))
operator = list(map(int, input().split()))

result = []

def backtrack(idx, current_value):
    if idx == N:
        result.append(current_value)
        return
    
    for i in range(4):
        if operator[i] > 0:
            operator[i] -= 1
            backtrack(idx + 1, calculator(current_value, A[idx], i))
            operator[i] += 1
        
def calculator(value1, value2, idx):
    match idx:
        case 0:
            return value1 + value2
        case 1:
            return value1 - value2
        case 2:
            return value1 * value2
        case 3:
            return value1 // value2 if value1 > 0 else -((-value1) // value2)
    
backtrack(1, A[0])

print(max(result))
print(min(result))