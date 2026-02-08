class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        queue = deque() # store indices
        res = []

        for right in range(len(nums)):
            left = right - k + 1
            
            # 1) remove expired index (out of window)
            if queue and queue[0] < left:
                queue.popleft()
            
            # 2) maintain decreasing order
            while queue and nums[queue[-1]] <= nums[right]:
                queue.pop()

            # 3) add current index
            queue.append(right)

            # 4) record answer when window is ready
            if right >= k - 1:
                res.append(nums[queue[0]])
        
        return res