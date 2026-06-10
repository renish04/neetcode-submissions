class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [0]
        maxarea = 0

        for i in range(1, len(heights)):
            if heights[i] >= heights[i-1]:
                stack.append(i)

            else:
                while stack and heights[stack[-1]] > heights[i]:
                    top = stack.pop()
                    left = stack[-1] if stack else -1
                    width = i - left - 1
                    subarea = heights[top] * width
                    if subarea > maxarea:
                        maxarea = subarea
                stack.append(i)

        while stack:
            top = stack.pop()
            left = stack[-1] if stack else -1
            width = len(heights) - left - 1
            subarea = heights[top] * width
            if subarea > maxarea:
                maxarea = subarea
                
        return maxarea



