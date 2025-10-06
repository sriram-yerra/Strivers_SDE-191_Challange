class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = None

        # Node(data, next=None) --> it is a constructor

def insert_at_end(head, data):
    new_node = Node(data)
    if head is None:  # Not 'null' in Python; use 'None'
        return new_node
    
    temp = head
    while temp.next != None:
        temp = temp.next
    
    temp.next = new_node
    return head

def insert_at_head(head, data):
    new_node = Node(data)
    new_node.next = head
    head = new_node
    return head

def insert_at_pos(head, data, pos):
    new_node = Node(data)

    temp = head
    i = 0   
    while temp != None and i < pos-1:
        temp = temp.next
        i += 1

    new_node.next = temp.next
    temp.next = new_node

    return head

def printList(head):
    temp = head
    while temp != None:
        print(temp.data)
        temp = temp.next

head = None
head = insert_at_head(head, 1)
head = insert_at_end(head, 99)
head = insert_at_pos(head, 2, 1)

# printList(head)