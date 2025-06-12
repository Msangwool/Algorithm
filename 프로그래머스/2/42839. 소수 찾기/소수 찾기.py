import math

def solution(numbers):
    def generate_combinations(numbers):
        result = set()

        def backtrack(path, used):
            if path:
                num = int(''.join(path))
                result.add(num)

            for i in range(len(numbers)):
                if not used[i]:
                    used[i] = True
                    path.append(numbers[i])
                    backtrack(path, used)
                    path.pop()
                    used[i] = False

        used = [False] * len(numbers)
        backtrack([], used)

        return result

    numbers = list(numbers)
    result = generate_combinations(numbers)
    M = max(result)
    
    is_valid = [True] * (M + 1)
    is_valid[0] = is_valid[1] = False
    
    for i in range(2, math.isqrt(M) + 1):
        if is_valid[i]:
            for j in range(i * i, M + 1, i):
                is_valid[j] = False
    
    return sum(1 for i in result if is_valid[i])