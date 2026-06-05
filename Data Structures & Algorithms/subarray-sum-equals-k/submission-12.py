class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prev = 0
        for i in range(len(nums)):
            nums[i] = prev + nums[i]
            prev = nums[i]

        sub = 0
        hm = {0 : 1}
        

        for i in range(len(nums)):
            if nums[i] - k in hm:
                sub += hm[nums[i]-k]
            if nums[i] in hm:
                hm[nums[i]] += 1
            else:
                hm[nums[i]] = 1    
        
        return sub