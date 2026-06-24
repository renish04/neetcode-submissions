# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        nodes = []

        def recurse(root):
            if not root:
                return
            
            recurse(root.left)
            recurse(root.right)
            nodes.append(root.val)

        recurse(root)
        return nodes