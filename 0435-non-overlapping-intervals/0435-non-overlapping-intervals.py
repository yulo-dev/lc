class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        
        intervals.sort()
        res = 0
        min_end = intervals[0][1]

        for i in range(1, len(intervals)):

            if min_end > intervals[i][0]:
                res += 1
                min_end = min(min_end, intervals[i][1])
            else:
                min_end = intervals[i][1]

        return res

              
