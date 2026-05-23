class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr1 = [0] * n
        arr2 = [0] * n
        final = []

        prod = 1
        for i in range(n):
            arr1[i] = prod*nums[i]
            prod = arr1[i]

        prod = 1
        for i in range(n-1, -1, -1 ):
            arr2[i] = prod*nums[i]
            prod = arr2[i]

        for i in range(n):
            if i == 0:
                final.append(arr2[i+1])

            elif i == n-1:
                final.append(arr1[i-1])

            else:
                final.append(arr1[i-1]*arr2[i+1])

        return final
