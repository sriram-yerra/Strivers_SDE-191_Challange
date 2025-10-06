class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

def inorder_traversal(node):
    '''
    💡 Meaning:

        It checks whether the current node is None.
        If it is None, the function stops (returns immediately).

        In other words:
        “If there’s no node here (we’ve reached beyond a leaf), don’t continue recursion.”
    '''
    if node is None:
        return
    else:
        inorder_traversal(node.left)
        print(node.value, end = " ")
        inorder_traversal(node.right)
        
def preorder_traversal(node):
    if node is None:
        return
    else:   
        print(node.value, end = " ")
        preorder_traversal(node.left)
        preorder_traversal(node.right)      
        
def postorder_traversal(node):
    if node is None:
        return
    if node is not None:
        postorder_traversal(node.left)
        postorder_traversal(node.right)
        print(node.value, end = " ")

def main():
    root = Node(10)
    root.left = Node(25)
    root.right = Node(30)
    root.left.left = Node(20)
    root.left.right = Node(35)
    root.right.left = Node(15)
    root.right.right = Node(45)
    
    postorder_traversal(root)    

if __name__ == "__main__":
    main()