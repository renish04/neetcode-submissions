# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def recurse(p, q):
            if not p and not q:
                return True
            elif not p and q:
                return False
            elif not q and p:
                return False
            
            if p.val != q.val:
                return False
            
            boolleft = recurse(p.left, q.left)
            boolright = recurse(p.right, q.right)
            if boolleft == True and boolright == True:
                return True
            else:
                return False

        return(recurse(p, q))