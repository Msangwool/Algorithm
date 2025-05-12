def merge(history, A, p, q, r):
    i, j = p, q + 1
    tmp = []
    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp.append(A[i])
            i += 1
        else:
            tmp.append(A[j])
            j += 1

    while i <= q:
        tmp.append(A[i])
        i += 1
    while j <= r:
        tmp.append(A[j])
        j += 1

    for k in range(len(tmp)):
        A[p + k] = tmp[k]
        history.append(tmp[k])

def merge_sort(history, A, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(history, A, p, q)
        merge_sort(history, A, q + 1, r)
        merge(history, A, p, q, r)

N, K = map(int, input().split())
A = list(map(int, input().split()))

history = []
merge_sort(history, A, 0, N - 1)

if len(history) < K:
    print(-1)
else:
    print(history[K - 1])