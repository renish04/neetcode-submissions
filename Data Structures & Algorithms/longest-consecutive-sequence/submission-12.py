class Solution:
    def longestConsecutive(self, nums):
        nums_set = set(nums)
        nums_start = []
        for num in nums_set:
            if num - 1 not in nums_set:
                nums_start.append(num)

        if len(nums) >=  len(nums_start):
            k = len(nums) - len(nums_start)
        else:
             k = len(nums_start) - len(nums)

        max_count = 0
        for x in range(len(nums_start)):
            i = 1
            temp_count = 1

            while i < len(nums)+1 - max_count:

                if nums_start[x] + i in nums_set:
                    temp_count += 1
                    i += 1
                else:
                    if temp_count > max_count:
                        max_count = temp_count
                    break
            if max_count >= k:
                break
        return max_count