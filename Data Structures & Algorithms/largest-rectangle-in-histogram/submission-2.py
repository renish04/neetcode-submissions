class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [0]
        maxarea = 0

        if len(heights) ==1:
            return heights[0]
            
        for i in range(1, len(heights)):
            if heights[i] >= heights[i-1]:
                stack.append(i)
            else:
                f = 1

                while stack and heights[stack[-1]] > heights[i]:
                    subarea = f*heights[stack[-1]]
                    if subarea > maxarea:
                        maxarea = subarea
                    stack.pop()
                    f += 1
                stack.append(i)

        for j in range(len(stack)):
            if j == 0:
                subarea = (heights[stack[j]] * (stack[j] - 0  - 1)) + heights[stack[j]] * (stack[-1] - stack[j] + 1)
                if subarea > maxarea:
                    maxarea = subarea
            else:
                subarea = (heights[stack[j]] * (stack[j] - stack[j-1]  - 1)) + (heights[stack[j]] * (stack[-1] - stack[j] + 1))
                if subarea > maxarea:
                    maxarea = subarea
                
        return maxarea



