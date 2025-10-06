from Reverse_a_LinkedList import Node, insert_at_end, printList

'''
Optimal: 2 pointer Approach.
1. Using fast and slow pointers
'''

def adding(head1, head2):
    dummy = Node(0)
    temp = dummy
    carry = 0

    while head1 or head2 or carry:
        if head1 is not None:
            val1 = head1.data
        else: 
            val1 = 0
        
        if head2 is not None:
            val2 = head2.data
        else: 
            val2 = 0

        total = val1 + val2 + carry
        carry = total // 10

        next_val = total % 10
        temp.next = Node(next_val)
        temp = temp.next

        if head1:
            head1 = head1.next
        if head2:
            head2 = head2.next

    return dummy.next # ponts to first node of the LL

head1 = None
head1 = insert_at_end(head1, 2)
head1 = insert_at_end(head1, 4)
head1 = insert_at_end(head1, 3)  # Represents number 342

head2 = None
head2 = insert_at_end(head2, 5)
head2 = insert_at_end(head2, 6)
head2 = insert_at_end(head2, 4)  # Represents number 465

head = adding(head1, head2)

printList(head)