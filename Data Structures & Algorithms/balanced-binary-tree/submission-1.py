# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.max_diff = 0

        def recurse(root):
            if not root:
                return 0
            left_depth = recurse(root.left)
            right_depth = recurse(root.right)

            self.max_diff = max(self.max_diff, abs(left_depth-right_depth))
            
            max_depth = 1 + max(left_depth, right_depth)
            return max_depth

        recurse(root)

        if self.max_diff <= 1:
            return True
        else:
            return False 