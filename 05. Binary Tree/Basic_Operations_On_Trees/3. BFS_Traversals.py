from collections import deque # (It is double ended queue..!)

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def bfs(root):
    if not root:
        return []
    '''
    💡 Meaning:

        It checks whether the current node is None.
        If it is None, the function stops (returns immediately).

        In other words:
        “If there’s no node here (we’ve reached beyond a leaf), don’t continue recursion.”
    '''
    
    q = deque([root])
    res = []

    while q:
        node = q.popleft()
        res.append(node.val)
        
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    
    return res

def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    q = deque([(root, 0)]) # used for level order traversal
    d = {}

    res = bfs(root) 
    print(res)

if __name__ == "__main__":
    main()