class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        tot = 0
        sub_score = 0
        map_list = {0:1}

        for i in range(len(nums)):
            nums[i] = nums[i] + tot
            tot = nums[i]
            if nums[i] - k in map_list:
                sub_score += map_list[nums[i]-k]
            if nums[i] in map_list:
                map_list[nums[i]] += 1
            elif nums[i] not in map_list:
                map_list[nums[i]] = 1
        
        return sub_score
