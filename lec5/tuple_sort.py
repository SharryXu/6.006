def tuple_sort(A: list[tuple]) -> list[tuple]:
    if len(A) == 0:
        return []
    length = len(A[0]) - 1
    while length >= 0:
        result = []
        while len(A) > 0:
            j = 0
            for i in range(len(A)):
                if A[j][length] > A[i][length]:
                    j = i
            result.append(A[j])
            A.pop(j)
        A = result
        length -= 1
    return A
