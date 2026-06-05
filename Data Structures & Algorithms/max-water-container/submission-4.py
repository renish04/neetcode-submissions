class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0

        i = 0
        j = len(height)-1

        while i < j:
            mini = min(height[i], height[j])
            maxarea = mini*(j-i)

            if maxarea > area :
                area = maxarea
            
            if mini == height[i]:
                i += 1
            else:
                j -= 1
            
        return area

