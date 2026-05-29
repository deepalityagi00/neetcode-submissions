# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def solve(root1, root2):
            if not (root1 or root2):
                # both of them is None
                return True 
            if not (root1 and root2):
                # either of them is Prsent 
                return False 

            # both of them present
            if root1.val != root2.val:
                return False 
            
            left = solve(root1.left, root2.left)
            right = solve(root1.right, root2.right)
            return left and right
        return solve(p,q)

