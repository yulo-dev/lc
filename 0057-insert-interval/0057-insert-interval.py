class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        new_start, new_end = newInterval
        inserted = False

        for start, end in intervals:
            #left
            if end < new_start:
                res.append([start, end])
            #right
            elif new_end < start:
                if not inserted:
                    res.append([new_start, new_end])
                    inserted = True

                res.append([start, end])
            else:
                new_start = min(new_start, start)
                new_end = max(new_end, end)

        if not inserted:
            res.append([new_start, new_end])

        return res