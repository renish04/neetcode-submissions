class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        j = 0
        sum = 0
        k = set()
        min_len = 0

        while j < len(nums):
            sum += nums[j]
            while sum >= target:
                sum -= nums[i]
                min_len = (j-i+1)
                k.add(min_len)
                i += 1
            j += 1
        
        if len(k) == 0 :
            return 0
        else:
            return min(k)