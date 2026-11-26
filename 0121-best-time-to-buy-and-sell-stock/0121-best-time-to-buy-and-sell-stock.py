class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        
        buy = 0
        profit = 0

        for i in range(1,len(prices)):
            if prices[i] < prices[buy]:
                buy = i

            profit = max(profit,  prices[i] - prices[buy])

        return profit