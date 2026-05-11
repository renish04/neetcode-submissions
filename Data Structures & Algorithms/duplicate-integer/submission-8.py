class Solution:
    def hasDuplicate(self, nums):
        set_num = set(nums)
        if len(set_num) != len(nums):
            return True
        return False
        