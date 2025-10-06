from Detect_cycle_in_LinkedList import Node, insert_at_end, printList

'''
Optimal:
Reverse 2nd half and compare it with 1st half:
'''
# Reverse second half
def reverse_list(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next

        curr.next = prev
        prev = curr
        curr = next_node
    return prev

def palindrome(head):
    '''
    If fast.next == None → Odd length
    (because fast moves 2 steps, so in an odd-length list it stops exactly on the last node)
   
    If fast == None → Even length
    (because fast moved 2 steps each time and landed past the last node)
    '''
    # Find middle
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    # Reverse second half
    second_half = reverse_list(slow)

    # Step 3: Compare first half and second half
    first_half = head
    second_half_copy = second_half  # Keep reference to restore later

    result = True
    # Taking 2nd half as reference, it compares with 1st half
    # Then it wont reach the extra element when the length is odd
    while second_half is not None:  
        if first_half.data != second_half.data:
            result = False
            break
        first_half = first_half.next
        second_half = second_half.next

    # Step 4 (Optional): Restore list
    reverse_list(second_half_copy)

    return result
    

head = None
head = insert_at_end(head, 1)
head = insert_at_end(head, 2)
head = insert_at_end(head, 3)
# head = insert_at_end(head, 1)
head = insert_at_end(head, 2)
head = insert_at_end(head, 1)

printList(head)

print(palindrome(head))
