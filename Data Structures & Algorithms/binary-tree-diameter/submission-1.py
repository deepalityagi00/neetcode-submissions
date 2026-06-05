# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def solve(node):
            if not node:
                return 0, 0 
            
            lh, ld = solve(node.left)
            rh, rd = solve(node.right)

            height = max(lh,rh)
            diameter = max(ld, rd, lh+rh)
            return 1+height, diameter 
        
        return solve(root)[1]



