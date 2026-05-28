# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def combine(left, right, root):
            root.left=right
            root.right=left
            return root

        def solve(root):
            if not root:
                return None
            left_result = solve(root.left)
            right_result = solve(root.right)

            return combine(left_result, right_result, root)
        
        return solve(root)