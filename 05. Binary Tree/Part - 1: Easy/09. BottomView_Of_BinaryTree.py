from collections import deque # (It is double ended queue..!)

# Never check the queue for its emptiness..! Just check for Nodes..!
'''
from collections import deque

q = deque([1, 2, 3])

# --- Adding elements ---
q.append(4)        # Add to RIGHT end  → deque([1, 2, 3, 4])
q.appendleft(0)    # Add to LEFT end   → deque([0, 1, 2, 3, 4])

# --- Removing elements ---
q.pop()            # Remove from RIGHT end → returns 4 → deque([0, 1, 2, 3])
q.popleft()        # Remove from LEFT end  → returns 0 → deque([1, 2, 3])

print(q)  # deque([1, 2, 3])
'''

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def bottom_view(root, q, d):
    if root is None:
        return []
    while q:
        node, hd = q.pop() # Tuple is popped out here from rightside
        d[hd] = node.val
        if node.left is not None:
            q.appendleft((node.left, hd-1)) # A tuple should be appended from leftside.
        if node.right is not None:
            q.appendleft((node.right, hd+1))
        
    res = []
    r = sorted(d.keys())
    for i in r:
        res.append(d[i])
    return res
    
def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    q = deque([(root, 0)]) # used for level order traversal
    # Already a tuple is filled with one element, so it is never none..!
    d = {}

    res = bottom_view(root, q, d)
    print(res)

if __name__ == "__main__":
    main()