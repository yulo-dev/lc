class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:

        jobs = sorted(zip(startTime, endTime, profit), key = lambda x: x[1]) 
        n = len(jobs)
        dp = [0] * (n+1)

        for i in range(n):
        
            curr_start, curr_end, curr_profit = jobs[i]
            left = 0
            right = i
            best_prev_idx = 0

            while left < right:
                mid = left + (right-left) // 2

                if jobs[mid][1] <= curr_start:
                    best_prev_idx = mid + 1
                    left = mid + 1
                else:
                    right = mid 

            #1-indexed
            dp[i + 1] = max(dp[i], curr_profit + dp[best_prev_idx])

        return dp[n]
                
