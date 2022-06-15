#!/usr/bin/env python3


def binary_search(A: list, target: int, a: int = 0, b: int = None) -> (int | None):
    if b is None:
        b = len(A) - 1
    if a > b:
        return None
    c = (a + b) // 2
    if A[c] == target:
        return c
    elif A[c] > target:
        return binary_search(A, target, a, c - 1)
    else:
        return binary_search(A, target, c + 1, b)
