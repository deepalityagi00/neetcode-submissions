# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def solve(root, low, high):
            if not root:
                return True
            if not (low < root.val < high):
                return False 
            
            #value cannot be greater than parents value
            left_solve =  solve(root.left, low, root.val)
            #value cannot be less than parents value
            right_solve =  solve(root.right, root.val, high)

            return left_solve and right_solve

            

        return solve(root, float('-inf'), float('inf'))
            