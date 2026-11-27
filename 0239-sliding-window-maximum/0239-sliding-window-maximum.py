class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:

        from collections import deque
        queue = deque()
        
        res = []
        
        for right in range(len(nums)):

            if right >= k and nums[right - k] == queue[0]:
                queue.popleft()

            while queue and nums[right] > queue[-1]:
                queue.pop()
            
            queue.append(nums[right])
            
            if right >= k-1:
                res.append(queue[0])

        return res