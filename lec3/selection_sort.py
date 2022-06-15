#!/usr/bin/env python3


def selection_sort(A, i=None):
    if i is None:
        i = len(A) - 1
    if i == 0:
        return
    else:
        j = prefix_max(A, i - 1)
        if A[j] > A[i]:
            A[i], A[j] = A[j], A[i]
        selection_sort(A, i - 1)


def prefix_max(A, i=None):
    if i is None:
        i = len(A) - 1
    if i == 0:
        return i
    else:
        j = prefix_max(A, i - 1)
        if A[i] < A[j]:
            return j
        else:
            return i
