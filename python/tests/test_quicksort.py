from code_challenges.quicksort.quicksort import (QuickSort)

def test_1():
    arr = [8,4,23,42,16,15]
    n=len(arr)
    real =QuickSort(arr, 0, n-1)
    expected=[4, 8, 15, 16, 23, 42]
    assert real==expected
