# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def recurse(node, low, high):
            if not node:                       # empty subtree is valid
                return True
            if not (low < node.val < high):    # node must fit its window
                return False
            return (recurse(node.left, low, node.val) and    # tighten high
                    recurse(node.right, node.val, high))       # tighten low

        return recurse(root, float('-inf'), float('inf'))
        
