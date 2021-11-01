from code_challenges.stack_queue_pseudo.stack_queue_pseudo import queue


def test():
    obj=queue()
    obj.enqueue(20)
    obj.enqueue(40)
    obj.enqueue(60)
    expected=60
    obj.dequeue()
    obj.dequeue()
    real=obj.dequeue()
    assert real==expected



#     queu1 = queue()

#     queu1.enqueue(20)

#     queu1.enqueue(15)

#     queu1.enqueue(20)


#     print(queu1.dequeue())

#     print(queu1.dequeue())

#     print(queu1.dequeue())
