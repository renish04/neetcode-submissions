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
            return final
        
        final.append(root.val)

        dq1 = deque([root])
        dq2 = deque([])

        while dq1:
            if dq1[0].left:
                dq2.append(dq1[0].left)
            if dq1[0].right:
                dq2.append(dq1[0].right)

            dq1.popleft()
        
            if not dq1 and dq2:
                final.append(dq2[-1].val)
                dq1 = dq2
                dq2 = deque([])

        return final


        

