class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_start = []
        nums_set = set(nums)

        for num in nums_set:
            if num-1 not in nums_set:
                nums_start.append(num)

        max_sequence = 0

        for i in range(len(nums_start)):
            temp_max = 1
            for j in range(1, len(nums)):
                if nums_start[i] + j  in nums_set:
                    temp_max += 1
                else:
                    break
            if temp_max > max_sequence:
                max_sequence = temp_max
        
        return max_sequence
                
        
