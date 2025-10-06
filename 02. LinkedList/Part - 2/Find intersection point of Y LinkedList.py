from Detect_cycle_in_LinkedList import Node, insert_at_end, printList

def intersection(head1, head2):
    temp1 = head1
    temp2 = head2

    '''
    The trick works because both pointers travel the same total length after switching. 
    If they intersect, they’ll meet; if not, both become None.
    '''
    while temp1 != temp2:
        if temp1 is not None:
            temp1 = temp1.next
        else:
            temp1 = head2

        if temp2 is not None:
            temp2 = temp2.next
        else:
            temp2 = head1

    if temp1 is not None:
        return temp1
    else:
        return None

# Create two lists that intersect at a common node
# Shared part
# common = Node(50)
# common = insert_at_end(common, 60)
# common = insert_at_end(common, 70)

# First list
head1 = Node(10)
head1 = insert_at_end(head1, 30)
temp = head1
while temp.next:
    temp = temp.next
# temp.next = common  # Attach intersection

# Second list
head2 = Node(11)
head2 = insert_at_end(head2, 20)
temp = head2
while temp.next:
    temp = temp.next
# temp.next = common  # Attach intersection

print(intersection(head1, head2))
