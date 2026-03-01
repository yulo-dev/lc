class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        
        left = 0
        right = len(height) - 1
        left_max = height[left]
        right_max = height[right]
        res = 0
        
        while left < right:
            # 誰小就處理誰，因為「短板」決定水量
            # 【左邊小，代表左邊這區塊的水位已經由 left_max 封頂了】
            if left_max < right_max:
                left += 1 # 踏入新領地
                left_max = max(left_max, height[left]) # 看看新領地的牆高
                res += left_max - height[left] # 【立刻結算】這塊新領地的水
            else:
                # 【右邊小，代表右邊這區塊的水位已經由 right_max 封頂了】
                right -= 1 # 踏入新領地
                right_max = max(right_max, height[right])
                res += right_max - height[right] # 【立刻結算】這塊新領地的水
                
        return res


# two pointers: 
# 雙指針最難理解的地方在於：我站在左邊，明明不知道右邊「全部」的牆長怎樣，為什麼我敢算水量？
    # 當 left_max（左邊目前的最高）比 right_max（右邊目前的最高）小時：
    # 1. 我們雖然不知道 left 指針和 right 指針「中間」還有沒有更高的牆。
    # 2. 但我們百分之百確定：對 left 這格來說，右邊至少有一面牆（就是現在看到的 right_max）比左邊高。
    # 3. 既然右邊已經有更高的擋著了，那麼限制 left 這格水位的「瓶頸」肯定就是左邊的 left_max。