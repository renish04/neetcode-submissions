class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        j = 0
        sum = 0
        k = 0
        min_len = len(nums)

        while j < len(nums):
            sum += nums[j]
            while sum >= target:
                k += 1
                sum -= nums[i]
                min_len = (j-i+1)
                i += 1
            j += 1
        
        if k == 0:
            return 0
        else:
            return min_len