class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        
        from collections import deque

        queue = deque([])

        for idx, val in enumerate(tickets):
            queue.append((idx, val))

        time = 0
        while queue:
            idx, val = queue.popleft()
            val -= 1
            time += 1
            
            if idx == k and val == 0:
                return time

            if val > 0:
                queue.append((idx, val))