from array_binary_search import __version__
from array_binary_search.array_binary_search import BinarySearch

def test_version():
    assert __version__ == '0.1.0'

def test_BinarySearch():

    array=[-131, -82, 0, 27, 42, 68, 179]

    value=42
    #Output is
    TestItem=4
    assert BinarySearch(value,array)==TestItem


def test_BinarySearch1():

    array=[1, 2, 3, 5, 6, 7]
    value=4
    #Output is
    TestItem=-1
    assert BinarySearch(value,array)==TestItem


def test_BinarySearch2():

    array=[4, 8, 15, 16, 23, 42]
    value=15
    #Output is
    TestItem=2
    assert BinarySearch(value,array)==TestItem
