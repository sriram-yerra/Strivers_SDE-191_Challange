class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def left_view(root, level, res):
    if root is None:
        return []
    else:
        if level == len(res):
            res.append(root.val)
            # print(root.val)
        left_view(root.left, level+1, res)
        left_view(root.right, level+1, res)
    return res

def main():
    n = 5
    adj = [[] for _ in range(n)]

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    res = []
    res = left_view(root, 0, res)
    print(res)

if __name__ == "__main__":
    main()