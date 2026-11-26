class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        
        buy = sell = 0
        profit = 0

        for i in range(1,len(prices)):

            if prices[i] < prices[buy]:
                buy = i
                sell = i
            
            if prices[i] > prices[sell]:
                sell = i

            profit = max(profit,  prices[sell] - prices[buy])

        return profit