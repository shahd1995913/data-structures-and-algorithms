from code_challenges.merge_sort.merge_sort import Mergesort
import pytest

def test_Mergesort():



    real = Mergesort([10,18,26,205,4,3])


    expected = [3, 4, 10, 18, 26, 205]

    assert expected == real
