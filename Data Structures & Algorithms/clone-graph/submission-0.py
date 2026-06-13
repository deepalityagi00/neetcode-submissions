"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        nodes = {}
        def dfs(root):
            if root in nodes:
                return nodes[root]
            node = Node(root.val)
            nodes[root] = node
            nei = []
            for n in root.neighbors:
                nei.append(dfs(n))
            node.neighbors = nei
            return node
        
        
        return dfs(node)
