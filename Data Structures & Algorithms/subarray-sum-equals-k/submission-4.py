class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre_sum = 0
        for i in range(len(nums)):
            nums[i] += pre_sum
            pre_sum = nums[i]

        hash_nums = {}
        total_sub_arrays = 0

        for i in range(len(nums)):
            if nums[i] == k:
                total_sub_arrays += 1
                if nums[i] - k in hash_nums:
                    total_sub_arrays += hash_nums[nums[i]-k]
                if nums[i] in hash_nums:
                    hash_nums[nums[i]] += 1
                else:
                    hash_nums[nums[i]] = 1
            elif nums[i] != k and nums[i] - k in hash_nums:
                total_sub_arrays += hash_nums[nums[i]-k]
                if nums[i] in hash_nums:
                    hash_nums[nums[i]] += 1
                else:
                    hash_nums[nums[i]] = 1
            else:
                if nums[i] in hash_nums:
                    hash_nums[nums[i]] += 1
                else:
                    hash_nums[nums[i]] = 1

        return total_sub_arrays 