from collections import deque  # (Not used here, but fine to import)

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def max_width(root, level, level_count):
    # level: Which level it is in the tree
    # level_count: Number of Nodes in that level
    # if root is None:
    #     return
    
    if level in level_count:
        level_count[level] += 1
    elif level not in level_count:
        level_count[level] = 1

    if root.left:
        max_width(root.left, level+1, level_count)
    if root.right:
        max_width(root.right, level+1, level_count)

def main():
    # Constructing tree:
    #         1
    #        / \
    #       2   3
    #      / \
    #     4   5
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    # Dictionary to store node count at each level
    level_count = {}

    # Start recursion from root (level = 0)
    level = hd = 0

    max_width(root, hd, level_count)

    print("Level-wise count:", level_count)
    print("Maximum width:", max(level_count.values()))


if __name__ == "__main__":
    main()
