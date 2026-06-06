class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        j = 0
        min_count = len(nums)
        sum = 0
        enter = 0

        while j < len(nums):
            sum += nums[j]

            while sum >= target:
                enter += 1
                if j-i+1 < min_count:
                    min_count = j-i+1
                sum -= nums[i]
                i += 1
            j+= 1

        if enter == 0:
            return 0
        else:
            return min_count