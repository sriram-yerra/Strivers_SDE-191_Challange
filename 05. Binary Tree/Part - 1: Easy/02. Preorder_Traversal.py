class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None 

def preorder(root):
    res = []
    if root is None:
        return []
    newnode = root
    res.append(newnode.data)
    res += preorder(newnode.left)
    res += preorder(newnode.right)

    return res

def create_tree(adj, a, b):
    # adj[a] = b
    # adj[b] = a
    adj[a].append(b)
    adj[b].append(a)

def buildTree(adj, rootval, visitedSet): # visitedset---> Avoids Cycles
    root = Node(rootval)
    visitedSet.add(rootval)
    
    children = []
    for c in adj[rootval]:
        if c not in visitedSet:
            children.append(c) # Result: a list of unvisited child nodes.

    if len(children) >= 1:
        root.left = buildTree(adj, children[0], visitedSet)
    '''
    If there is at least one unvisited child, we make it the left child of the current node.
    '''

    if len(children) >= 2:
        root.right = buildTree(adj, children[1], visitedSet)
    '''
    If there is a second unvisited child, we make it the right child.
    '''

    return root

def main():    
    # root = Node(1) # this is another approach, useful when manually creating nodes.

    # adj = [[]*n] # this wont work
    
    adj = [[] for _ in range(5)]
    create_tree(adj, 1, 2)
    create_tree(adj, 1, 3)

    visited = set()
    root_node = buildTree(adj, 1, visited)

    res = preorder(root_node)

    print(res)

if __name__ == "__main__":
    main()
