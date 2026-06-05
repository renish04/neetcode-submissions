class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prev = 0
        for i in range(len(nums)):
            nums[i] = prev + nums[i]
            prev = nums[i]

        sub = 0
        hm = set()
        hm.add(0)

        for i in range(len(nums)):
            if nums[i] in hm:
                sub += 1
            if num[i] - k in hm:
                sub += 1
            hm.add(nums[i])
        
        return sub