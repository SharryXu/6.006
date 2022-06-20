def direct_access_sort(A):
    u = 1 + max([x for x in A])
    arr = [None] * u
    for i in A:
        arr[i] = 1
    j = 0
    for k in range(u):
        if arr[k] is not None:
            A[j] = k
            j += 1
