class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()

        max_len  = 0
        curr_len = 1

        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]-1:
                curr_len += 1
            elif nums[i] == nums[i+1]:
                curr_len = curr_len
            else:
                curr_len = 1
            
            if curr_len > max_len:
                max_len = curr_len

        if curr_len > max_len:
                max_len = curr_len
            
        if not nums:
            return 0
        else:
            return max_len