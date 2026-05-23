class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] <=0 or nums[i] > len(nums):
                nums[i] = ""
            else:
                k = nums[i]
                if nums[k-1] == k and i != k-1:
                    nums[i] = ""
                else:
                    if nums[k-1] <= 0 or nums[k-1] > len(nums):
                        nums[k-1] = ""
                    nums[i], nums[k-1] = nums[k-1], nums[i]
        print(nums)    
        for i in range(len(nums)):
            if nums[i] == "":
                return i+1
            else:
                continue

        return len(nums)+1