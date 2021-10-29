from  code_challenges.stack_and_queue.stack import Stack
from code_challenges.stack_and_queue.queue import Queue

def test_push():

    stack_obj=Stack()

    stack_obj.push(10)

    assert stack_obj.top.item==10


def test_multi_push():

    stack_obj=Stack()

    stack_obj.push(10)

    stack_obj.push(20)

    stack_obj.push(30)

    assert stack_obj.top.item==30

def test_pop_stack():

    stack_obj=Stack()

    stack_obj.push(10)

    stack_obj.push(20)

    stack_obj.push(30)

    stack_obj.pop()

    assert stack_obj.top.item==20

def test_multu_pop():

    stack_obj=Stack()

    stack_obj.push(100)

    stack_obj.push(150)

    stack_obj.push(200)

    stack_obj.pop()

    stack_obj.pop()

    stack_obj.pop()

    assert stack_obj.check_stackempty()==True


def test_peek_stack():

    stack_obj=Stack()

    stack_obj.push(100)

    stack_obj.push(50)

    assert stack_obj.peek()==50


def test_empty_stack():

    stack_obj=Stack()

    assert stack_obj.check_stackempty()==True


def test_pop_peek_if_empty():

    stack_obj=Stack()

    assert stack_obj.peek()=="Stack null not contain any values"

    assert stack_obj.pop()=="Stack null not contain any values"


def test_enqueue():

    queue_obj=Queue()

    queue_obj.enqueue(10)

    assert queue_obj.front.item==10

def test_multu_enqueue():

    queue_obj=Queue()

    queue_obj.enqueue(10)

    queue_obj.enqueue(15)

    queue_obj.enqueue(20)

    assert queue_obj.front.item==10

    assert queue_obj.rear.item==20

def test_dequeue():

    queue_obj=Queue()

    queue_obj.enqueue(1)

    queue_obj.enqueue(2)

    queue_obj.enqueue(3)

    queue_obj.dequeue()

    assert queue_obj.front.item==2

def test_peek():

    queue_obj=Queue()

    queue_obj.enqueue(10)

    queue_obj.enqueue(20)

    queue_obj.enqueue(30)

    assert queue_obj.peek()==10

def test_is_empty():

    queue_obj=Queue()
    queue_obj.enqueue(15)

    queue_obj.enqueue(16)

    queue_obj.dequeue()

    queue_obj.dequeue()

    assert queue_obj.is_empty()==True

def test_empty():

    queue_obj=Queue()

    assert queue_obj.is_empty()==True


def test_dequeue_peek_empty():

    queue_obj=Queue()

    assert queue_obj.peek()=="queue is null"

    assert queue_obj.dequeue()=="queue is null"
