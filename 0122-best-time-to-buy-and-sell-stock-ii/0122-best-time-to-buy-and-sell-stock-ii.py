class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 邊界處理：若價格清單為空，獲利為 0
        if not prices:
            return 0

        # 初始化買入價格為第一天的價格
        buy = prices[0]
        profit = 0


        # 開始遍歷價格流（此處的 sell 代表「今日價格」）
        for sell in prices:
            # 意識點：如果今日價格高於昨日價格（buy），則存在獲利空間
            if sell > buy:
                # 累加這段微小的價差到總利潤中
                profit += sell - buy

            # 關鍵動作：將今日價格更新為「下一輪的昨日價格」
            # 這樣在下一輪迴圈中，我們就是在比較「明天」與「今天」
            buy = sell

        return profit