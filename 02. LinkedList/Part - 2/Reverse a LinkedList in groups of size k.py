from Detect_cycle_in_LinkedList import Node, insert_at_end, printList

def rev(head, k):

    prev = None
    dummy = head
    count = 1

    # Reverse first K nodes
    while dummy is not None and count < k:
        next_node = dummy.next

        dummy.next = prev
        prev = dummy
        dummy = next_node

        count += 1

    # Link the rest of the list
    # since dummy is at next_node, it will be at beginnig of the next part.
    # head will be at original beginnig of the LL.
    head.next = dummy # Joining of both the parts

    return prev

head = Node(0)
head = insert_at_end(head, 10)
head = insert_at_end(head, 20)
head = insert_at_end(head, 30)
head = insert_at_end(head, 40)

head = rev(head,3)

printList(head)
