from tuple_sort import tuple_sort


def radix_sort(A: list) -> list:
    if len(A) == 0:
        return A
    max_value = max(A)
    max_length = len(str(max_value))
    result = []
    for i in range(len(A)):
        B = [
            0,
        ] * max_length
        length = max_length - 1
        a, B[length] = divmod(A[i], 10)
        while a != 0:
            length -= 1
            a, B[length] = divmod(a, 10)
        result.append(B)
    return tuple_sort(result)
