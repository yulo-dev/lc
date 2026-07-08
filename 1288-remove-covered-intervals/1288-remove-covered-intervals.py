class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        n = len(intervals)

        for i in range(1, len(intervals)):
            prev = intervals[i-1]
            curr = intervals[i]

            if (prev[0] <= curr[0] and curr[1] <= prev[1]):
                n -= 1
                curr[0] = prev[0] 
                curr[1] = prev[1] 

            elif (curr[0] <= prev[0] and prev[1] <= curr[1]):
                n -= 1

        return n
