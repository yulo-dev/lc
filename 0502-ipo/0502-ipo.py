class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

        proj = sorted(zip(capital, profits))
        h = [] # max heap
        i = 0

        for _ in range(k):

            while i < len(proj) and proj[i][0] <= w:
                heapq.heappush(h, -proj[i][1]) #profit
                i += 1

            if not h:
                break

            w += -heapq.heappop(h)

        return w