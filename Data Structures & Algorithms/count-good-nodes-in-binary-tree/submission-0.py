# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        self.list = [root.val]

        def recurse_goodNodes(root):

            if root.val >= self.list[-1]:
                self.count += 1
                self.list.append(root.val)

            if root.left is not None:
                recurse_goodNodes(root.left)

            if root.right is not None:
                recurse_goodNodes(root.right)
            
            if root.val == self.list[-1]:
                self.list.pop()
            
        
        recurse_goodNodes(root)

        return self.count
