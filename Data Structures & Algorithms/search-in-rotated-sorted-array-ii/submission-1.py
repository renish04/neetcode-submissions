class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l = 0
        r = len(nums) - 1

        while l <= r:
            while nums[l] == nums[r] and l <= r:
                l += 1

            mid = (l + r) // 2

            if nums[mid] == target:
                return True
            elif nums[l] <= nums[mid] and nums[mid] <= nums[r]:
                if nums[mid] >= target:
                    r = mid - 1
                else:
                    l = mid + 1
                
            elif nums[l] <= nums[mid] and nums[mid] >= nums[r]:
                if nums[l] <= target and target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
                
            elif nums[l] >= nums[mid] and nums[mid] <= nums[r]:
                if nums[mid] <= target and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return False        
            