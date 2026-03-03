class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def can_finish(speed):
            hours = 0
            for p in piles:
                hours += (p + speed - 1) // speed # 向上取整
            return hours <= h

        
        #最小就是每小時只吃一根 最多就是每小時吃max piles根
        left = 1
        right = max(piles) #max piles
        ans = right # 先存一個保險的答案

        while left <= right:
            mid = left + (right - left) // 2

            if can_finish(mid):
                ans = mid       # 這個速度行，試試看能不能更慢
                right = mid - 1 
            else:
                left = mid + 1  # 太慢了，吃不完，加快速度

        return ans