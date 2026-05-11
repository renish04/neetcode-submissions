class Solution:
    def getConcatenation(self, nums):
        ans = []
        for i in range(len(nums)):
            ans.append(nums[i])
            if len(ans) == len(nums):
                for i in range(len(nums)):
                    ans.append(nums[i])
            
        return ans

        