class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort()
        res = 0
        new_interval = []

        for element in intervals:
            start = element[0]
            end = element[1]

            if not new_interval:
                new_interval.append([start, end])
            else:
                prev_start = new_interval[-1][0]
                prev_end = new_interval[-1][1]

                if start < prev_end:
                    res += 1
                    if end <= prev_end:
                        new_interval[-1][0] = start
                        new_interval[-1][1] = end
                else:
                    new_interval.append([start, end])
 
        return res