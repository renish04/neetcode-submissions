# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        curr = root

        while True:
            if curr and val < curr.val:
                if curr.left is not None:
                    curr = curr.left
                else:
                    temp = TreeNode(val)
                    curr.left = temp
                    return root
                
            elif curr and val > curr.val:
                if curr.right is not None:
                    curr = curr.right
                else:
                    temp = TreeNode(val)
                    curr.right = temp
                    return root

            else:
                root = TreeNode(val)
                return root                