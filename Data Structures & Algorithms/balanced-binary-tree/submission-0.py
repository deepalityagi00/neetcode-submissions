# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def solve(root):
            if not root:
                return 0, True
            
            lh, lb = solve(root.left)
            rh, rb = solve(root.right)

            is_balanced = abs(rh-lh) < 2

            return 1 + max(lh, rh) , lb and rb and is_balanced
        
        return solve(root)[1]




