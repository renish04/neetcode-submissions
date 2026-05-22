class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(len(nums)):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = ""
        
        for i in range(len(nums)):
            if nums[i] == "":
                continue
            else:
                k = nums[i] 
                if i == k-1:
                    continue
                elif nums[i] == nums[k-1]:
                    nums[i] = ""
                else:
                    nums[i], nums[k-1] = nums[k-1], nums[i] 

        for i in range(len(nums)):
            if nums[i] == "":
                return i+1
        return n+1