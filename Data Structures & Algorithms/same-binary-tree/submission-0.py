# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.listp = []
        self.listq = []

        def recurse_p(p):
            if not p:
                self.listp.append(None)
                return

            self.listp.append(p.val)
            recurse_p(p.left)
            recurse_p(p.right)

        def recurse_q(q):
            if not q:
                self.listq.append(None)
                return

            self.listq.append(q.val)
            recurse_q(q.left)
            recurse_q(q.right)
            
        recurse_p(p)
        recurse_q(q)

        print(self.listp, self.listq)
        if self.listp == self.listq:
            return True
        else:
            return False
        