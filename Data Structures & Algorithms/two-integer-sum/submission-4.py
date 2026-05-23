class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_hash = {}

        for i in range(len(nums)):
            if target-nums[i] in sum_hash:
                return [sum_hash[nums[i]-target], i]
            else:
                sum_hash[nums[i]] = i
