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

def rotate(head):
    
    return head

head = None
head = insert_at_end(head, 10)
head = insert_at_end(head, 20)
head = insert_at_end(head, 30)
head = insert_at_end(head, 40)

head = reverse(head)

printList(head)