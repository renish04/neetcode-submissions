class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        element = nums[0]
        score = 0

        for i in range(len(nums)):
            if nums[i] == element:
                score += 1
            else:
                score -= 1
                if score == 0:
                    element = nums[i]
                    score += 1
        
        return element