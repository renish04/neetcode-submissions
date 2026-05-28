class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = -1
        right = len(nums)
        k = 0

        while k < right:
            if nums[k] == 0:
                nums[k], nums[left+1] = nums[left+1], nums[k]
                k += 1
                left += 1
            elif nums[k] == 1:
                k += 1
            else:
                nums[k], nums[right-1] = nums[right-1], nums[k]
                right -= 1
    
        