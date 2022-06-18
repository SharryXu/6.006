#!/usr/bin/env python3


def insertion_sort(A, i=None):
    if i is None:
        i = len(A) - 1
    if i > 0:
        insertion_sort(A, i - 1)
        insert_last(A, i)


def insert_last(A, i):
    if A[i] > A[i - 1]:
        return
    else:
        while A[i] < A[i - 1] and i > 0:
            A[i], A[i - 1] = A[i - 1], A[i]
            i -= 1
