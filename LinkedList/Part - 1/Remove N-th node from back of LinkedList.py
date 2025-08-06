from Reverse_a_LinkedList import Node, insert_at_end, printList

'''
Optimal: 2 pointer Approach.
1. Using fast and slow pointers
'''

def remove_from_last_nth_node(head, n):
    temp = head
    dummy = Node(0)
    dummy.next = temp

    fast = dummy # pointer-1
    slow = dummy # pointer-2

    # Move fast pointer n steps ahead using while loop
    count = 0
    while count < n:
        fast = fast.next
        count += 1

    # Move both fast and slow pointers until fast reaches the end
    while fast.next is not None:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next

    return temp

head = None
head = insert_at_end(head, 10)
head = insert_at_end(head, 30)
head = insert_at_end(head, 50)
head = insert_at_end(head, 11)
head = insert_at_end(head, 20)
head = insert_at_end(head, 30)

head = remove_from_last_nth_node(head, 2)

printList(head)