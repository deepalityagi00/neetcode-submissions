# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def equal(root1, root2):
            if not(root1 or root2):
                return True 
            if not(root1 and root2):
                return False 
            
            if root1.val != root2.val:
                return False 

            left = equal(root1.left, root2.left)
            right = equal(root1.right, root2.right)
            return left and right 
        
        tree = deque()
        tree.append(root)
        
        while tree:
            node = tree.popleft()
            if node.val == subRoot.val:
                check_node = node 
                if equal(check_node, subRoot):
                    return True
            if node.left:
                tree.append(node.left)
            if node.right:
                tree.append(node.right)
        return False
