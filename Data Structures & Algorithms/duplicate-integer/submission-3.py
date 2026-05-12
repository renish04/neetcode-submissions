class Solution:
    def hasDuplicate(self, nums):
        check = []
        for i in range(len(nums)):
            if nums[i] in check:
                return True
            else:    
                check.append(nums[i])
        return False
        