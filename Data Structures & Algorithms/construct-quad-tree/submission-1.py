"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
    
        def recurse_quad(node, grid):
            
            first_el = grid[0][0]
            node.val = first_el
            node.isLeaf = 1

            for i in grid:
                for j in i:
                    if j != first_el:
                        node.val = 1
                        node.isLeaf = 0
                        break
                
            if node.isLeaf == 0:
                
                topLeft = []
                node_topLeft = Node()
                node.topLeft = node_topLeft
                for i in range(len(grid)//2):
                    temp = []
                    for j in range(len(grid)//2):
                        temp.append(grid[i][j])
                    topLeft.append(temp)
                recurse_quad(node.topLeft, topLeft)

                topRight = []
                node_topRight = Node()
                node.topRight = node_topRight
                for o in range(len(grid)//2):
                    temp = []
                    for k in range(len(grid)//2, len(grid)):
                        temp.append(grid[o][k])
                    topRight.append(temp)
                recurse_quad(node.topRight, topRight)

                bottomLeft = []
                node_bottomLeft = Node()
                node.bottomLeft = node_bottomLeft
                for s in range(len(grid)//2, len(grid)):
                    temp = []
                    for p in range(len(grid)//2):
                        temp.append(grid[s][p])
                    bottomLeft.append(temp)
                recurse_quad(node.bottomLeft, bottomLeft)

                bottomRight = []
                node_bottomRight = Node()
                node.bottomRight = node_bottomRight
                for r in range(len(grid)//2, len(grid)): 
                    temp = []
                    for q in range(len(grid)//2, len(grid)):
                        temp.append(grid[r][q])
                    bottomRight.append(temp)
                recurse_quad(node.bottomRight, bottomRight)

            else:
                node.topLeft = None
                node.topRight = None
                node.bottomLeft = None
                node.bottomRight = None
        
        node = Node()
        recurse_quad(node, grid)

        return node

        


        



          