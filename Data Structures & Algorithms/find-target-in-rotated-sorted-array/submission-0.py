class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l+r) // 2

            if nums[mid] == target:
                return mid
            elif abs(nums[l]-target) > abs(nums[r]-target):
                l = mid + 1
            elif abs(nums[r]-target) >= abs(nums[l]-target):
                r = mid - 1

        return -1