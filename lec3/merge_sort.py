#!/usr/bin/env python3


def merge_sort(A, a=0, b=None):
    if b is None:
        b = len(A) - 1

    if a + 1 < b:
        c = (a + b + 1) // 2
        merge_sort(A, a, c)
        merge_sort(A, c, b)
        L, R = A[a:c], A[c:b]
        merge_two_array_3(A, L, R, a, b, len(L) - 1, len(R) - 1)


"""
1 -> 2 -> 3
"""


def merge_two_array_1(A, L, R, i, j):
    a = len(L) - 1
    b = len(R) - 1
    while i <= j:
        if (a > 0 and L[a] > R[b]) or b <= 0:
            A[j] = L[a]
            a -= 1
            j -= 1
        else:
            A[j] = R[b]
            b -= 1
            j -= 1


def merge_two_array_2(A, L, R, i, j, a, b):
    while i <= j:
        if (a > 0 and L[a] > R[b]) or b <= 0:
            A[j] = L[a]
            a -= 1
            j -= 1
        else:
            A[j] = R[b]
            b -= 1
            j -= 1


def merge_two_array_3(A, L, R, i, j, a, b):
    if i < j:
        # This 'b <= 0' condition means we need to make sure the length
        # of array a should always be bigger than the length of array b
        # when we doing the split array operation.
        if (a > 0 and L[a] > R[b]) or b <= 0:
            A[j] = L[a]
            a -= 1
        else:
            A[j] = R[b]
            b -= 1
        merge_two_array_3(A, L, R, i, j - 1, a, b)
