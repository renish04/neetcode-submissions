# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        
        dummy = TreeNode(0, root, None)
        prev = dummy
        
        
        curr = root
        
        if not curr:
            return root  
            
        while curr.val != key:
            if key < curr.val:
                prev = curr
                curr = curr.left
            else:
                prev = curr
                curr = curr.right
        
        point = curr
        deleted = False

        while deleted is False:
            if not point.left and not point.right:
                if prev.right is curr:
                    prev.right = None
                elif prev.left is curr:
                    prev.left = None
                deleted = True

            elif not point.left:
                if prev.left is curr:
                    prev.left = point.right
                elif prev.right is curr:
                    prev.right = point.right
                deleted = True

            elif not point.right:
                if prev.left is curr:
                    prev.left = point.left
                elif prev.right is curr:
                    prev.right = point.left
                deleted = True

            else:
                succ_prev = point
                succ = point.right

                while succ.left:
                    succ_prev = succ
                    succ = succ.left

                point.val = succ.val

                prev = succ_prev
                curr = succ
                point = succ

        return dummy.left

        


         
        