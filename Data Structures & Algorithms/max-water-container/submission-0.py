class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        score = 0
        while i < j:
            mini = min(height[i], height[j])

            if height[i] == mini:
                if (mini * (j - i)) > score:
                    score = (mini * (j - i))
                i += 1

            elif height[j] == mini:
                if (mini * (j - i)) > score:
                    score = (mini * (j - i))
                j -= 1
            
        return score


