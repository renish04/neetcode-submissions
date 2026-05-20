class Solution:
    def longestConsecutive(self, nums):
        nums_set = set(nums)
        nums_start = []
        for i in range(len(nums)):
            if nums[i] - 1 not in nums_set:
                nums_start.append(nums[i])

        if len(nums_set) >=  len(nums_start):
            k = len(nums_set) - len(nums_start)
        else:
             k = len(nums_start) - len(nums_set)

        max_count = 0
        for x in range(len(nums_start)):
            i = 1
            temp_count = 1

            while i < len(nums)+1:

                if nums_start[x] + i in nums_set:
                    temp_count += 1
                    i += 1
                else:
                    if temp_count > max_count:
                        max_count = temp_count
                    break
        return max_count