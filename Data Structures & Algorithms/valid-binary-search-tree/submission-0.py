# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.list = []
        self.check = True

        def recurse_bst(root):
            self.list.append(root.val)

            if root.left is not None:
                if root.left.val > root.val:
                    self.check = False
                
                recurse_bst(root.left)

            if root.right is not None:
                if root.right.val < root.val:
                    self.check = False

                recurse_bst(root.right)
            
            if root.val == self.list[-1]:
                self.list.pop()
                
        recurse_bst(root)
        return self.check