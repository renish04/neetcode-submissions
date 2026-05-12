class Solution:
    def hasDuplicate(self, nums):
        setnum = set(nums)

        if len(setnum) != len(nums):
            return True
        return False