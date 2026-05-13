class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        map_nums = {}
        for i in range(len(nums)):
            if nums[i] not in map_nums:
                map_nums[nums[i]] = 1
            else:
                map_nums[nums[i]] += 1
        
        for i in map_nums:
            
            x = len(nums) / 2
            if  map_nums[i] > x:
                return i
                