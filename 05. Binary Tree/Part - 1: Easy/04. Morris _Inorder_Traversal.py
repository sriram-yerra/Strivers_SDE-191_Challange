class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def MorrisInorder(root):
    pass

def createtree(adj, a, b):
    adj[a].append(b)
    adj[b].append(a)

def main():
    n = 5
    adj = [[] for _ in range(n)]

    root = Node(1)
    createtree(adj, 1, 2)
    createtree(adj, 1, 3)


if __name__ == "__main__":
    main()