class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        if nums[0] > nums[len(nums)-1]:
            hi = 0
            lo = len(nums)-1
        else:
            lo = 0
            hi = len(nums)-1

        while abs(lo - hi) != 1:
            mid = (lo + hi) // 2

            if nums[mid] > nums[lo]:
                hi = mid
            elif nums[mid] < nums[lo]:
                lo = mid
            
        return nums[lo]

