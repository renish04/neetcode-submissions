class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre_sum = 0
        for i in range(len(nums)):
            nums[i] += pre_sum
            pre_sum = nums[i]

        hash_nums = {}

        for i in range(len(nums)):
            if nums[i] not in hash_nums:
                hash_nums[nums[i]] = 1
            else:
                hash_nums[nums[i]] += 1

        total_sub_arrays = 0
        for x in hash_nums:
            if x == k:
                total_sub_arrays += hash_nums[x]
            elif x!= k and x-k in hash_nums:
                total_sub_arrays += hash_nums[x-k]
        print(nums)
        print(hash_nums)
        return total_sub_arrays 