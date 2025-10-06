from Detect_cycle_in_LinkedList import Node, insert_at_end, printList
# Floyd’s Cycle Detection Algorithm
def loop(head):
    slow = head
    fast = head

    # step-1: loop1
    while True:
        slow = slow.next
        fast = fast.next.next
        # when they first mee then break
        if slow == fast: 
            break

    # Find start of cycle
    # step-2: loop2
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow.data  # start node of cycle

# Create linked list with a cycle
head = Node(1)
head = insert_at_end(head, 2)
head = insert_at_end(head, 3)
head = insert_at_end(head, 4)
head = insert_at_end(head, 5)

# Create cycle: last node points to the node with value 3
cycle_start = head.next.next 
temp = head
while temp.next is not None:
    temp = temp.next
temp.next = cycle_start

print(loop(head))
