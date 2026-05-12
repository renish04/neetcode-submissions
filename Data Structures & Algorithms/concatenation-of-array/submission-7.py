class Solution:
    def getConcatenation(self, nums):
        conc = []
        for i in range(len(nums)):
            conc.append(nums[i])

        if len(nums) == len(conc):
            for i in range(len(nums)):
                conc.append(nums[i])
        
        