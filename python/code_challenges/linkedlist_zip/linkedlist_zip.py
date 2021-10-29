"""
function called zip_lists that take 2 list and  make a zip for them as one list

"""
def  zip_lists(l1,l2):

  li1_head1 =l1.head

  li1_head2=l2.head

  if (not li1_head1) and (not li1_head2):

    return "The both list is null"

  elif not li1_head1:

    return l2.to_string()

  elif not li1_head2:

    return l1.to_string()

  else:

    t=''

    while li1_head1 and li1_head2 :

      if li1_head2 :

        t =li1_head1.next

        li1_head1.next=li1_head2

        li1_head1=t

      if li1_head1 :

        t =li1_head2.next

        li1_head2.next=li1_head1

        li1_head2=t

    return l1.to_string()

# li=[1,2,3]
# li2=[4,5,6]
# obj=LinkedList()
# obj.insert(1)
# obj.insert(2)
# obj.insert(3)
# obj.insert(4)

# obj2=LinkedList()
# obj2.insert(5)
# obj2.insert(6)
# obj2.insert(7)
# obj2.insert(8)

# result = zip(obj,obj2)
# print(result)

