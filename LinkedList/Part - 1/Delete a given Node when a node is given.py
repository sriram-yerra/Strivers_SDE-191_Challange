from Reverse_a_LinkedList import Node, insert_at_end, printList

def delete_node(head, n):
    # If the head node itself holds the value to be deleted
    if head.data == n:
        return head.next 

    temp = head
    while temp.next is not None:
        if temp.next.data == n:
            temp.next = temp.next.next  # skip the node with data == n
            return head
        temp = temp.next

    return head  # if node with value n not found

head = None
head = insert_at_end(head, 10)
head = insert_at_end(head, 20)
head = insert_at_end(head, 30)
head = insert_at_end(head, 4)

head = delete_node(head, 20)

printList(head)