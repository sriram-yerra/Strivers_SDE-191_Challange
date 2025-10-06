from collections import deque # (It is double ended queue..!)

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def verticleOrder_traversal(root, q, d):
    if root is None:
        return {}
    while q:
        node, hd = q.popleft()
        if hd not in d: d[hd] = [node.val]
        else: d[hd].append(node.val)    

        if node.left is not None: q.append((node.left, hd-1))
        if node.right is not None: q.append((node.right, hd+1))

    for i in sorted(d.keys()):
        print(d[i])

def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    q = deque([(root, 0)]) # used for level order traversal
    d = {}

    res = verticleOrder_traversal(root, q, d)
    print(res)

if __name__ == "__main__":
    main()