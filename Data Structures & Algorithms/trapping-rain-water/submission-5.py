class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = []
        max_right = []

        score_left = 0
        for i in range(len(height)):
            if height[i] > score_left:
                max_left.append(height[i])
                score_left = height[i]
            else:
                max_left.append(score_left)

        score_right = 0
        for i in range(len(height)-1, -1, -1):
            if height[i] > score_right:
                max_right.append(height[i])
                score_right = height[i]
            else:
                max_right.append(score_right)

        area = 0
        for i in range(len(height)):
            area += (min(max_left[i], max_right[len(height)-1-i])) - height[i]

        return area
