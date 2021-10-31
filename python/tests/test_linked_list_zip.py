from code_challenges.linkedlist_zip.linkedlist_zip import zipLists
from code_challenges.linked_list.linked_list import LinkedList

def test_linked_zip():
    ll1=LinkedList()

    ll1.insert(2)
    ll1.insert(1)
    ll2=LinkedList()
    ll2.insert(6)
    ll2.insert(5)

    assert zipLists(ll1,ll2) == "{ 1 } -> { 5 } -> { 2 } -> { 6 } -> NULL"
