# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.n =0
        self.k = k
        self.result = 0

        def recurse(root):
            if not root:
                return
            recurse(root.left)
            self.n += 1
            if self.n == self.k:
                self.result = root.val
            recurse(root.right)
        
        recurse(root)
        return self.result
        