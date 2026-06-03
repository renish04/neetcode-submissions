class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = len(nums) - 1

        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        
        left = 0
        right = k-1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        l = k
        r = len(nums) - 1

        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        
