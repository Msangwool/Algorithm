def cantor(arr, start, N):
    if N <= 1:
        return

    N = N // 3
    K = N + start
    for i in range(K, K + N):
        arr[i] = ' '

    cantor(arr, start, N)
    cantor(arr, K + N, N)

while True:
    try:
        N = int(input())
        N_list = ['-' for _ in range(3**N)]
    except EOFError:
        break

    cantor(N_list, 0, len(N_list))
    print(''.join(N_list))