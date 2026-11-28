class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        buy = 0
        profit = float("-inf")

        for sell in range(len(prices)):
            if prices[sell] < prices[buy]:
                buy = sell
            
            profit = max(profit, prices[sell] - prices[buy])
        
        return profit