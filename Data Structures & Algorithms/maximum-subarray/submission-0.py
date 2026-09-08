class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr_sum = nums[0]

        for i in range(1, len(nums)):
            curr_sum += nums[i]
            if curr_sum > max_sum:
                max_sum = curr_sum
            elif curr_sum < 0 and i < len(nums)-1:
                curr_sum = 0
            
        return max_sum