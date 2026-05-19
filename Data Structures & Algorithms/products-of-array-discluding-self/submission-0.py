class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        one = [1] * len(nums)
        two = [1] * len(nums)

        one[0] = nums[0]
        score = nums[0]
        for i in range(1, len(nums)):
            one[i] = nums[i]*score
            score = one[i]
        
        k = len(two) - 1
        two[k] = nums[k]
        prod = nums[k]
        for i in range(k-1, -1, -1):
            two[i] = prod*nums[i]
            prod = two[i]

        nums[0] = two[1]
        nums[k] = one[k-1]

        for i in range(1, k):
            nums[i] = one[i-1]*two[i+1]

        return nums  
