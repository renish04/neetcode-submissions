# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        rootlist = []
        nodelist = []

        while root:
            rootlist.append(root)
            if not root.left:
                if root.right:
                    nodelist.append(root.val)
                    rootlist.pop()
                    root = root.right
                else:
                    nodelist.append(root.val)
                    rootlist.pop()
                    if rootlist:
                        root = rootlist[-1]
                    else:
                        root = None
                        break
                    if root.right:
                        nodelist.append(root.val)
                        rootlist.pop()
                        root = root.right
                    else:
                        nodelist.append(root.val)
                        rootlist.pop()
                        if rootlist:
                            root = rootlist[-1]
                        else:
                            root = None              
            else:
                root = root.left

        return nodelist

          
        
