class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = -1
                i += 1
            else:
                k = nums[i]
                if nums[i] == nums[k-1]:
                    if i != k -1 :
                        nums[i] = -1
                        i += 1
                    else:
                        i += 1
                else:
                    nums[i], nums[k-1] = nums[k-1], nums[i]
                    
        print(nums)
        for i in range(n):
            if nums[i] == -1:
                print("wnet")
                return i + 1
        return n + 1