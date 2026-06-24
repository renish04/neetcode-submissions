# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.bend = 0

        def recurse(root):
            if not root:
                return 0
            
            left_depth = recurse(root.left)
            right_depth = recurse(root.right)
            depth = 1 + max(left_depth, right_depth)
            self.bend = left_depth + right_depth

            return depth

        recurse(root)
        return self.bend