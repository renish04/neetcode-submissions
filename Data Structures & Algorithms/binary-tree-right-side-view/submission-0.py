# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        final = []

        if not root:
            return fianl

        dq1 = deque([root])
        dq2 = deque([])

        while dq1:
            
            node = dq1.popleft()
            if node.left:
                dq2.append(node.left)
            if node.right:
                dq2.append(node.right)
            
            if not dq1:
                final.append(node.val)
                dq1 = dq2
                dq2 = deque([])
            
        return final