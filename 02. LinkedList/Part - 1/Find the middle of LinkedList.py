from Reverse_a_LinkedList import Node, insert_at_end, printList

'''
1. We'll use the Tortoise and Hare (slow and fast pointer) method — it’s efficient and avoids counting.
2. while fast reaches the last, slow reaches the midlle of the LinkedList.
'''
def middle(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow

'''
Naive approach having 2 loops but still having o(n) complexity as fast, slow approach. 
'''
# def middle(head):
#     temp = head
#     count = 0
#     while temp is not None:
#         count += 1
#         temp = temp.next

#     temp = head
#     i = 0
#     while i < count//2:
#         temp = temp.next
#         i += 1

#     return temp.data

head = None
head = insert_at_end(head, 10)
head = insert_at_end(head, 20)
head = insert_at_end(head, 30)
head = insert_at_end(head, 4)

printList(head)