'''
🌳 Step 1: Does “Root to Node Path” have overlapping subproblems?

Not really.
Each node’s subtree is unique, so once you explore the left subtree, you don’t need that computation again for the right subtree — meaning no overlapping subproblems exist.

So technically, this is not a DP problem in the usual sense.

⚙️ Step 2: How we can adapt the idea (DP-style thinking)

You can apply memoization to store and reuse partial paths — especially in cases where:

The tree has repeated subtrees, or

You’re repeatedly querying for different target nodes.

In that case, we can store results for each node in a DP-like structure (dictionary).
'''

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def dfs(node, path, dp): # DYNAMIC PROGRAMMING:
    if not node:
        return
    '''
    💡 Meaning:

        It checks whether the current node is None.
        If it is None, the function stops (returns immediately).

        In other words:
        “If there’s no node here (we’ve reached beyond a leaf), don’t continue recursion.”
    '''

    # store the current path for this node
    dp[node.val] = path + [node.val]

    # recurse left and right
    dfs(node.left, dp[node.val], dp)
    # New node is constantly added to previous "dp[node.val]" path..!
    dfs(node.right, dp[node.val], dp)


# Example
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    dp = {}
    dfs(root, [], dp)

    print(dp)
    print("Path to node 5:", dp[5])
