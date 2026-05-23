class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        while i < (len(nums)):
            k = nums[i]
            if nums[i] == -1 or nums[i] <=0 or nums[i] > len(nums):
                nums[i] = -1
                i += 1
            elif nums[i] == nums[k-1] and i == k-1:
                i += 1
            else:
                if nums[k-1] == k and i != k-1:
                    nums[i] = -1
                else:
                    nums[i], nums[k-1] = nums[k-1], nums[i]
        
        print(nums)    
        for i in range(len(nums)):
            if nums[i] == -1:
                return i+1
            else:
                continue

        return len(nums)+1