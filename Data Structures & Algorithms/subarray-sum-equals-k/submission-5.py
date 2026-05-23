class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_nums = [0] * len(nums)

        hold = 0
        for i in range(len(nums)):
            sum_nums[i] = hold + nums[i]
            hold = sum_nums[i]

        hash_check = {0:1}
        tot_sub = 0
        for i in range(len(sum_nums)):
            if sum_nums[i] - k in hash_check:
                tot_sub += hash_check[sum_nums[i]-k]
                if sum_nums[i] in hash_check:
                    hash_check[sum_nums[i]] += 1
                else:
                    hash_check[sum_nums[i]] = 1
            else:
                if sum_nums[i] in hash_check:
                    hash_check[sum_nums[i]] += 1
                else:
                    hash_check[sum_nums[i]] = 1
        
        return tot_sub