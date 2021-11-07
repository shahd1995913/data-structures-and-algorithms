from code_challenges.tree_fizz_buzz.tree_fizz_buzz import ( Kth_tree,Node,fizz_buzz_tree)


def test_div_3():

    kth_obj= Kth_tree()

    kth_obj.root = Node(9)

    excepted = 'Fizz'

    actual = fizz_buzz_tree(kth_obj.root).value

    assert excepted == actual


def test_div_5():

    kth_obj= Kth_tree()

    kth_obj.root = Node(3)

    kth_obj.root.kth.append(Node(25))

    excepted = 'Buzz'

    actual = fizz_buzz_tree(kth_obj.root).kth[0].value

    assert excepted == actual

def test_div_3_and_5_():

    kth_obj= Kth_tree()

    kth_obj.root = Node(3)

    kth_obj.root.kth.append(Node(5))

    kth_obj.root.kth.append(Node(15))

    excepted = 'FizzBuzz'

    actual = fizz_buzz_tree(kth_obj.root).kth[1].value

    assert excepted == actual

def test_div_3_or_5():

    kth_obj= Kth_tree()

    kth_obj.root = Node(3)

    kth_obj.root.kth.append(Node(5))

    kth_obj.root.kth.append(Node(76))

    excepted = '76'

    actual = fizz_buzz_tree(kth_obj.root).kth[1].value

    assert excepted == actual
