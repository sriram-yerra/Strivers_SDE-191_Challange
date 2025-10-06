class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# def inorder(newNode):
#     if newNode is None:
#         return []
#     else:
#       `res = []
#         inorder(newNode.left)
#         print(newNode.data)
#         inorder(newNode.right)

def inorder(newNode):
    if newNode is None:
        return []

    res = []
    res += inorder(newNode.left)       # traverse left subtree
    res.append(newNode.data)           # visit root
    res += inorder(newNode.right)      # traverse right subtree
    return res

    # return inorder(newNode.left) + [newNode.data] + inorder(newNode.right)
   
def main():
    root = Node(10)
    root.left = Node(25)
    root.right = Node(30)
    root.left.left = Node(20)
    root.left.right = Node(35)
    root.right.left = Node(15)
    root.right.right = Node(45)
        
    result = inorder(root)
    print(result)

    for i in result:
        print(f"{i} ")    

if __name__ == "__main__":
    main()
    