class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr1 = []
        arr2 = []
        final = []

        score = 1
        for i in range(len(nums)):
            arr1.append(score*nums[i])
            score = arr1[i]
        score = 1
        for i in range(len(nums)-1, -1, -1):
            arr2.append(score*nums[i])
            score = arr2[i]
        
        for i in range(len(nums)):
            if i == 0:
                final.append(arr2[len(nums)-2])
            elif i == len(nums)-1:
                final.append(arr1[i-1])
            else:
                final.append(arr1[i-1]*arr2[len(nums)-1-(i+1)])
        return final