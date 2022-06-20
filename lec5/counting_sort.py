def counting_sort(A):
    u = 1 + max([i for i in A])
    arr = [[]] * u
    for i in A:
        arr[i].append(i)
    j = 0
    for k in range(u):
        if len(arr[k]) > 0:
            for x in arr[k]:
                A[j] = x
                j += 1
