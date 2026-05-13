class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapnum = {}

        for i in range(len(nums)):
            x = target - nums[i]

            if nums[i] not in mapnum:
                mapnum[x] = i

            elif nums[i] in mapnum:
                return [mapnum[nums[i]], i]