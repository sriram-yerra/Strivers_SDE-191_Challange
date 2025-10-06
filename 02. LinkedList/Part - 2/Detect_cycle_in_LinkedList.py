class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = None

def insert_at_end(head, data):
    new_node = Node(data)
    if head is None:  # Not 'null' in Python; use 'None'
        return new_node
    
    temp = head
    while temp.next != None:
        temp = temp.next
    
    temp.next = new_node
    return head

def printList(head):
    temp = head
    while temp != None:
        print(temp.data)
        temp = temp.next

def cycle(head):
    fast = head
    slow = head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True

    return False

head = None
head = insert_at_end(head, 10)
dummy = head
head = insert_at_end(head, 20)
head = insert_at_end(head, 30)
head = insert_at_end(head, 40)

# Move to the last node
temp = head
while temp.next:
    temp = temp.next

temp.next = dummy

# print(cycle(head))

# printList(head)