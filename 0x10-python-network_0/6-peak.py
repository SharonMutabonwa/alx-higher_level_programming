#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers"""
    li = list_of_integers
    l-len = len(li)
    if l-len == 0:
        return
    m = l // 2
    if (m == l-len - 1 or li[m] >= li[m + 1]) and (m == 0 or li[m] >= li[m - 1]):
        return li[m]
    if m != l-len - 1 and li[m + 1] > li[m]:
        return find_peak(li[m + 1:])
    return find_peak(li[:m])
