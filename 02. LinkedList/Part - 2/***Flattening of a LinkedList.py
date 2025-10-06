class Node:
    def __init__(self, x=0, nextNode=None, childNode=None):
        self.data = x
        self.next = nextNode
        self.child = childNode

# Merges two linked lists in a particular
# order based on the data value
def merge(list1, list2):
    # Create a dummy node as a
    # placeholder for the result
    dummyNode = Node(-1)
    res = dummyNode

    # Merge the lists based on data values
    while list1 and list2:
        if list1.data < list2.data:
            res.child = list1
            res = list1
            list1 = list1.child
        else:
            res.child = list2
            res = list2
            list2 = list2.child
        res.next = None

    # Connect the remaining
    # elements if any
    if list1:
        res.child = list1
    else:
        res.child = list2

    # Break the last node's
    # link to prevent cycles
    if dummyNode.child:
        dummyNode.child.next = None

    return dummyNode.child

# Flattens a linked list with child pointers
def flattenLinkedList(head):
    # If head is null or there 
    # is no next node, return head
    if not head or not head.next:
        return head

    # Recursively flatten the
    # rest of the linked list
    mergedHead = flattenLinkedList(head.next)
    head = merge(head, mergedHead)
    return head

# Print the linked list by
# traversing through child pointers
def printLinkedList(head):
    while head:
        print(head.data, end=" ")
        head = head.child
    print()

# Print the linked list
# in a grid-like structure
def printOriginalLinkedList(head, depth):
    while head:
        print(head.data, end="")

        # If child exists, recursively
        # print it with indentation
        if head.child:
            print(" -> ", end="")
            printOriginalLinkedList(head.child, depth + 1)

        # Add vertical bars
        # for each level in the grid
        if head.next:
            print()
            print("| " * depth, end="")
        head = head.next

# Create a linked list with child pointers
head = Node(5)
head.child = Node(14)
head.next = Node(10)
head.next.child = Node(4)
head.next.next = Node(12)
head.next.next.child = Node(20)
head.next.next.child.child = Node(13)
head.next.next.next = Node(7)
head.next.next.next.child = Node(17)

# Print the original
# linked list structure
print("Original linked list:")
printOriginalLinkedList(head, 0)

# Flatten the linked list
# and print the flattened list
flattened = flattenLinkedList(head)
print("\nFlattened linked list: ", end="")
printLinkedList(flattened)

                             