# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.depth = 0
        self.max_depth = 0

        def recurse(root):
            if not root:
                return

            self.depth += 1
            if self.depth > self.max_depth:
                self.max_depth = self.depth

            recurse(root.left)
            recurse(root.right)
            self.depth -= 1

        recurse(root)

        return self.max_depth