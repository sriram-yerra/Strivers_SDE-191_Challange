from collections import deque # (It is double ended queue..!)

# In python there is no seperate dedicated stack.
'''
Instead we can use:
1. list               --> pop() and append()
2. collections.deque  --> pop() and append()
3. queue.LifoQueue    --> put() and get()
4. Custom Stack Class --> (for learning / DSA)
'''
# 4. Custom Stack Class:
'''
class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        # List Supports pop()
        return self.items.pop() if not self.is_empty() else None
    def peek(self):
        return self.items[-1] if not self.is_empty() else None
    def is_empty(self):
        return len(self.items) == 0
'''

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def all_Traversals_iterative(root, pre, In, post):
    if root is None:
        return [], [], []
    st = deque() # this 1 is for preorder.
    st.append((root, 1))
    while st:
        node, num = st.pop()
        if num == 1:
            pre.append(node.val)
            st.append((node, 2))
            if node.left is not None:
                st.append((node.left, 1))
        elif num == 2:
            In.append(node.val)
            st.append((node, 3))
            if node.right is not None:
                st.append((node.right, 1))
        elif num == 3:
            post.append(node.val)

    return pre, In, post

# def all_Traversals_recursive(root, pre, In, post):
#     if root is None:
#         return [], [], []
#     pre.append(root.val)
#     all_Traversals_recursive(root.left, pre, In, post)
#     In.append(root.val)
#     all_Traversals_recursive(root.right, pre, In, post)
#     post.append(root.val)

#     return pre, In, post

    
def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    pre = []
    In = []
    post = []

    res = all_Traversals_recursive(root, pre, In, post)
    print(res)
    
if __name__ == "__main__":
    main()