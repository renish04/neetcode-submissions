class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea = 0

        left = 0
        right = len(height)-1

        while left < right:
            mini = min(height[left], height[right])

            if mini == height[left]:
                if mini*(right-left) > maxarea:
                    maxarea = mini*(right-left)
                left += 1
            else:
                if mini*(right-left) > maxarea:
                    maxarea = mini*(right-left)
                right -= 1
            
        return maxarea