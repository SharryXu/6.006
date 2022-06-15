#!/usr/bin/env python3

def merge_sort_v1(A, a=0, b=None):
    '''
    Recursive version
    '''
    if b is None:
        b = len(A)
    if 1 < b - a:
        c = (a + b + 1) // 2
        merge_sort_v1(A, a, c)
        merge_sort_v1(A, c, b)
        L, R = A[a:c], A[c:b]
        merge(L, R, A, len(L), len(R), a, b)


def merge(L, R, A, i, j, a, b):
    if a < b:
        # j <= 0 means the right array has all been merged.
        if (j <= 0) or (i > 0 and L[i - 1] > R[j - 1]):
            A[b - 1] = L[i - 1]
            i -= 1
        else:
            A[b - 1] = R[j - 1]
            j -= 1
        merge(L, R, A, i, j, a, b - 1)


def merge_sort_v2(A, a=0, b=None):
    if b is None:
        b = len(A)
    # This is for odd numbers list
    if 1 < b - a:
        c = (a + b + 1) // 2
        merge_sort_v2(A, a, c)
        merge_sort_v2(A, c, b)
        L, R = A[a:c], A[c:b]
        # In this version, finger point starts at 0 compare to recursive version.
        i, j = 0, 0
        while a < b:
            if (j >= len(R)) or (i < len(L) and L[i] < R[j]):
                A[a] = L[i]
                i += 1
            else:
                A[a] = R[j]
                j += 1
			# The reason why variable a can be changed is the merge_sort_2(A, a, c) was all been 'called'
            a += 1