class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        i = 0
        j = i+1

        while i < len(prices)-2 and j < len(prices)-1:
            if prices[j] < prices[i]:
                i = j
                j = i+1
            else:
                if prices[j] - prices[i] > profit:
                    profit = prices[j] - prices[i]
                    j += 1
                else:
                    j += 1
            

        

        return profit