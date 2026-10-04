class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        res = []

        for element in intervals:
            
            start = element[0]
            end = element[1]

            if len(res) == 0:
                res.append([start, end])
            else:
                last_start = res[-1][0]
                last_end = res[-1][1]
                if start <= last_end:
                    res[-1][0] = min(start, last_start)
                    res[-1][1] = max(end, last_end)
                else:
                    res.append([start, end])
                
        return res