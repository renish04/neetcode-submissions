class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_profit = 0

        for i in range(1, len(prices)):
            if nums[i] > nums[i-1]:
                total_profit += nums[i] - nums[i-1]

        return total_profit 