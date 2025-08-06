from Reverse_a_LinkedList import Node, insert_at_end, printList

'''
Naive approach involves the merging at new LL
'''
'''
Optimal: 
1. Involves using the LL1 to combine both.
2, Use one dummy node initially to start the process
'''
def mergeLL(head1, head2):
    dummy_node = Node(-1)
    temp = dummy_node

    while head1 is not None and head2 is not None:
        if head1.data <= head2.data:
            # giving the address of that next samll value from head1 to the next to temp
            temp.next = head1 
            head1 = head1.next
        else:
            # giving the address of that next samll value from head2 to the next to temp
            temp.next = head2 
            head2 = head2.next
        temp = temp.next

    if head1 is not None:
        temp.next = head1
    else:
        temp.next = head2

    return dummy_node.next


head1 = None
head1 = insert_at_end(head1, 10)
head1 = insert_at_end(head1, 30)
head1 = insert_at_end(head1, 50)

head2 = None
head2 = insert_at_end(head2, 11)
head2 = insert_at_end(head2, 20)
head2 = insert_at_end(head2, 30)

head = mergeLL(head1, head2)

printList(head)