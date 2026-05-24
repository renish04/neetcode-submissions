class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        left = 0
        right = n-1
        i = 0

        while left < len(nums):
            if i > right:
                break
            if nums[i] == 0:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
            if nums[i] == 2:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
            else:
                i += 1