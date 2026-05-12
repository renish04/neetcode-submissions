class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sumdict = {}
        for i in range(len(nums)):
 
            x = target - nums[i]
            if nums[i] in sumdict:
                y = sumdict[nums[i]]
                return [y, i]
            else:
                sumdict[x] = i
                print(sumdict)

