def counting_sort(A):
    u = 1 + max([i for i in A])
    # cannot use [[]] * u, that will cause all elements
    # bind to the same child array
    arr = [[] for _ in range(u)]
    for a in A:
        (arr[a]).append(a)
    j = 0
    for k in range(u):
        for x in arr[k]:
            A[j] = x
            j += 1
