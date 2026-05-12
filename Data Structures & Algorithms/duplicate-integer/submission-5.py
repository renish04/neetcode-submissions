class Solution:
    def hasDuplicate(self, nums):
        for i in range(len(nums)):
            if nums[i] in nums[i+1:len(nums)+1]:
                return True
        return False
        