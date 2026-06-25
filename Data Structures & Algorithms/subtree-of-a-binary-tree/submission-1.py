# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def recurse(root):
            if not root:
                return False 

            same = sameTree(root, subRoot)
            print(same)
            leftrecurse = recurse(root.left)
            rightrecurse = recurse(root.right)

            return same or leftrecurse or rightrecurse

        def sameTree(root, subRoot):
            
            if not root and not subRoot:
                return True
            elif root and not subRoot:
                return False
            elif not root and subRoot:
                return False
            
            if root.val != subRoot.val:
                return False
            
            left = sameTree(root.left, subRoot.left)
            right = sameTree(root.right, subRoot.right)

            return left and right
    
        return recurse(root)