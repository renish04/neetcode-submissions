class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[target - nums[i]] = i
            else:
                return [hashmap[nums[i]], i]