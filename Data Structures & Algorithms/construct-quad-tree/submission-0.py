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

        def recurse_quad(node, trace):
            
            first_el = trace[0]
            # print(trace)
            # print(first_el)

            node.val = first_el
            node.isLeaf = 1

            for i in trace:
                if i != first_el:
                    node.val = 1
                    node.isLeaf = 0
                    break
                
            if node.isLeaf == 0:

                topLeft = trace[0:len(trace)//4]
                node_topLeft = Node()
                node.topLeft = node_topLeft
                recurse_quad(node.topLeft, topLeft)

                topRight = trace[len(trace)//4 : len(trace)//2]
                node_topRight = Node()
                node.topRight = node_topRight
                recurse_quad(node.topRight, topRight)

                bottomLeft = trace[len(trace)//2 : 3*(len(trace)//4)]
                node_bottomLeft = Node()
                node.bottomLeft = node_bottomLeft
                recurse_quad(node.bottomLeft, bottomLeft)

                bottomRight = trace[3*(len(trace)//4) : len(trace)]
                node_bottomRight = Node()
                node.bottomRight = node_bottomRight
                recurse_quad(node.bottomRight, bottomRight)

            else:
                node.topLeft = None
                node.topRight = None
                node.bottomLeft = None
                node.bottomRight = None

        self.trace = []

        for i in range(len(grid)//2):
            for j in range(len(grid)//2):
                self.trace.append(grid[i][j])

        for o in range(len(grid)//2):
            for k in range(len(grid)//2, len(grid)):
                self.trace.append(grid[o][k])
        
        for s in range(len(grid)//2, len(grid)):
            for p in range(len(grid)//2):
                self.trace.append(grid[s][p])
                
        for r in range(len(grid)//2, len(grid)): 
            for q in range(len(grid)//2, len(grid)):
                self.trace.append(grid[r][q])
        
        node = Node()
        recurse_quad(node, self.trace)

        return node

        


        



          