# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        root = TreeNode()
        root.val = preorder[0]
        node = root

        i = 1
        j = 0

        arr_node = [root]
        while i < len(preorder):

            if inorder[j] == root.val:
                node = root
                new_node = TreeNode()
                new_node.val = preorder[i]
                arr_node.append(new_node)
                node.right = new_node
                node = new_node
                i += 1
                j += 1

            while i < len(preorder) and preorder[i] != inorder[j]:
                new_node = TreeNode()
                new_node.val = preorder[i]
                node.left = new_node
                arr_node.append(new_node)
                node = new_node
                i += 1
            
            if i < len(preorder) and preorder[i] == inorder[j]:
                new_node = TreeNode()
                new_node.val = preorder[i]
                node.left = new_node
                arr_node.append(new_node)
                node = new_node
            
            x = i

            print(x)
            while x < len(preorder) and j < len(preorder) and preorder[x] == inorder[j]:
                x -= 1
                j += 1
            
            if x + 1 < len(preorder):
                node = arr_node[x+1]
                i += 1

            if i < len(preorder):
                new_node = TreeNode()
                new_node.val = preorder[i]
                arr_node.append(new_node)
                node.right = new_node
                node = new_node

                if preorder[i] == inorder[j]:
                    j += 1
                i += 1

        return root
            



        

