from code_challenges.trees.trees import Node , Binary_search , Binarytrees
def test():
    obj =Binarytrees()
    a=obj.root=Node(1)
    a= obj.root.left=Node(2)
    a= obj.root.right=Node(3)
    expected =123
    actual1 =  obj.pre(a)
    assert actual1 == expected
    expected2 =231
    expected3 =321
    actual2 =  obj.post(a)
    actual3 =  obj.inorder(a)
    assert actual2 == expected
    assert actual3 == expected








