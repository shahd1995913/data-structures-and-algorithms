from code_challenges.insertion_sort.insertion_sort import InsertionSort

def test_1():
    arr=[20,18,12,8,5,-2]
    real =InsertionSort(arr)
    expected=[-2, 5, 8, 12, 18, 20]
    assert real==expected


def test_Few_uniques():
    arr=[5,12,7,5,5,7]
    real =InsertionSort(arr)
    expected=[5, 5, 5, 7, 7, 12]
    assert real==expected


def test_Nearly_sorted():
    arr=[2,3,5,7,13,11]
    real =InsertionSort(arr)
    expected=[2, 3, 5, 7, 11, 13]
    assert real==expected
