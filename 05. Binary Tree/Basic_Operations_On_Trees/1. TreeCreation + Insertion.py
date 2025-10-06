from collections import deque

class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

def display_tree(root, adj):
    for i in range(1, len(adj)):
        if len(adj[i]) != 0:
            print(f"{i} --> {adj[i]}")
            
    print(f'length of the tree is {len(adj)}')

# def print_parents_dfs(root, adj, parent):
#     for child in adj[root]:
#         if child != parent:
#             print(f"Parent of {child} is {root}")
#             print_parents_dfs(child, adj, root) 
            
# or  #

def display_parent(root, adj):
    visited = [False] * len(adj) # array of falses.
    parent = [None] * len(adj)  # Using None instead of False because they are values not bool.
    queue = deque([root]) # adding root to the queue.
    
    visited[root] = True

    while queue: # until the queue is empty
        u = queue.popleft() # pop the first element from the queue
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                queue.append(v)

    for i in range(len(adj)):
        if visited[i] and i != root:  # Check if node was visited and is not the root
            print(f"{parent[i]} is the parent of {i}")

def display_children(root, adj):
    visited = [False] * len(adj)
    parent = [False] * len(adj)
    queue = deque([root])
    
    visited[root] = True

    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                queue.append(v)

    for i in range(len(adj)):
        if visited[i] and i != root:
            print(f"{i} is the child of {parent[i]}")

def display_leaf_nodes(root, adj):
    for i in range(1, len(adj)):
        if len(adj[i]) == 1 and i != root:
            print(f"{i} is a leaf node")
            
def print_degrees(adj):
    for i in range(1, len(adj)):
        print(f"Degree of {i} is {len(adj[i])}")

def create_tree(a, b, adj):
    adj[a].append(b)
    adj[b].append(a)

def main():
    adj = []
    root = 1
    n = 8

    adj = [[] for _ in range(n)] # List of Lists
        
    create_tree(1,2, adj)
    create_tree(1,3, adj)
    create_tree(2,4, adj)
    create_tree(2,5, adj)
    create_tree(3,6, adj)
    create_tree(3,7, adj)
    
    display_tree(root, adj)
    print(" ")
    display_parent(root, adj)
    print(" ")
    display_children(root, adj)
    print(" ")
    display_leaf_nodes(root, adj)
    print(" ")
    print_degrees(adj)
    print(" ")
    
if __name__ == "__main__":
    main()