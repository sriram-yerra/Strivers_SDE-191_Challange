from inserting_node_linkedlist import Node, insert_at_end, printList

def del_at_beginning(head):
    # code the base cases
    head = head.next
    return head

def del_at_pos(head, pos):
    # code the base cases
    
    if pos == 1:
        return head.next

    temp = head
    i = 1
    while temp is not None and i < pos - 1:
        temp = temp.next
        i += 1

    if temp is not None and temp.next is not None:
        temp.next = temp.next.next

    return head


def del_at_ending(head):
    temp = head
    while temp.next.next is not None:
        temp = temp.next

    temp.next = None
    return head    

head = None
head = insert_at_end(head, 10)
head = insert_at_end(head, 20)
head = insert_at_end(head, 30)
head = insert_at_end(head, 40)

head = del_at_beginning(head)
head = del_at_pos(head, 2)  
head = del_at_ending(head)

printList(head)

