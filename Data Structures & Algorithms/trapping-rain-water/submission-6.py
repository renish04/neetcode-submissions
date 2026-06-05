class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = [-1]*len(height)
        max_right = [-1]*len(height)

        maxarea = 0

        leftmax = 0
        for i in range(len(height)):
            if height[i] > leftmax:
                max_left[i] = height[i]
                leftmax = height[i]
            else:
                max_left[i] = leftmax
            
        rightmax = 0
        for i in range(len(height)-1, -1, -1):
            if height[i] > rightmax:
                max_right[i] = height[i]
                rightmax = height[i]
            else:
                max_right[i] = rightmax
        
        for i in range(len(height)):
            maxarea += min(max_left[i], max_right[i]) - height[i] 

        print(max_left)
        print(max_right)
        return maxarea