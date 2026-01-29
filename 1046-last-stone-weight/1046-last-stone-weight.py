class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = [-x for x in stones]
        heapq.heapify(h)

        while len(h) > 1:
            y = -heapq.heappop(h)  # largest
            x = -heapq.heappop(h)  # second largest

            if y != x:
                heapq.heappush(h, -(y - x))

            #不用特別寫兩顆石頭相同時的情況 因為這情況下兩顆石頭應該要被砸碎然後消失
            #所以就是他們都被pop出來然後不處理 也不push回去 下一輪也不會再出現 就代表消失了
        
        return -h[0] if h else 0
