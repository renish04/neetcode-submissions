class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        fast = 1
        dups = 0

        while fast < len(nums):
            if nums[fast] != nums[slow]:
                nums[slow+1], nums[fast] = nums[fast], nums[slow+1]
                slow += 1
                fast += 1
            else:
                fast += 1
                dups += 1

        return len(nums)-dups   
            

